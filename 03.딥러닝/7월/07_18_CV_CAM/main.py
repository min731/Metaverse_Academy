# 웹캠으로 한장씩 캡쳐
# 이미지 1장을 추론해서 예측

# 최소 30프레임의 영상

import cv2

# 비디어 캡쳐
vcap = cv2.VideoCapture(0) # 0번 카메라(Default 카메라)

# 카메라의 width
w = round(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 동영상을 저장하려면 코덱을 맞추어주어야함
# mp4 : 압축률이 좋음, 코덱-fmp4
codec = cv2.VideoWriter_fourcc(*'DIVX') # 코덱:DIVX

fps = round(vcap.get(cv2.CAP_PROP_FPS))
delay = round(1000/fps)
# print(fps,delay)

# fps 값은 카메라 fps보다 높을 수 없음
out = cv2.VideoWriter('out.avi',codec,fps,(w,h))

# 영상이므로 계속 대기
while True:
    ret, frame = vcap.read()

    print(ret,frame)

    # 캡쳐된 이미지가 없으면 끝내기
    if not ret:
        break

    # 좌우 반전
    frame = cv2.flip(frame,1)

    # inference
    out.write(frame)
    cv2.imshow('cam',frame)

    # 27 == 'esc'키
    if cv2.waitKey(1)==27:
        break

out.release()
vcap.release()
cv2.destroyAllWindows()