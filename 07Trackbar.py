import cv2


def callback():
    pass


cv2.namedWindow('color', cv2.WINDOW_NORMAL)
img = cv2.imread("lenna.png")
color_spaces = [cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2HLS_FULL, cv2.COLOR_BGR2HSV,
                cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2Lab, cv2.COLOR_BGR2LAB, cv2.COLOR_BGR2Luv, cv2.COLOR_BGR2LUV,
                cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2XYZ, cv2.COLOR_BGR2YCrCb, cv2.COLOR_BGR2YCR_CB,
                cv2.COLOR_BGR2YUV]
cv2.createTrackbar('cur_color', 'color', 0, len(color_spaces) - 1, callback)
while True:
    index = cv2.getTrackbarPos('cur_color', 'color')
    print(color_spaces[index])
    cvt_img = cv2.cvtColor(img, color_spaces[index])

    if index == 0:
        cv2.imshow('color', img)
    else:
        cv2.imshow("color", cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
