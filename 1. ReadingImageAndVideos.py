import matplotlib.pyplot as plt
import cv2

# Reading Image
img = cv2.imread('test1.jfif', cv2.IMREAD_GRAYSCALE)

# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap= 'gray', interpolation='bicubic')
plt.plot([50,100], [9,27], 'c', linewidth=2)
plt.show()

# Reading Video from WebCam
cap = cv2.VideoCapture(0)
# Writing to a file from WebCam
fourcc = cv2.VideoWriter_fourcc(*'XVID') # This is the codec to save the video in.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('Camera Window', frame)
    cv2.imshow('Grayed window', gray)

    # On keypress q shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()