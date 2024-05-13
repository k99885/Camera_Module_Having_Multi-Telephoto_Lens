import numpy as np, cv2
import sys

#image = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR) # 컬러 영상 읽기
#if image is None: raise Exception("영상 파일 읽기 오류")

def Barrel(input_image_path, output_image_path):
    #k1, k2, k3 = 0.5, 0.2, 0.0
    k1, k2, k3 = -0.04, 0, 0
    img3 = cv2.imread(input_image_path)

    rows, cols = img3.shape[:2]
    # 매핑 배열을 생성해 줍니다.

    mapy, mapx = np.indices((rows, cols), dtype=np.float32)

    # 중앙점 좌표로 -1~1 정규화

    mapx = 2 * mapx / (cols - 1) - 1
    mapy = 2 * mapy / (rows - 1) - 1

    #극좌표로 변환
    r, theta = cv2.cartToPolar(mapx, mapy)
    #왜곡 제거
    ru = r * (1+ k1 * (r ** 2))                                                              #+ k2 * (r ** 4) + k3 * (r ** 6))
    # 직교 좌표로 변환
    mapx, mapy = cv2.polarToCart(ru, theta)


    mapx = ((mapx + 1) * cols - 1) / 2
    mapy = ((mapy + 1) * rows - 1) / 2

    # 리매핑하기

    distored = cv2.remap(img3, mapx, mapy, cv2.INTER_LINEAR)

    cv2.imwrite(output_image_path, distored)




img_names = ['images/51.jpeg', 'images/512.jpg','images/513.jpg','images/514.jpg']
# img_names = ['images/51.jpeg','images/54.jpeg']

#img_names = ['images/41.dng', 'images/44.dng']

imgs = []

for name in img_names:

    img = cv2.imread(name)

    if img is None:

        print('Image load failed!')

        sys.exit()
    imgs.append(img)

stitcher = cv2.Stitcher_create()
status, dst = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:

    print('Stitch failed!')

    sys.exit()


cv2.imwrite('output1.jpg', dst)
#cv2.namedWindow('dst',cv2.WINDOW_NORMAL)
#cv2.imshow('dst', dst)
print("done1")

Barrel("output1.jpg", "output_image.jpg")

print("done4")
cv2.waitKey()
cv2.destroyAllWindows()
