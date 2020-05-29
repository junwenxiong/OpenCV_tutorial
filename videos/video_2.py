import numpy as np
import cv2

cap = cv2.VideoCapture('D:\\CodingFolder\\OPENCVFolder\\resource\\nike_video.mp4')

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("width = %s, height = %s" % (cap.get(3), cap.get(4)))

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()