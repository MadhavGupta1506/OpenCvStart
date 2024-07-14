import cv2 as cv
img=cv.imread("images/cat.jpg",-1)

img=cv.line(img,(100,150),(300,400),(220,70,150),thickness=5)
img=cv.arrowedLine(img,(0, 400),(250,400),(220,70,150),thickness=5)

img=cv.rectangle(img,(100,200),(200,100),(32,0,132),thickness=-1)

img=cv.circle(img,(80,80),50,(221,242,41),5)
cv.imshow("Image",img)
cv.waitKey(0)