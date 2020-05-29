import cv2 as cv
import numpy as np

def video_demo():
    # 从摄像头中读入视频
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        cv.imshow("video", frame)
        frame = cv.flip(frame, 1) # 左右变换
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype) #每个像素的类型
    pixel_data = np.array(image)
    print(pixel_data)

print("-------------Hello Python -----------")
src = cv.imread("D:\\CodingFolder\\OPENCVFolder\\resource\\1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

get_image_info(src)
# video_demo()
# 转变为灰度图像
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# 第一个参数是图像名称， 第二个参数是想存入的图像
cv.imwrite("D:/CodingFolder/OPENCVFolder/resource/1-2.jpg", gray)
cv.waitKey(0)
cv.destroyAllWindows()