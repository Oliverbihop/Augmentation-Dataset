import cv2
import numpy as np 
import argparse
import glob

img1 = cv2.imread("data_aug/aug0_0.jpg")
x,y,w,h = 59,	36	,74,	58
cv2.rectangle(img1, (x, y), (w, h), (255, 255, 0), 2)
cv2.imshow("a",img1)
cv2.waitKey(0)