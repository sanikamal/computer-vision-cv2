# functions : cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText()


import numpy as np
import cv2
# Drawing Line
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(311,311),(255,0,0),15)
# Drawing Rectangle
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
# Drawing Circle
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
# Drawing Ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
# Drawing Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Adding Text to Images:
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()