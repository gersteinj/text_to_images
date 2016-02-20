import svgwrite
import PIL
from PIL import Image
from PIL import ImageDraw
print('svg')
print('pillow')

# Create relevant variables
prefix = 'test'
textSize = 75
count = 1
letterSize = textSize * .75

# Load strings from a list
wordList = open('wordlist.txt')
words = wordList.read()
lines = words.splitlines()

# Grab the next string
for line in lines:
    print(line)

    # Set size variables based on length of word
    # TODO: Can I figure out a way to do it based on the actual width of the
    # word?
    print(len(line))
    imageW = len(line) * letterSize
    imageH = letterSize * 2

    # create a new image
    img = Image.new("RGB", (int(imageW), int(imageH)), (200, 50, 255))

    # TODO: set font size

    # Draw text
    draw = ImageDraw.Draw(img)
    draw.text((0, imageH/2), line, fill='white')

    # Save file
    img.save(str(count)+'.png')
    count += 1
