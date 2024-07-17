import cv2 as cv
import numpy as np

img=cv.imread("images/lady.jpg")
cv.imshow("Image",img)



cv.waitKey(0)
cv.destroyAllWindows()