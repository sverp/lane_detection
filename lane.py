import cv2
import numpy as np

img = cv2.imread('image/1.jpg')
cv2.imshow('lane',img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('grayscaled image',gray_img)

#gauss_img = cv2.GaussianBlur(gray_img,(5,5),0)
#cv2.imshow('gauss',gauss_img)

canny_img = cv2.Canny(gray_img,100,200)
cv2.imshow('cannyimg',canny_img)
cv2.waitKey(0)





