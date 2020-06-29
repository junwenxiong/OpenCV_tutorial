import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_noise(img):
    rows, cols, channels = img.shape
    for i in range(5000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y ,:] = 0
    return img

def median_filter(img, kernel_size=5):
    result = cv2.medianBlur(img, kernel_size)
    cv2.imshow('median', result)

if __name__ == "__main__":
    img = cv2.imread('resource\\1_sp_noise.jpg')
    img = cv2.resize(img, (512, 512))
    # img_noise = add_noise(img)
    median_filter(img)
    # plt.subplot(1,2,1)
    # plt.imshow(img)
    # plt.show()

    cv2.imshow('img_noise', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()