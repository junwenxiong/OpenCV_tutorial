import cv2 
import numpy as np

filename = 'resource\\data\\chessboard.png'
img = cv2.imread(filename)
img = cv2.resize(img, dsize=(600,400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

