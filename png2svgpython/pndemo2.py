import cv2
import os
img_file = 'test/input/mypngphoto.png'
image = cv2.imread(img_file, cv2.IMREAD_ANYDEPTH)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", image)
cv2.waitKey()