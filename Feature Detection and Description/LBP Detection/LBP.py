import cv2 

img = cv2.imread('resource/yzh.jpg')

face_detect = cv2.CascadeClassifier('Feature Detection and Description\\LBP Detection\\lbpcascade_frontalface_improved.xml')

gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
face_zone = face_detect.detectMultiScale(gray, scaleFactor=2, minNeighbors=2)
print('face_zone: \n', face_zone) # return x,y,w,h
for x, y, w, h in face_zone:
    cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h), color=[0,0,255], thickness=2)

    cv2.circle(img, center=(x+w//2, y+h//2), radius=w//2, color=[0,255,0], thickness=2)

cv2.namedWindow('Easmount-CSDN',0)

cv2.imshow('result', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
