import cv2 
import numpy as np

filename = 'resource\\data\\chessboard.png'
img = cv2.imread(filename)
img = cv2.resize(img, dsize=(600,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
print('img.shape:',img.shape, 'gray.shape:',gray.shape)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,3,23,0.04)

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()] = [0,0,255]

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()