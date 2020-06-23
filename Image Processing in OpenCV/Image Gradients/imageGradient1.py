import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('resource\\data\\left01.jpg')
print(img.shape)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

absX = cv2.convertScaleAbs(sobel_x)
absY = cv2.convertScaleAbs(sobel_y)

dst = cv2.addWeighted(absX,0.5, absY, 0.5, 0)

plt.subplot(2,3,1),plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3), plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel_x'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4), plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel_y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5), plt.imshow(dst, cmap='gray')
plt.title('dst'), plt.xticks([]), plt.yticks([])

plt.show()
