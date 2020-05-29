import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height: %s, width: %s, channels: %s" % (height, width, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255- pv
    cv.imshow("pixels_show", image)


print("--------Hello Python-----")
src = cv.imread("D:/CodingFolder/OPENCVFolder/resource/1.jpg")
# 指定图片是否可以resize，默认是WINDOW_AUTOSIZE, 如果是WINDOW_NORMAL
# 则可以resize图像
cv.namedWindow("input image", cv.WINDOW_NORMAL)
cv.imshow("input image", src)
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
print("time consumption: %d" % ((t2 - t1)/cv.getTickFrequency()))
# 参数单位是微秒，指定等待的时间，为0的话，等待键入关闭
cv.waitKey(0)
cv.destroyAllWindows()