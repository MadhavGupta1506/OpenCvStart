import numpy as np
import cv2 as cv

cap=cv.VideoCapture("Videos/vtest.avi.mp4")


ret,frame1=cap.read()
ret,frame2=cap.read()

while(cap.isOpened()):
    
    diff=cv.absdiff(frame1,frame2)
    
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    
    blur=cv.GaussianBlur(gray,(5,5),0)
    
    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    
    dilated=cv.dilate(thresh,None,3)
    
    contours ,_=cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_TC89_KCOS)
    
    for contour in contours:
        (x,y,w,h)=cv.boundingRect(contour)
        
        if(cv.contourArea(contour)>=400):
            cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(frame1,f"Status:Movement",(10,50),cv.FONT_HERSHEY_SIMPLEX,1,(3,242,255),2)
    
    # cv.drawContours(frame1,contour,-1,(0,22,242),2)
    cv.imshow("Video",frame1)
    
    frame1= frame2
    ret,frame2=cap.read()

    
    if(cv.waitKey(60)==27):
        break


cv.destroyAllWindows()