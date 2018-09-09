import numpy as np
import cv2

pic=np.zeros((500,500,3),dtype='uint8')
# drawing a rectangle
cv2.rectangle(pic,(0,0),(500,150),(234,65,231),3,lineType=8,shift=0)
# drawing a line
cv2.line(pic,(50,50),(500,350),(231,12,78))
# drawing a circle
cv2.circle(pic,(250,250),30,(255,255,0))
# writing text
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,"Rua Tech",(10,100),font,3,(255,255,255),4,cv2.LINE_8)
cv2.imshow("text",pic)
cv2.imwrite('text.png',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()