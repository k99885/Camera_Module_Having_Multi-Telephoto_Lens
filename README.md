# 다중 망원카메라를 이용한 광각 영상 구현
## Overview
(Wide-angle image implementation using multiple telephoto cameras)

바형 폴더블 스마트폰의 경우 외부 후면 카
메라의 위치가 외부 디스플레이와 동일한 위치에 존재하는 물리적 구조를 가
지고 있어 카메라 성능을 높이기 위해 큰 모듈과 많은 모듈을 탑재한다면 외
부 디스플레이 영역을 침범한다는 문제점을 가지고 있습니다. 
이때 폴더블의 경우 외부디스플레이 크기와 카메라 모듈의 성능은 모순적으로 
하나의 성능의 증가는 다른 하나의 성능 하락을 발생시켜 제한적인 카메라 모
듈 수를 가지고 있습니다 외부 디스플레이 또한 제한적인 크기로 화면 크기를 키
우지 못하는 문제점을 가지고 있습니다. 

이와 같은 문제점을 해결하기 위해 다중 망원카메라를 활용하여 취득한 메
가급 이미지를 병합스티칭하여 망원으로 해결하지 못하는 넓은 화각의 이미
지를 취득하는데 그 목적이 있습니다.
 
또한 최종적으로 병합된 이미지는 각 카메라모듈의 메가급 이미지의 합으로 
이뤄지기에 높은 해상도의 이미지가 취득되며 확대하여 이미지를 보더라도
종래의 디지털 크롭 보다 높은 해상도를 가질 수 있습니다.

## Table of contents
 - [1. 영상 취득](#1-영상-취득)
 - [2. 이미지 스티칭](#2-이미지-스티칭)
 - [3. 왜곡 제거](#3-왜곡-제거)
 - [4. 결과](#4-결과)

## 1. 영상 취득
![도면1](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/991f19c5-6379-4e73-885a-c176b9a1c5a4)
![도면2](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/c1e6d2cb-1da1-4f3c-941d-ff973b5ac814)

이와 같이 서로 다른 위치의 이미지를 취득하기 위해 일정 각도로 틸팅 되어있는 망원 모듈을 사용합니다.

실제로 장치를 구현하여 영상을 취득하면 좋겠지만 제한사항이 존재하여 아래와같은 카메라 거치대를 제작하였습니다.

![취득장치](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/25e1f5b5-ae66-497d-93ef-564d4bae2b53)
![각도 테스트 도면](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/449462ae-b230-458f-87e3-0cea8ded8549)

거치대에 스마트폰 카메라를 장착하고 도면을 사용하여 상하좌우 10도로 틸팅되어진 영상을 취득하였습니다.

![샘플영상](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/c14c224a-3e06-448b-b188-09aeaa543037)

망원카메라로 취득한영상 이기때문에 영상을 2배 줌 하여 좌우상하단 영상 4개를 취득하였습니다. 

![샘플 스펙](https://github.com/k99885/k99885-Wide-angle-image-implementation-using-multiple-telephoto-cameras/assets/157681578/e2d83d37-fa5f-49d5-a541-53c45449cbc6)

## 2. 이미지 스티칭
```
stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)
```
취득한 영상들을 opencv에서 제공하는 이미지스티칭함수를 사용하여 영상을 병합하였습니다.

![5_스티칭](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/910dd080-bfab-41e9-bfc9-ad982fe4fec4)


## 3. 왜곡 제거
![5_격자1](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/66f5f058-a63e-4ee1-9b9f-71a706e1bb6f)

이미지병합 과정중에 이미지에 왜곡이 발생하여 그리드를 추가하여 왜곡 정도를 확인하였습니다.

```
def Barrel(input_image_path, output_image_path):
    k1, k2, k3 = -0.04, 0, 0
    img3 = cv2.imread(input_image_path)

    rows, cols = img3.shape[:2]

    mapy, mapx = np.indices((rows, cols), dtype=np.float32)

    # 중앙점 좌표로 -1~1 정규화

    mapx = 2 * mapx / (cols - 1) - 1
    mapy = 2 * mapy / (rows - 1) - 1

    #극좌표로 변환
    r, theta = cv2.cartToPolar(mapx, mapy)
    #왜곡 제거
    ru = r * (1+ k1 * (r ** 2))
    # 직교 좌표로 변환
    mapx, mapy = cv2.polarToCart(ru, theta)

    mapx = ((mapx + 1) * cols - 1) / 2
    mapy = ((mapy + 1) * rows - 1) / 2

    distored = cv2.remap(img3, mapx, mapy, cv2.INTER_LINEAR)

    cv2.imwrite(output_image_path, distored)
```

변형된 모양이 베럴왜곡과 비슷한 형태를 가지고 있다고 생각하여 배럴왜곡을 보정하는 알고리즘을 사용하여 왜곡을 제거해주었습니다.

![5_격자_-0 06](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/d29a7969-a1c3-4b0f-a5a2-de206a9f72a0)

그리드가 적용된 이미지를 사용하여 왜곡이 어느정도 보정된것을 확인하였습니다.

## 4. 결과

![5_스티칭3_-0 04](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/6325d32f-0c3e-4d1b-b232-8218b8e58878)

![image](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/add3ce32-fcbd-444f-9f06-6c6f6aaa9e18)

최종적으로 망원카메라로 취득한영상(3024x3024)4개를 병합하여 4868x5250의 높은 해상도를 가진 하나의 영상을 취득하였습니다.

![image](https://github.com/k99885/Wide-angle-image-implementation-using-multiple-telephoto-cameras-/assets/157681578/a5b29c5a-e910-4229-acd3-f231be04474a)


