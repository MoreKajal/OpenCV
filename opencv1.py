
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
print("The shape of an image is -->", img.shape)
#print(h,w)
print('Height = {}, Width = {} '.format(h,w))

#RGB to Gray
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_scale', gry_img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

#Extract RGB values of an image
#Choose a random pixel to extract values
(B, G, R) = img[150, 150]    #pixel value must be between h & w
print((B,G,R))