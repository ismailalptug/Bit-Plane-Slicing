import cv2
import numpy as np

def  bitplaneslicing(img,bit):
    out = []
    create = np.full((img.shape[0], img.shape[1]), 2 ** bit, np.uint8)
    bit_op = cv2.bitwise_and(create, img)
    multip = bit_op * 255

    out.append(multip)
    out_son = np.hstack(out)
    cv2.imshow("bit plane", out_son)
    cv2.waitKey(0)
    cv2.destroyAllWindows()