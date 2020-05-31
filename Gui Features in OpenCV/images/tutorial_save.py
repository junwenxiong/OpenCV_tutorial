import cv2 as cv
import numpy as np

# 第二个参数是读取图像的方式
# IMREAD_COLOR: loads a color image  --1
# IMREAD_GRAYSCALE: loads image in grayscale mode --0
# IMREAD_UNCHANGED: loads image as such including alpha channel -- -1
img = cv.imread("D:/CodingFolder/OPENCVFolder/resource/1.jpg", 0)
cv.imshow("input image", img)
k = cv.waitKey(0) & 0xFF
if k == 27: # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('D:/CodingFolder/OPENCVFolder/resource/1-test.jpg', img)
    cv.destroyAllWindows()