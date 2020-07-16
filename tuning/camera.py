import numpy as np
import cv2 as cv
import time

image_hsv = None   # global ;(
pixel = (20,60,80) # some stupid default

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        #you might want to adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        print(pixel, lower, upper)

        image_mask = cv.inRange(image_hsv,lower,upper)
        cv.imshow("mask",image_mask)
        return

def main():
    import sys
    global image_hsv, pixel # so we can use it in mouse callback
    cap = cv.VideoCapture(0)
    print("Choose the pixel in bg , using your mouse") 
    while True:
        ret, image_src = cap.read()
        if not ret:
            print(" Exiting ...")
            break
        cv.namedWindow('bg')
        cv.imshow("bg",image_src)
        cv.namedWindow('hsv')
        cv.setMouseCallback('bg', pick_color)
        image_hsv = cv.cvtColor(image_src,cv.COLOR_BGR2HSV)
        cv.imshow("hsv",image_hsv)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

# When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
if __name__=='__main__':
    main()
