from cv2 import cv2 as cv
import os.path as path


def getPath(typeFile, file):
    folder = "Photos" if typeFile == 'img' else "Videos"
    return path.abspath(path.join(__file__, "../..",
                                  "Resources/"+folder, file))


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# read video
capture = cv.VideoCapture(getPath("", "Dog.mp4"))
while(True):
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("VideoResize", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
