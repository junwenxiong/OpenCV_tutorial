import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('resource\\data\\left01.jpg')

sobel_x = cv2.Sobel(img,-1, 1, 0, ksize=5)
sobel_x_64F = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
print(sobel_x.dtype, sobel_x_64F.dtype)

plt.subplot(121),plt.imshow(sobel_x, cmap='gray')
plt.title('soble_x'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(sobel_x_64F, cmap='gray')
plt.title('sobel_x_64F'), plt.xticks([]), plt.yticks([])

plt.show()