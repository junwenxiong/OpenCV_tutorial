import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('resource\\1.jpg', 0)
img2 = cv2.imread('resource\\1.jpg')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
print('img1', img1,
        '\n gray', gray)
# ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# img2 = cv2.imread('resource\\1.jpg',-1)
# cv2.imshow('img1', img1)
# cv2.imshow('thresh1', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
