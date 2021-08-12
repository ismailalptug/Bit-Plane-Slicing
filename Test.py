import cv2
from BP_Slicing import bitplaneslicing

inimg = cv2.imread('F14.TIF', 0)
cv2.imshow("Original",inimg)
bitplaneslicing(inimg, 3)