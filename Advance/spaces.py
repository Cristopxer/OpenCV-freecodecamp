from cv2 import cv2 as cv
import os.path as path


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


img = cv.imread(getPath("img", "park.jpg"))
cv.imshow("Boston Park", img)


# BGR to GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Boston Park Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Boston Park HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Boston Park LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Boston Park RGB", rgb)

# HVS to BGR
hvs_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("Boston Park HSV --> BGR", hvs_bgr)


cv.waitKey(0)
