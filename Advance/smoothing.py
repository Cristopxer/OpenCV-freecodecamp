from cv2 import cv2 as cv
import os.path as path


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


img = cv.imread(getPath("img", "cats.jpg"))
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Cats_average", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian blur", gauss)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow("Cats_median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow("Cats_Bilateral", bilateral)


cv.waitKey(0)
