# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Create relevant variables
prefix = 'test'
textSize = 75
count = 1
letterSize = textSize * .75

# Load strings from a list
wordList = open('wordlist.txt')
words = wordList.read()
lines = words.splitlines()

# TODO: set font size
fnt = ImageFont.truetype('LinBiolinum_Rah.ttf', int(textSize))

# Grab the next string
for line in lines:
    print(line)

    # Set size variables based on length of word
    # TODO: Can I figure out a way to do it based on the actual width of the
    # word? OMG YES TEXTSIZE

    # print(len(line))
    line = '  ' + line + '  '
    imageW = len(line) * letterSize
    imageH = letterSize * 1.5

    # create a new image
    img = Image.new("RGB", (int(imageW), int(imageH)), (200, 255, 255))

    # Draw text
    draw = ImageDraw.Draw(img)
    x, y = draw.textsize(line, font=fnt)
    draw.text(((imageW-x)/2, 0), line, font=fnt, fill='black')

    # Save file
    img.save(prefix + str(count)+'.png')
    count += 1
