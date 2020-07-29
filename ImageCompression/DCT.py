"""
Description: Discrete Cosine Transform

author: xjw

date: 2020-7-29
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import util
"""
add salt&pepper noise
"""
def add_noise(img):
    rows, cols, channels = img.shape
    for i in range(500):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        if np.random.randint(0,1) == 0:
            img[x,y] = 0
        else:
            img[x, y] = 255
    return img

"""
@param  
"""
def denoising(img, sigma, psize=8):
    img_out = np.zeros(img.shape, np.uint8)
    cv2.xphoto.dctDenoising(img, img_out, sigma, psize)
    return img_out


if __name__ == "__main__":
    str = "resource/1_sp_noise.jpg"
    img = cv2.imread(str)
    cv2.imshow("original image", img)

    img_denoising = denoising(img, 45, 8)
    cv2.imshow("denoising image", img_denoising)
    cv2.waitKey(0)