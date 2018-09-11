#https://pypi.org/project/pytesseract/
#simple script that uses pytesseract to read the text in an image as arguments
#Gregory Ivo

import sys
from PIL import Image
import pytesseract
# Simple image to string

######THIS WORKS PERFECTLY!
print(pytesseract.image_to_string(Image.open(sys.argv[1]), config='-psm 6'))
