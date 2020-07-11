import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
    # capture frame-by-frame, 
    # read() return a bool
    ret, frame = cap.read()
    # get specified property of the video by the different number 
    # which range from 0 to 18
    width = cap.get(3)
    height = cap.get(4)
    print("width = %s, height = %s" % (width, height))
    # sets width to 320 and height to 240
    ret = cap.set(3, 320)
    ret = cap.set(4, 240)

    # convert to gray image 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()