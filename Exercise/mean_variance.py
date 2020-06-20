import cv2
import numpy as np
import os

path = 'C:\\Users\\xjw\Desktop\\test_dataset\\'

size = (128,128)
for file in os.listdir(path):
    img = cv2.imread(path + file)
    img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    variance = np.var(img)
    print("filename : %s , image shape is %s , image variance is %s" % (file, img.shape, variance))

# img = cv2.imread('resource/1-1.jpg')

# variance = np.var(img, axis=0)
# print(variance)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()