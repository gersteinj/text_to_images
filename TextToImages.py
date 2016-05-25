# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logging
import easygui as gui
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

# Show Directions
gui.msgbox('Choose a list of words and a save location')

# Create relevant variables
# Setting these as variables will help when I add a GUI
prefix = 'MagneticPoetry'
textSize = 75
count = 1

# Get file location
filename = gui.fileopenbox(msg='Pick your word list', title='File selection')
logging.info('Your word list is %s' % filename)

# Get save location
savepath = gui.diropenbox(title='Choose save location')
logging.info('Save files in %s' % savepath)

# Choose base file name
prefix = gui.enterbox(msg='Choose a prefix for your file names', default='MagneticPoetry')
logging.info('Saving files as %s with numerical suffixes' % prefix)

# Load strings from a list
wordList = open(filename)
words = wordList.read()
lines = words.splitlines()

# Set font size
fnt = ImageFont.truetype('LinBiolinum_Rah.ttf', int(textSize))

# Grab the next string
for line in lines:
    logging.info('Next line is %s' % line)

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
    newImg.save(os.path.join(savepath, (prefix + str(count) + '.png')))
    count += 1
