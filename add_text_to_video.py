import cv2 as cv
cap=cv.VideoCapture(0)

'''
We can use 3 instead of cv.CAP_PROP_FRAME_WIDTH 
We can use 4 instead of cv.CAP_PROP_FRAME_HEIGHT

'''

cap.set(4,900) 
cap.set(3,3000) 


while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        frame=cv.putText(frame,"HELLO",(80,280),cv.FONT_HERSHEY_TRIPLEX,5,(0,252,121),5,cv.LINE_AA)
        cv.imshow("Video",frame)
        if(cv.waitKey(20) & 0xFF==ord("q")):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()