import cv2

# img = cv2.imread('Pic-4.jpg')
# imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# # Binary Thresholding
# # With Color
# retval1, threshold1 = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
#
# # With Grayscaled image
# retval2, threshold2 = cv2.threshold(imggray, 10, 255, cv2.THRESH_BINARY)
#
# # Adaptive Thresholding
# gauss = cv2.adaptiveThreshold(imggray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
#                               115, 1)
#
# # Otsu Thresholding
# retval3, otsu = cv2.threshold(imggray, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
#
# cv2.imshow('Original Image', img)
# cv2.imshow('Thresholded Image', threshold1)
# cv2.imshow('Thresholded Grayscale Image', threshold2)
# cv2.imshow('Adaptive Thresholded Image', gauss)
# cv2.imshow('Otsu Thresholded Image', otsu)

# cv2.waitKey(0)

# Using Thresholding in video
# Reading Video from WebCam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Binary Thresholding
    # With Color
    retval1, threshold1 = cv2.threshold(frame, 130, 255, cv2.THRESH_BINARY)

    # With Grayscaled image
    retval2, threshold2 = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

    # Adaptive Thresholding
    gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                  125, 1)

    # Otsu Thresholding
    retval3, otsu = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('Camera Window', frame)
    # cv2.imshow('Grayed window', gray)
    cv2.imshow('Ordinary Threshold window', threshold1)
    cv2.imshow('Grayed threshold window', threshold2)
    cv2.imshow('Adaptive Thresholding window', gauss)
    cv2.imshow('Otsu Thresholding window', otsu)



    # On keypress q shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


cv2.destroyAllWindows()
