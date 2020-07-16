import cv2
def Tracecallback(value):
    pass
def trackbars(filter_type):
    cv2.namedWindow("Trackbars", 0)
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in filter_type:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, Tracecallback)
def get_trackbar_values(filter_type):
    values = []
    for i in ["MIN", "MAX"]:
        for j in filter_type:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values

def main():
    filter_type = "HSV"
    camera = cv2.VideoCapture(0)
    trackbars(filter_type)
    while True:
        rt, image = camera.read()
        if not rt:
            break
        if filter_type == 'RGB':
            frame_to_thresh = image.copy()
        else:
            frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        v1min, v2min, v3min, v1max, v2max, v3max = get_trackbar_values(filter_type)
        thresh = cv2.inRange(frame_to_thresh, (v1min, v2min, v3min), (v1max, v2max, v3max))
        image = cv2.flip(image, 1)
        cv2.imshow("Original", image)
        thresh = cv2.flip(thresh, 1)
        cv2.imshow("FILTER", thresh)
        if cv2.waitKey(1) & 0xFF is ord('x'):
            break
if __name__ == '__main__':
    main()
