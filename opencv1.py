
import sys
print("Python version")
print(sys.version)

#Let's read and display an image

import cv2
img = cv2.imread('pic1.jpg')

cv2.imshow('input', img)
cv2.waitKey(1000)

#Extractiong the Height and Width
h,w = img.shape[:2]
#print(h,w)
print('Height = {}, Width = {} '.format(h,w))

cv2.destroyAllWindows()
