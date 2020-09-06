import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image=grayFrame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(
            img=frame,
            pt1=(x, y),
            pt2=(x+w, y+h),
            color=(255, 0, 0),
            thickness=2
        )
        roi_gray = grayFrame[y: y+h, x:x+w]
        roi_color = frame[y: y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(image=roi_gray, scaleFactor=1.2, minNeighbors=4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                img=roi_color,
                pt1= (ex, ey),
                pt2= (ex + ew, ey + eh),
                color=(0, 255, 0),
                thickness=2
            )

    cv2.imshow('Detected Frame', frame)

    # On keypress q shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()