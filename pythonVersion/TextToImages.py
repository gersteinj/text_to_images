# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

# Create relevant variables
# Setting these as variables will help when I add a GUI
prefix = 'test'
textSize = 75
count = 1

# Load strings from a list
wordList = open('wordlist.txt')
words = wordList.read()
lines = words.splitlines()

# Set font size
fnt = ImageFont.truetype('LinBiolinum_Rah.ttf', int(textSize))

# Grab the next string
for line in lines:
    logging.debug(line)

    # print(len(line))
    fullLine = '  ' + line + '  '
    logging.debug(fullLine)

    # create a new image
    img = Image.new("RGB", (10, 10), (255, 255, 255))

    # Draw text
    # Create a draw object
    draw = ImageDraw.Draw(img)
    # Use textsize to calculate size of text
    w, h = draw.textsize(fullLine, font=fnt)
    # Resize Image to fit text (find a way with less backtracking!)
    newImg = img.resize((w, int(h * 1.2)))
    newDraw = ImageDraw.Draw(newImg)
    newDraw.text((0, 0), fullLine, font=fnt, fill='black')

    # Save file
    newImg.save(prefix + str(count) + '.png')
    count += 1
