# Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/neelam.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()