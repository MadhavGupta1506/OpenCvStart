import numpy as np
import cv2 as cv

img=cv.imread("images/OpenCvLogo.png")
imgray=cv.imread("images/OpenCvLogo.png",0)

ret,thresh=cv.threshold(imgray,127,255,0)
contour,hierarchy=cv.findContours(imgray,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

print("no. of contours:"+str(len(contour)))
print(contour[0])

cv.drawContours(img,contour,1,(0,255,22),3)

cv.imshow("Image",img)
cv.imshow("Image Gray",imgray)
cv.waitKey(0)
cv.destroyAllWindows()