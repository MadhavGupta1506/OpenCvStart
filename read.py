import cv2 as cv

# Reading the images
''' img=cv.imread('images/cat_large.jpg')
cv.imshow('cat',img)
cv.waitKey(0)
'''

# Reading Videos
capture=cv.VideoCapture(0)

while True:
    isTrue,Frame=capture.read()
    cv.imshow('video',Frame)
    if(cv.waitKey(1) and 0xFF==ord("d")):
        break
capture.release()
cv.destroyAllWindows()