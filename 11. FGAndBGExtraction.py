import cv2

cap = cv2.VideoCapture(0)

# Creating Background Subtractor using Mixture of Gaussians
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    fgmask = fgbg.apply(frame)


    cv2.imshow('Original', frame)
    cv2.imshow('Foreground', fgmask)

    # On keypress q shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()