import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # HSV - Hue Saturation Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color Filtering in Video

    # For a Light Bluish Color
    lower_blue = np.array([70, 160, 70])
    upper_blue = np.array([140, 250, 180])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #
    # # Average filtering for noise reduction
    # kernel = np.ones((15,15), np.float32)/225
    # smoothed = cv2.filter2D(res, -1, kernel)
    #
    # # Gaussian Filter For better blur
    # blur = cv2.GaussianBlur(res, (15,15), 0)
    #
    # # Median Blur - better pepper noise reduction
    # medBlur = cv2.medianBlur(res, 15)
    #
    # # bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    #
    # cv2.imshow('Frame', frame)
    # # cv2.imshow('Mask', mask)
    # cv2.imshow('Result', res)
    # # cv2.imshow('Smoothed', smoothed)
    # cv2.imshow('Blur', blur)
    # cv2.imshow('Median Blur', medBlur)

    # Morphological Transformations

    kernel = np.ones((5, 5), np.uint8)

    # Erosion
    erosion = cv2.erode(mask, kernel, iterations=1)

    # Dilation
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Opening
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Closing
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('Result', res)
    # cv2.imshow('Erosion', erosion)
    # cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    # On keypress q shutdown
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()