# import cv2

# from random import randrange

# trained_data_face = cv2.CascadeClassifier('frontalface.xml')

# img = cv2.imread('RC.jpg')

# grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# face_coordinate = trained_data_face.detectMultiScale(grey_img)
# print(face_coordinate)

# # [[196 149 476 476]]
# for lst in face_coordinate:
#     (x , y , w , h) = lst
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,randrange(255),0),3)
# # cv2.circle()
# cv2.imshow('test RJ', img)
# cv2.waitKey()

import cv2
from random import randrange

trained_data_face = cv2.CascadeClassifier('frontalface.xml')

# img = cv2.imread('RC.jpg')
webcam = cv2.VideoCapture(0)

while True:
    boolean , frame = webcam.read()
    grey_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinate = trained_data_face.detectMultiScale(grey_img)

    for lst in face_coordinate:
        (x , y , w , h) = lst
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),3)
    cv2.imshow('test RJ', frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break


# face_coordinate = trained_data_face.detectMultiScale(grey_img)
# print(face_coordinate)

# # [[196 149 476 476]]
# for lst in face_coordinate:
#     (x , y , w , h) = lst
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,randrange(255),0),3)
# # cv2.circle()
# cv2.imshow('test RJ', img)
# cv2.waitKey()