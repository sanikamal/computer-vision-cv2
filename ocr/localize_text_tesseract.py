# USAGE
# python localize_text_tesseract.py --image apple_support.png
# python localize_text_tesseract.py --image apple_support.png --min-conf 50

# import the necessary packages
import numpy as np
from pytesseract import Output
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
ap.add_argument("-c", "--min-conf", type=int, default=0,
	help="mininum confidence value to filter weak text detection")
args = vars(ap.parse_args())

# sharpen = 255 - sharpen
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
# dilate = cv2.dilate(sharpen, kernel, iterations=1)
# result = 255 - dilate
# # load the input image, convert it from BGR to RGB channel ordering,
# and use Tesseract to localize each area of text in the input image
image = cv2.imread('ocr/sheet.jpg')
stretch_near = cv2.resize(image, (780, 540),interpolation = cv2.INTER_NEAREST) 
rgb = cv2.cvtColor(stretch_near, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(stretch_near, cv2.COLOR_BGR2GRAY)


ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2,3,i+1)
# 	plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# cv2.imshow("Image Thresh", thresh1)
# cv2.waitKey(0)

# kernel = np.ones((5,5),np.uint8)
# img_erosion = cv2.erode(thresh1, kernel, iterations=1) 
# cv2.imshow("Image eroson", img_erosion)
# cv2.waitKey(0)
# gray = cv2.threshold(stretch_near, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
results = pytesseract.image_to_data(thresh1,config="tessedit_char_whitelist=0123456789 -oem 2", output_type=Output.DICT)
# results=pytesseract.image_to_string(rgb,output_type=Output.DICT)
# print(results)


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
		cv2.rectangle(stretch_near, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.putText(stretch_near, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			1.2, (0, 0, 255), 3)

# show the output image
cv2.imshow("Image", stretch_near)
cv2.waitKey(0)



def getNumber(image):
    image = cv2.resize(image, (0, 0), fx=3, fy=3)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh, image_bin = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    image_final = PIL.Image.fromarray(image_bin)

    txt = pytesseract.image_to_string(
        image_final, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    return txt



def getNumber(image):

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Otsu Tresholding automatically find best threshold value
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # invert the image if the text is white and background is black
    count_white = numpy.sum(binary_image > 0)
    count_black = numpy.sum(binary_image == 0)
    if count_black > count_white:
        binary_image = 255 - binary_image

    # padding
    final_image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 255, 255))

    txt = pytesseract.image_to_string(
        final_image, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')

    return txt

