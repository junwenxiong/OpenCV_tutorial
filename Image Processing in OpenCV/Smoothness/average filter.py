import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_noise(img):
    rows, cols, channels = img.shape
    for i in range(500):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        img[x, y ,:] = 255
    return img


# 均值滤波
# uses 3x3 filter
def median_filter(img, kernel_size=3):
    result = cv2.blur(img,  (kernel_size, kernel_size))   
    cv2.imshow('median', result)

if __name__ == "__main__":

    img = cv2.imread('resource\\1.jpg')
    source = cv2. cvtColor(img, cv2.COLOR_BGR2RGB)

    img_noise = add_noise(img)
    median_filter(img_noise)
    

    cv2.imshow('img_noise', img_noise)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # titles = ['img_noise', 'blur image (3, 3)', ]
    # images = [img_noise, result]

    # fig, axs = plt.subplots(3,1, figsize=(15,17))

    # for i in range(2):
    #     plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    # plt.show()