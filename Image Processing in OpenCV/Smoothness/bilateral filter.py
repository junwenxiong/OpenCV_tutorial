import cv2 as cv
import numpy as np

# src = cv.imread('resource\\rain_on_face.png')
src = cv.imread('C:\\Users\\xjw\\Desktop\\yzh.jpg')
cv.imshow("src", src)
dst = cv.bilateralFilter(src, 0 ,100, 10)
cv.imshow('bf', dst)
cv.waitKey(0)
cv.destroyAllWindows()