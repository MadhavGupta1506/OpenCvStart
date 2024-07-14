import cv2 as cv
import numpy as np


img1=np.zeros((250,500,3),np.uint8)
img1=cv.circle(img1,(250,125),125,(255,255,255),-1)
img2=cv.imread("images/BW.png")


bitand=cv.bitwise_and(img2,img1)
bitor=cv.bitwise_or(img2,img1)
bitxor=cv.bitwise_xor(img2,img1)



cv.imshow("Img1",img1)
cv.imshow("Img2",img2)
cv.imshow("Bit And",bitand)
cv.imshow("Bit Or",bitor)
cv.imshow("Bit Xor",bitxor)



# img=cv.imread(z)




cv.waitKey(0)
cv.destroyAllWindows()