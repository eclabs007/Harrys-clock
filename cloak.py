####
###https://ineclabs.com
###maintainer 
###
import cv2
import numpy as np
import time
import copy

print("""
Would you like to try my invisibility cloak ??
Cover a Red Cloth over you to make yourself invisible!!!!
       
    """)


cap = cv2.VideoCapture(0)
time.sleep(3)
background=0
for i in range(30):
    ret,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    img2 = img.copy()
    img = np.flip(img,axis=1)
    img2 = np.flip(img2,axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value,0)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    #lower_blue = np.array([ 80, 130, 150]) 
   # upper_blue = np.array([120, 170, 230])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    mask3 = cv2.inRange(blurred,lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask4 = cv2.inRange(blurred,lower_red,upper_red)
    mask5=mask3+mask4
    mask = mask1+mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    mask5 = cv2.morphologyEx(mask5, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    #HSV+ mask
    img[np.where(mask==255)] = background[np.where(mask==255)]
    #Blurred + Mask
    img2[np.where(mask5==255)] = background[np.where(mask5==255)]
    #final = cv2.hconcat((img2,hsv))
    #final = cv2.hconcat((img,final))
    img2 = cv2.resize(img2, (960, 720))   
    cv2.imshow('Display',img2)
    k = cv2.waitKey(10)
    if k == 27:
        break
