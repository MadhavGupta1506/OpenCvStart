import cv2 as cv

def rescaleFrame(frame,scale=.5):
    width=int(frame.shape[1]*scale)  
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading the images
# img=cv.imread('images/cat_large.jpg')

# resizedImage=rescaleFrame(img)

# cv.imshow('cat',resizedImage)
# cv.waitKey(0)


# Reading Videos
capture=cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue,frame=capture.read()
    
    frameResized=rescaleFrame(frame)
    cv.imshow('video',frameResized)
    if(cv.waitKey(25) and 0xFF==ord("d")):
        break
capture.release()
cv.destroyAllWindows()
