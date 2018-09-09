import numpy as np
import cv2

# Accessing and Modifying pixel values

img=cv2.imread('me_friends_teacher.jpg')
px = img[100,100]
print(px)
# accessing only blue pixel
blue = img[100,100,0]
img[100,100] = [255,255,255]
print(img[100,100])

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

# Accessing Image Properties

# Image properties include number of rows, columns and channels, type of image data,
#  number of pixels etc.

print(img.shape)

# Total number of pixels is accessed by img.size:
print(img.size)

# Image datatype is obtained by img.dtype:

print(img.dtype)


# region of images
reg = img[280:340, 330:390]
img[273:333, 100:160] = reg
# cv2.imshow("Image",img)

# Splitting and Merging Image Channels

b,g,r = cv2.split(img)
print(b)
img = cv2.merge((b,g,r))
# OR
# blue
b = img[:,:,0]

# all the green pixels to zero
img[:,:,1] = 0
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()