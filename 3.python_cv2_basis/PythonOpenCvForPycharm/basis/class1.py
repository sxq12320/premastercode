import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('E:\\code\\3.python_cv2_basis\\PythonOpenCvForPycharm\\picture\\cat.jpg')
# img = cv.imread('PythonOpenCvForPycharm\picture\cat.jpg')
img_gray = cv.cvtColor(img , cv.COLOR_RGB2GRAY)
cv.imshow('windows' , img_gray)
cv.waitKey(0)
cv.destroyWindow()
