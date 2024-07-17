import cv2 as cv
import numpy as np

img=cv.imread("images/lady.jpg")
cv.imshow("Image",img)

img=cv.imread("images/lady.jpg")
cv.imshow("Image",img)


img=cv.imread("images/group 1.jpg")
# cv.imshow("Image",img)

gray=cv.imread("images/group 1.jpg",0)
cv.imshow("Grqy",gray)
haar_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Image",img)


cv.waitKey(0)
cv.destroyAllWindows()