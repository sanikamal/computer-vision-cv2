from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
# The tools are returned in the recommended order of usage
tool = tools[0]

langs = tool.get_available_languages()
lang = langs[0]
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

# txt = tool.image_to_string(
#     Image.open('test.png'),
#     lang=lang,
#     builder=pyocr.builders.TextBuilder()
# )
# txt is a Python string

# word_boxes = tool.image_to_string(
#     Image.open('test.png'),
#     lang="eng",
#     builder=pyocr.builders.WordBoxBuilder()
# )
# list of box objects. For each box object:
#   box.content is the word in the box
#   box.position is its position on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

# line_and_word_boxes = tool.image_to_string(
#     Image.open('test.png'), lang="fra",
#     builder=pyocr.builders.LineBoxBuilder()
# )
# list of line objects. For each line object:
#   line.word_boxes is a list of word boxes (the individual words in the line)
#   line.content is the whole text of the line
#   line.position is the position of the whole line on the page (in pixels)
#
# Beware that some OCR tools (Tesseract for instance)
# may return empty boxes

# Digits - Only Tesseract (not 'libtesseract' yet !)
digits = tool.image_to_string(
    Image.open('ocr/sheet.jpg'),
    lang=lang,
    builder=pyocr.tesseract.DigitBuilder()
)
# digits is a python string
print(digits)