from utilities.facedetector import FaceDetector
import cv2

# Define paths
image_path = 'images/oli_sani.jpg'
cascade_path = 'cascades/haarcascade_frontalface_default.xml'

# Load the image and convert it to greyscale
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find faces in the image
detector = FaceDetector(cascade_path)
face_boxes = detector.detect(gray, 1.2, 5)
print("{} face(s) found".format(len(face_boxes)))
# setup text
font = cv2.FONT_HERSHEY_SIMPLEX
text = "{} face(s) found".format(len(face_boxes))

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0]

# get coords based on boundary
# textX = (image.shape[1] - textsize[0]) //2
# textY = (image.shape[0] + textsize[1]) // 2
textX=0
textY=50

# add text centered on image
cv2.putText(image, text, (textX, textY ), font, 1, (0, 0, 255), 2)
# cv2.putText()

# Loop over the faces and draw a rectangle around each
for (x, y, w, h) in face_boxes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Save the detected faces
cv2.imwrite('images/count_face.png',image)
# Show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)
