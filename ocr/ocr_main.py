import numpy as np
from pytesseract import Output
import pytesseract
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--min-conf", type=int, default=0,
	help="mininum confidence value to filter weak text detection")
args = vars(ap.parse_args())
img = cv2.imread('ocr/sheet.jpg')
# stretch_near = cv2.resize(img, (900, 600),interpolation = cv2.INTER_NEAREST) 
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# inverted_thresh = 255 - thresh
# cv2.imshow('result', thresh)
# cv2.waitKey(0)
# kernel = np.ones((5,5),np.uint8)
# img_erosion = cv2.erode(thresh1, kernel, iterations=1) 
results = pytesseract.image_to_data(thresh,output_type=Output.DICT)
# print(txt)
# loop over each of the individual text localizations
for i in range(0, len(results["text"])):
	# extract the bounding box coordinates of the text region from
	# the current result
	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]

	# extract the OCR text itself along with the confidence of the
	# text localization
	text = results["text"][i]
	conf = int(results["conf"][i])

	# filter out weak confidence text localizations
	if conf > args["min_conf"]:
		# display the confidence and text to our terminal
		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")

		# strip out non-ASCII text so we can draw the text on the image
		# using OpenCV, then draw a bounding box around the text along
		# with the text itself
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(thresh, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			1.2, (0, 0, 255), 3)

cv2.imshow('result', thresh)
cv2.waitKey(0)
