import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

vc = cv.VideoCapture('0.picture\VID_20231003_123113.mp4')
print(vc)
if vc.isOpened():
    open,frame = vc.read()
else:
    open = False

while(open == True):
    rat,frame = vc.read()
    if(frame is None):
        break
    if(rat == True):
        video_Gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        rat , video_Gray_Binary= cv.threshold(video_Gray,100,255,cv.THRESH_BINARY)
        video_Gray_Binary_Medianblur = cv.medianBlur(video_Gray_Binary,5)
        kernel = np.ones((3,3),np.uint8)
        video_Gray_Binary_Medianblur_Erode = cv.erode(video_Gray_Binary_Medianblur,kernel,iterations=2)
        video_Gray_Binary_Medianblur_Erode_Dialte = cv.dilate(video_Gray_Binary_Medianblur_Erode,kernel,iterations=3)
        res = video_Gray_Binary_Medianblur_Erode_Dialte
        cv.imshow('figure1',res)
        cv.waitKey(10)
        if( cv.waitKey(10) & 0XFF == ord('q')):
            break


vc.release()
cv.destroyAllWindows()
