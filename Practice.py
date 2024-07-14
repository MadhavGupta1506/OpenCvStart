import cv2 as cv
import numpy as np
img=cv.imread("images/IMG_7489.jpg",1)

resized=cv.resize(img,(700,500),interpolation=cv.INTER_AREA)
cv.imshow("Cat",resized)

# Gausian Blur
Blur=cv.GaussianBlur(resized,(1,1),10)

cv.imshow("Gaussian Blur",Blur)

# Median Blur
Blur=cv.medianBlur(resized,5)
cv.imshow("Median Blur",Blur)
cv.waitKey(0)