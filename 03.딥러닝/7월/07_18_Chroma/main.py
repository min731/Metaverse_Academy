import cv2
import numpy as np

# 0번 카메라
cap = cv2.VideoCapture(0)

# 배경
back_frame = cv2.imread('starry_night.jpg')

# 카메라 크기와 맞춰주기
back_frame = cv2.resize(
                            (back_frame,
                                (
                                int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                                )
                            )
                        )

# 합성변수
do_composit = True

while True:
    ret,frame = cap.read()

    if not ret:
        break

    if do_composit:
                # 보통 크로마키 색상 : 초록색 뽑기
        mask = cv2.inRange(frame,(0,100,0),(128,255,128))
        cv2.copyTo(back_frame,mask,frame)

    cv2.imshow('chroma',frame)

    # 스페이스바로 배경 바꾸기
    if cv2.waitKey(1) == ord(' '):
        do_composit = not do_composit