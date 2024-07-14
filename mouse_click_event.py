import cv2 as cv
import numpy as np
import random as rd
def click_event(event,x,y,flags,param):
    if(event==cv.EVENT_LBUTTONDOWN):
        font=cv.FONT_HERSHEY_DUPLEX
        strxy=str(x)+" "+str(y)
        cv.putText(img,strxy,(x,y),font,1,(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)),2)
        cv.imshow("Image",img)
img=np.zeros((522,522,3),np.uint8)
cv.imshow("Image",img)

cv.setMouseCallback("Image",click_event)

cv.waitKey(0)
cv.destroyAllWindows()