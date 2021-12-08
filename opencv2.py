# Operations with Image

import cv2
import sys

img = cv2.imread(cv2.samples.findFile('pic2.jpg'))     #default imread

if img is None:
    sys.exit("Could not read the image")

cv2.imshow('Default flag', img)
cv2.waitKey((5000))

'''
cv2.imread(filename, flages)
Here, Filename = 'path/to /the / file'
flages = cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED

IMREAD_COLOR: Default parameter, can pass 1 for this flag,loads image in BGR 8-bit format, 
IMREAD_GRAYSCALE: loads image in Grayscale mode, can pass 0 for this flag
IMREAD_UNCHANGED: loads image as is including alpha channel present if any, can pass -1 

'''

img2 = cv2.imread('pic2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale img', img2)
cv2.waitKey(5000)

img3 = cv2.imread('pic2.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('Unchanged, with alpha if any', img3)
cv2.waitKey(5000)

#We can keep the single waitKey() at last, to show the outputs at a time
