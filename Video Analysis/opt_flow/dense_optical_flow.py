import cv2
import numpy as np

cap = cv2.VideoCapture("resource\\shibuya.mp4")

ret, first_frame = cap.read()

prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

mask = np.zeros_like(first_frame)
# 设置图像饱和度到最大
mask[...,1]=255

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow("input", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 用Farnevback 方法计算dense optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # 计算2D向量的幅度和角度
    magnitude, angle = cv2.cartToPolar(flow[...,0], flow[...,1])
    # 设置image hue 根据optical flow direction
    mask[..., 0] = angle * 180 / np.pi / 2
    # 根据optical flow magnitude 设置image value
    mask[...,2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    # HSV转为BGR
    rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

    cv2.imshow("Car", rgb)

    prev_gray=gray
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
