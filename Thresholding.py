import cv2 as cv
import numpy as np

img=cv.imread("images/IMG_7489.jpg")
img=cv.resize(img,(700,400),)

_,th1=cv.threshold(img,100,255,cv.THRESH_BINARY)
# _,th2=cv.threshold(img,100,255,cv.THRESH_BINARY_INV)

_,th3=cv.threshold(img,100,255,cv.THRESH_TRUNC)



cv.imshow("image",img)
cv.imshow("Threshold1",th1)
# cv.imshow("Threshold2",th2)
cv.imshow("Threshold3",th3)



cv.waitKey(0)
cv.destroyAllWindows()