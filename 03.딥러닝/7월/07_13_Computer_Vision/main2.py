import cv2
import sys
import matplotlib.pyplot as plt

img = cv2.imshow('img1.jpg')
# 중요!
# 이미지마다 RGB 채널 순서가 다를 수 있음
# 차선 검출할 시에도 차선외에는 흑백으로 만듬
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imggray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

plt.axis('off')
plt.imshow(imggray)
plt.show()