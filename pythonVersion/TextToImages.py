import svgwrite

# Create relevant variables
imageW = 300
imageH = 300
textSize = 75
count = 1
letterSize = textSize*.75

# Load strings from a list
wordList = open('wordlist.txt')
lines = wordList.readlines()

# Grab the next string
for line in lines:
	print(line)

	# Set size variables based on length of word
	# TODO: Can I figure out a way to do it based on the actual width of the word?
	print(len(line))
	imageW = len(line) * letterSize

	# create an SVG file
	dwg = svgwrite.Drawing(str(line.rstrip())+'.svg', (imageW, imageH), profile = 'tiny')

	# Draw background
	dwg.add(dwg.rect(insert = (0,0), size = ('100%', '100%'), fill = 'purple'))

	# TODO: Draw text
	dwg.add(dwg.text(line,
		insert = (imageW/2, imageH/2 + textSize*.25	),
		text_anchor = 'middle',
		fill = 'white',
		font_size = str(textSize),
		font_family = 'Arial'
		))

	# Save file
	dwg.save()
	count += 1

# TODO: Convert SVG to image file