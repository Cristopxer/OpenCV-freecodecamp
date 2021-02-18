from cv2 import cv2 as cv
import os.path as path
import numpy as np


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


img = cv.imread(getPath("img", "Cats.jpg"))
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Cats gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(blur, 125, 175)

# cv.imshow("Cats canny", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours", blank)


cv.waitKey(0)
