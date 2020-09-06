import cv2
import matplotlib.pyplot as plt

# Matching 2 Images better than simple template matching
template = cv2.imread('Pic-11.png')
img = cv2.imread('Pic-12.png')

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(img, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key= lambda x:x.distance)

fImg = cv2.drawMatches(template, kp1, img, kp2, matches[:10], None, flags=2)

plt.imshow(fImg)
plt.show()
