''' filename : display_image.py

Description : This sample demonstrates how to read an image, display it on the window and print image size.
Level : Beginner

Benefits : Learn to load image and display it in window

Usage : python display_image.py <image_file> 

Written by : Sani Kamal '''

import cv2
import sys
import numpy as np

print(cv2.__file__)

if len(sys.arg)!=2:                  ## Check for error in usage syntax
    print( "Usage : python display_image.py <image_file>")

else:
    img = cv2.imread(sys.argv[1],cv2.IMREAD_COLOR)  ## Read image file

    if (img == None):                      ## Check for invalid input
        print("Could not open or find the image")
    else:
        cv2.namedWindow('Display Window')        ## create window for display
        cv2.imshow('Display Window',img)         ## Show image in the window
        print("size of image: ",img.shape)       ## print size of image
        cv2.waitKey(0)                           ## Wait for keystroke
        cv2.destroyAllWindows()                  ## Destroy all windows
