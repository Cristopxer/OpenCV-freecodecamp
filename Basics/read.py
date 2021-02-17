from cv2 import cv2 as cv
import os.path as path
# read image
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow("Cat", img)

# read video
videoPath = path.abspath(
    path.join(__file__, "../..", "Resources/Videos/dog.mp4"))
capture = cv.VideoCapture(videoPath)
while(True):
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
