import cv2 as cv
import numpy as np

img = cv.imread("D:\\CodingFolder\\OPENCVFolder\\resource\\7.jpeg")

px = img[100,100]

blue = img[100,100,0]
# print(blue)
# print(px)
# accessing RED value
# print(img[10,10])
# print(img.item(10,10,0))


# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

# access shape of image
print(img.shape)

# access size of image , shape[0] * shape[1] * shape[2]
# print(img.size)

# access datatype of image
# print(img.dtype)

ROI = img[230:340, 250:660]

# split B,G,R channels
b,g,r = cv.split(img)
img = cv.merge((r,g,b))

# set pixels of  R channels to equal zero
img[:,:,2] = 0

cv.imshow("input image", img)
cv.imshow("ROI", ROI)
cv.waitKey(0)
cv.destroyAllWindows()