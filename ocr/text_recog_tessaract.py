# text recognition
import cv2
import pytesseract
# read image
im = cv2.imread('ocr/sheet.jpg')
# configurations
# config = ('-l eng --oem 1 --psm 3')
custom_config = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(im, config=custom_config))
# pytessercat
# text = pytesseract.image_to_string(im, config=config)
# print text
# text = text.split('\n')
# print(text)