import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

def CvImshow(a , b):
    cv.imshow(a,b)
    cv.waitKey(0)
    cv.destroyAllWindows()

kernel = np.ones((3,3),np.uint8)
ImgCat = cv.imread('0.picture\cat.jpg')
ImgCat = cv.medianBlur(ImgCat,3)
ImgCat = cv.cvtColor(ImgCat,cv.COLOR_BGR2GRAY)
rat, ImgCat = cv.threshold(ImgCat,140,255,cv.THRESH_BINARY)
ImgCat = cv.dilate(ImgCat , kernel , iterations =2)
ImgCat = cv.erode(ImgCat , kernel , iterations=2)
ImgCat = cv.GaussianBlur(ImgCat,(3,3),1)
# CvImshow('cat',ImgCat)


vc = cv.VideoCapture('0.picture\VID_20231003_123113.mp4')
if vc.isOpened():
    open,frame = vc.read()
else:
    open = False


plt.ion()
fig1 = plt.figure('orginal picture')

while(open == True):
    rat,frame = vc.read()

    if(frame is None):
        break
    if(rat == True):

        kernel = np.ones((3,3),np.uint8)
        ImgCat = cv.medianBlur(frame,3)
        ImgCat = cv.cvtColor(ImgCat,cv.COLOR_BGR2GRAY)
        rat, ImgCat = cv.threshold(ImgCat,140,255,cv.THRESH_BINARY)
        ImgCat = cv.dilate(ImgCat , kernel , iterations =2)
        ImgCat = cv.erode(ImgCat , kernel , iterations=2)
        ImgCat = cv.GaussianBlur(ImgCat,(3,3),1)

        ax1 = fig1.add_subplot(1,2,1)
        ax1.axis('off')
        ax1.imshow(frame , cmap='gray')
        
        ax2 = fig1.add_subplot(1,2,2)
        ax2.axis('off')
        ax2.imshow(ImgCat,cmap='gray')

        plt.pause(2)
        fig1.clf()


vc.release()
cv.destroyAllWindows()
