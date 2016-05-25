# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import logging
import easygui as gui
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

introMessage = '''
Welcome to Text to Images, a tool for creating magnetic poetry images.

This is still a work in progress, with more features and a better interface under development. 
The current version is Windows only. Linux is coming soon, but I'll need access to a Mac to create the OSX version. 

Please do not distribute this application yourself - it can't check for updates, so the only way to get the most updated version is to download it directly. 
A link to the current version will always be available at www.robotsinheels.com.

If you have questions or suggestions, please reach out to me at gersteinj@gmail.com or as @gersteinj on twitter.

To use Text to Images, you'll need to select a word list, a location to save your images, and a name to use for the files (the program will automatically add numbers to the end of the filename).

The default settings are black text on a white background. If you want to change that, choose yes when asked about changing settings.
Color names are standard named HTML colors. A list can be found at http://www.w3schools.com/colors/colors_names.asp
'''

# Show Directions
gui.msgbox(introMessage)

# Default settings
advancedSettings = False
textSize = 75
bgColor = 'white'
textColor = 'black'

# Other variables
prefix = 'MagneticPoetry'
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

# Use advanced settings?
advancedSettings = gui.ynbox(msg='Use advanced settings?')
logging.info('Advanced settings: %s' % advancedSettings)

# If Advanced Settings are used, pop up box to ask for font size and colors
if advancedSettings == True:
    # TODO: Set variables
    # Set text size
    textSize = gui.integerbox(msg='Set font size', default=75, lowerbound = 10, upperbound = 300)
    logging.info('Setting text size to %s' % textSize)
    # Set colors
    textColor = gui.enterbox(msg='Choose your text color using standard named HTML colors', strip=True, default='black')
    bgColor = gui.enterbox(msg='Choose your background color using standard named HTML colors', strip=True, default='white')


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
    img = Image.new("RGB", (10, 10), bgColor)

    # Draw text
    # Create a draw object
    draw = ImageDraw.Draw(img)
    # Use textsize to calculate size of text
    w, h = draw.textsize(fullLine, font=fnt)
    # Resize Image to fit text (find a way with less backtracking!)
    newImg = img.resize((w, int(h * 1.2)))
    newDraw = ImageDraw.Draw(newImg)
    newDraw.text((0, 0), fullLine, font=fnt, fill=textColor)

    # Save file
    newImg.save(os.path.join(savepath, (prefix + str(count) + '.png')))
    count += 1
