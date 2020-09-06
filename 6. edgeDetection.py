import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('Original', frame)

    # Edge Detection
    # Laplacian Filtering
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    cv2.imshow('Laplacian Filter', laplacian)

    # Sobel Filter
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imshow('Sobel Filter in X-direction', sobelx)
    cv2.imshow('Sobel Filter in Y-direction', sobely)

    # Canny Edge detector
    edges = cv2.Canny(frame, 150, 200)
    cv2.imshow('Canny Edge Detector', edges)



    # On keypress q shutdown
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()