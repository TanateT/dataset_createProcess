import cv2
import numpy as np

"""颜色调整 """


def callback():
    ...


cv2.namedWindow("trackbar", cv2.WINDOW_NORMAL)

# 创建trackbar
cv2.createTrackbar("R", "trackbar", 0, 255, callback)
cv2.createTrackbar("G", "trackbar", 0, 255, callback)
cv2.createTrackbar("B", "trackbar", 0, 255, callback)
img = cv2.imread(r"Sample Images/data/images\tb_100.jpg")
img_background = np.zeros_like(img)
while True:
    r = cv2.getTrackbarPos("R", "trackbar")
    g = cv2.getTrackbarPos("G", "trackbar")
    b = cv2.getTrackbarPos("B", "trackbar")
    img_background[:] = [b, g, r]
    cvt_img = cv2.addWeighted(img_background, 1, img, 0.5, 0)
    cv2.imshow("trackbar", img_background)
    cv2.imshow('demo', cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()