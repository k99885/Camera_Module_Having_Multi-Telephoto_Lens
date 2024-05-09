# 다중 망원카메라를 이용한 광각 영상 구현

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

## 2. 
