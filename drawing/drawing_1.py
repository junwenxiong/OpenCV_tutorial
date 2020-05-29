import numpy as np
import cv2 as cv

# Create a black image 
img = np.zeros((512, 512, 3), np.uint8)


# Draw a diagonal blue line with thickness of 10 px
img_line = cv.line(img, (511,0), (0, 511), (255,255,255), 10)

# (384, 0) is top-left corner 
# (510, 128) is bottom-right corner
img_rec = cv.rectangle(img, (384,0),(510,128),(0,255,0), 3)

# (447, 63) is center coordinates
# 63 is radius
img_cir = cv.circle(img, (447, 63), 63, (0,0,255), -1)

# (256,256) is the center location
# (100, 50) is axes length
# 30 is the angle of rotation of ellipse in anti-clockwise direction
# 0 and 360 is the startAngle and endAngle denotes the starting and ending of
# ellipse arc measured in clockwise direction from major axis.
img_ell = cv.ellipse(img, (256,256),(100,50),30,0,360,255,-1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# -1 表示 该维度自动计算元素个数
pts = pts.reshape((-1,1,2))
print(pts)
img_poly = cv.polylines(img, [pts], False, (0,255,255))

font = cv.FONT_HERSHEY_SIMPLEX
# some arguments given below
# Text data 
# Positin coordinates of where you want put it
# Font type 
# Font Scale
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255,255,255), 2, cv.LINE_AA)

cv.imshow("input image", img_rec);
cv.waitKey(0)
cv.destroyAllWindows()