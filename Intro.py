import cv2
import os

# img = cv2.imread("Images\Videocollage1.jpg")
# print(img)
# cv2.imshow("img", img)
# cv2.waitKey(0)

# img = cv2.imread("Images\Videocollage1.jpg", 0)
# print(img)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# os.chdir("C:/Users/senit/OneDrive/Documents/Jet Learn/OpenCV With Python/Images")

# cv2.imwrite("img_black.png", img)

img = cv2.imread("Images\opencv.png")
print(img)
b, g, r = cv2.split(img)
cv2.imshow("blue", b)
cv2.waitKey(0)
cv2.imshow("green", g)
cv2.waitKey(0)
cv2.imshow("red", r)
cv2.waitKey(0)