# OpenCV 설치
# pip install opencv-python
import cv2
import sys

img = cv2.imread('img1.jpg')

# 윈도우로 띄우겠다
cv2.imshow('Display Window',img)

# 대기
cv2.waitKey()

# 아무키나 누르면 창이 닫힘
cv2.destroyAllWindows()