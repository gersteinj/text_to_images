# Setup

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logging

import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')

# Default settings
TEXT_SIZE = 75
BG_COLOR = 'lime'
TEXT_COLOR = 'black'
FNT = ImageFont.truetype('SourceSansPro-Bold.ttf', int(TEXT_SIZE))

# Word list

wordlist = """
apple
banana
cuttlefish
dog
elephant
"""

# Create word array from word list
words = wordlist.split('\n')[1:-1]

print(words)

# create a starting image
img = Image.new("RGB", (30, 30), 'purple')
draw = ImageDraw.Draw(img)

for word in words:
	logging.info("Working on {}.".format(word))
	fullLine = '  ' + word + '  '
	logging.debug(fullLine)
	w, h = draw.textsize(fullLine, font=FNT)
	logging.debug("{} x {}".format(w, h))
	new_img = Image.new("RGB", (w, int(h * 1.2)), BG_COLOR)
	new_draw = ImageDraw.Draw(new_img)
	new_draw.text((0, 0), fullLine, fill=TEXT_COLOR, font=FNT)
	new_img.save(os.path.join('saved_images', (word + '.png')))

# img.save(os.path.join('saved_images', 'sample.png'))