from cv2 import cv2 as cv
import os.path as path
import numpy as np


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


img = cv.imread(getPath("img", "park.jpg"))
cv.imshow("Boston Park", img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("b", blue)
cv.imshow("g", green)
cv.imshow("r", red)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)


cv.waitKey(0)
