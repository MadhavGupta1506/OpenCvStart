import cv2 as cv
import numpy as np

img=cv.imread('images/park.jpg')
cv.imshow("Boston",img)

# Converting to GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)


# Blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Edge cascading
cany=cv.Canny(blur,125,175)
cv.imshow("cany",cany)

# Dilating an image
dilated=cv.dilate(cany,(3,3),iterations=5)
cv.imshow('dilated',dilated)

# Eroding
eroded=cv.erode(dilated,(3,3),iterations=9)
cv.imshow('erode',eroded)


cv.waitKey(0)