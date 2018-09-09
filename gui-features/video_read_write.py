# Capture Video from Camera
# capture a video from the camera (I am using the in-built webcam of my laptop),
# convert it into grayscale video and display it

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('vtest.avi')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data/output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()