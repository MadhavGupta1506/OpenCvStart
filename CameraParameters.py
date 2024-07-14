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
        gray=cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
        cv.imshow("Video",gray)
        if(cv.waitKey(1) & 0xFF==ord("q")):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()