# import the necessary packages
import numpy as np
import argparse
import imutils#for opencv functions
import cv2
from os.path import dirname, join

image1 = cv2.imread("images/group_1.jpg")
cv2.imshow("imutils", imutils.resize(image1, 500, 500))
cv2.imshow("cv2", cv2.resize(image1, (300, 300)))
# cv2.imshow("Output1c", image1)
# image2 = cv2.imread("images/group_2.jpg")
# cv2.imshow("Output2", imutils.resize(image2, 500, 500))
# image3 = cv2.imread("images/group_3.jpg")
# cv2.imshow("Output3", imutils.resize(image3, 500, 500))
# image4 = cv2.imread("images/messi.jpeg")
# cv2.imshow("Output4", imutils.resize(image4, 500, 500))
cv2.waitKey(0)