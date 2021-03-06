import cv2
import numpy as np

# Corner Detection
img = cv2.imread('Pic-10.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(
    image=gray,
    maxCorners=100,
    qualityLevel=0.2,
    minDistance=10
)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corners', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
