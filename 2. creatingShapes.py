import cv2
import numpy as np

img = cv2.imread('Test1.jfif', cv2.IMREAD_COLOR)

# Putting a line in the image
cv2.line(img, (0,0), (150,150), (0,0,0), 5)

# Putting a rectangle in the image
cv2.rectangle(img, (10,20), (400,200), (0,0,0), 1)

# Putting a circle in the image
cv2.circle(img, (200,100), 50, (255,0,0), 4)

# Putting a polygon in the image
pts = np.array([[25,35], [70,45], [120,140], [400, 200]

cv2.imshow('Altered Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()