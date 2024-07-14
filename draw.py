import cv2 as cv
import numpy as np

# blank=np.zeros((500,500,3),dtype="uint8")
# cv.imshow("blank",blank)

# 1. Painting the blank image
# blank[200:300,300:400]=0,0,255
# cv.imshow("green",blank)


# 2. Draw a rectangle

# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED) # We use thickness=cv.FILLED or thickness=-1 to fill the entire rectangle.  

# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=-1)
# cv.imshow("rectangle",blank)


# # 3. Draw a Circle
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1)
# cv.imshow("Circle",blank)


# # 4. Draw a Line
# cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=4)
# cv.imshow("Line",blank)

# 5. Write a Text
cv.putText(blank,"Hello,This is Madhav's Pc",(0,255),cv.FONT_HERSHEY_TRIPLEX, 1.0,(55,15,177),2)
cv.imshow("Text",blank)


cv.waitKey(0) 