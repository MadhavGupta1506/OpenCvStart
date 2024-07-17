import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img=cv.imread("images/smarties.png",0)

_,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernal=np.ones((2,5),np.uint8)

dilation=cv.dilate(mask,kernal,iterations=2)

erosion=cv.erode(mask,kernal,iterations=1)


titles=["image","mask","dilation","erosion"]
images=[img,mask,dilation,erosion]
for i in range(len(images)):
    plt.subplot(2,len(images)-2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])  
    plt.yticks([])
plt.show()