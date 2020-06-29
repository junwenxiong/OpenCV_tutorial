import  cv2
import tkinter
import numpy as np
from matplotlib import pyplot as plt

#定义线性增强函数，<x1,x2>为增强区间
def linear_threshold(Image,h,w,x1,x2,z2,z1 = 0,z3 = 0):

    for i in range(0, h):
        for j in range(0, w):
            tmp = Image[i, j]
            if tmp < x1:
                Image[i, j] = z1
            elif tmp >= x1 and tmp < x2:
                Image[i, j] = z2
            else:
                Image[i, j] = z3

    return Image

#轮廓面积计算函数
def areaCal(contour):

    area = 0
    for i in range(len(contour)):
        area += cv2.contourArea(contour[i])

    return area


if __name__ == "__main__":
    img = cv2.imread('resource\\test.png')
    print(img.shape)
    
    cv2.imshow('img', img)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()