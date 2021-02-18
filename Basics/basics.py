from cv2 import cv2 as cv
import os.path as path


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


img = cv.imread(getPath("img", "park.jpg"))

# Converting a img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Cat", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Erode", eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resize", resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
