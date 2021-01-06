print('This is Car detection (¬‿¬)(¬‿¬)')

import cv2
from random import randrange

classifire_file = "car_class.xml"
classifire_file2 = "man_class.xml"
car_tracker = cv2.CascadeClassifier(classifire_file)
man_tracker = cv2.CascadeClassifier(classifire_file2)

image_car = "carimage.jpg"
img = cv2.imread(image_car)
video = cv2.VideoCapture('moto2.mp4')
blacknwhite = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

while True:
    boool, frame = video.read()
    # img = cv2.imread(frame)
    blacknwhite = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars = car_tracker.detectMultiScale(blacknwhite)
    for car in cars:
        (x , y , w , h) = car
        cv2.rectangle(frame,(x,y),(x+w,y+h),((0),(255),(0)),2)
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),2)
    
    mans = man_tracker.detectMultiScale(blacknwhite)
    for man in mans:
        (x , y , w , h) = man
        cv2.rectangle(frame,(x,y),(x+w,y+h),((255),(0),(0)),2)
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),2)

    cv2.imshow('car image', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break

# cars = car_tracker.detectMultiScale(blacknwhite)
# print(cars)
# for car in cars:
#     (x , y , w , h) = car
#     cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),2)

# cv2.imshow('car image', img)
# cv2.waitKey()