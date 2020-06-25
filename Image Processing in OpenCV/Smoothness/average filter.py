import cv2
import numpy as np
import matplotlib.pyplot as plt

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


# 均值滤波
# uses 3x3 filter
def average_filter(img, kernel_size=3):
    result = cv2.blur(img,  (kernel_size, kernel_size))   
    cv2.imshow('average', result)

## custom filter 
def custom_filter(img):
    kernel = np.array([[1,0,1],
                       [-2,0,-2],
                       [1,0,1]],
                       dtype=np.float32)
                    
    # kernel = np.ones((kernel_size, kernel_size), np.float32)/25
    dst = cv2.filter2D(img, -1, kernel)
    print(dst.shape)
    cv2.imshow('custom', dst)

# gaussian filter
def gaussian_filter(img, kernel_size=5):
    res = cv2.GaussianBlur(img,(kernel_size, kernel_size),0)
    cv2.imshow('gaussian', res)

# median filter
def median_filter(img, kernel_size=5):
    result = cv2.medianBlur(img, kernel_size)
    cv2.imshow('median', result)


if __name__ == "__main__":

    img = cv2.imread('resource\\data\\pic2.png')
    source = cv2. cvtColor(img, cv2.COLOR_BGR2RGB)

    img_noise = add_noise(img)
    average_filter(img_noise)
    custom_filter(img_noise)
    gaussian_filter(img_noise,kernel_size=5)
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