import cv2 as cv

cap=cv.VideoCapture(0)

while(cap.isOpened()):
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow("Video",gray)
    if(cv.waitKey(1) & 0xFF==27):
        break
cap.release()
cv.destroyAllWindows()