import numpy as np
import cv2

# Functions: cv2.imread(), cv2.imshow(), cv2.imwrite()

# Load an color image in grayscale
# cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# img=cv2.imread('neelam.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('data/neelam.jpg', 0)
# img2 = cv2.imread('data/neelam.jpg', 1)
# img3 = cv2.imread('data/neelam.jpg',-1)

# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Fun With Image', cv2.WINDOW_NORMAL)
cv2.imshow('Fun With Image', img)
# cv2.imshow('image2', img2)
# cv2.imshow('image3', img3)


# Use the function cv2.imwrite() to save an image
# cv2.imwrite('data/neelam_gray.png',img)
# cv2.waitKey(0)
# k = cv2.waitKey(0)
k = cv2.waitKey(0) & 0xFF
# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()
# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite('data/neelam_gray1.png', img)
    cv2.destroyAllWindows()
# cv2.destroyAllWindows()
