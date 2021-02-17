from cv2 import cv2 as cv
import os.path as path
import numpy as np


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

# Paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Green', blank)

# draw a rectangle
# cv.rectangle(blank, (0, 0),
#              (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
# cv.imshow('Rectangle', blank)

# draw a circle
# cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# draw a line
# cv.line(blank, (0, 0), (blank.shape[1]//2,
#                         blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# draw text
cv.putText(blank, 'Hello bitches', (225, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
