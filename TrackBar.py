import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv.namedWindow("Image")

cv.createTrackbar("B","Image",0,255,nothing)
cv.createTrackbar("G","Image",0,255,nothing)
cv.createTrackbar("R","Image",0,255,nothing)

while(1):
    cv.imshow("Image",img)
    k=cv.waitKey(1) & 0xFF
    if(k==27):
        break
    b=cv.getTrackbarPos("B","Image")
    g=cv.getTrackbarPos("G","Image")
    r=cv.getTrackbarPos("R","Image")
    img[:]=[b,g,r]    
# cv.waitKey(0)
cv.destroyAllWindows()