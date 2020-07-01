import cv2
print('Project Topic: Vehicle Classification')
print('By Junwen Xiong')

cascade_src = 'Feature Detection and Description\\Haar Feature Detection\\Car Detection\\cars.xml'

video_src = 'Feature Detection and Description\\Haar Feature Detection\\Car Detection\\video.avi'

# 参数可以为设备索引或者是文件名
cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    # 一帧一帧地捕获
    ret, img = cap.read()
    # print('ret', ret)
    if (type(img) == type(None)):
        break
    img = cv2.resize(img, (600,400))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1 , 2)

    for (x,y,w,h) in cars:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,255),2)
    cv2.imshow('video', img)

    if cv2.waitKey(0) == ord('q'):
        break 

cv2.destroyAllWindows()