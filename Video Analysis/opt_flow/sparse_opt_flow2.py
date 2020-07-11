import cv2 
import numpy as np

# 设置Shi-Tomasi角点检测参数
feature_params = dict(maxCorners = 300, qualityLevel = 0.2, minDistance = 2, blockSize = 7)

# lucas kanada optical flow参数
lk_params = dict(
                winSize = (15,15),
                maxLevel = 2,
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# 创造随机颜色
color = (0,255,0)

# 提取第一帧并找到其的转为灰度图像
cap = cv2.VideoCapture("resource/Car.mp4")
ret, first_frame = cap.read()
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# 返回所有满足要求的角点的位置,角点为用Shi-Tomasi方法找到的最强的角点，后面使用optical flow追踪这些角点
p0 = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)

# 因为角点位置为float，需要将其转为int型
# corners = np.int0(corners)
# 

mask = np.zeros_like(first_frame)

while(cap.isOpened()):
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用Lucas-Kanade方法计算sparse optical flow
    p1, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, p0, None, **lk_params)

    # 选择一些好的点
    good_olds = p0[status == 1]
    good_news = p1[status == 1]
    # 画optical flow的轨迹
    for i , (new, old) in enumerate(zip(good_news, good_olds)):
        # 返回一个展平后的数组
        x0, y0 = new.ravel()
        x1, y1 = old.ravel()
        # 从新坐标到旧坐标画一根color颜色的厚度为2的直线
        mask = cv2.line(mask, (x0, y0), (x1, y1), color, 2)
        # 在新坐标画一个半径为3的color颜色的厚度为-1的圆圈
        frame = cv2.circle(frame, (x0, y0), 3, color, -1)
    
    img = cv2.add(frame, mask)
    cv2.imshow("result", img)
    prev_gray = frame_gray.copy()
    p0= good_news.reshape(-1, 1, 2)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
