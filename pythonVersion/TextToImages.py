import svgwrite

# Create relevant variables
prefix = 'test'
textSize = 75
count = 1
letterSize = textSize*.75

# Load strings from a list
wordList = open('wordlist.txt')
words = wordList.read()
lines = words.splitlines()

# Grab the next string
for line in lines:
	print(line)

	# Set size variables based on length of word
	# TODO: Can I figure out a way to do it based on the actual width of the word?
	print(len(line))
	imageW = len(line) * letterSize
	imageH = letterSize * 2

	# create an SVG file
	# dwg = svgwrite.Drawing(str(line)+'.svg', (imageW, imageH), profile = 'tiny')
	dwg = svgwrite.Drawing(str(prefix)+str(count)+'.svg', (imageW, imageH), profile = 'tiny')

	# Draw background
	dwg.add(dwg.rect(insert = (0,0),
		size = ('100%', '100%'),
		stroke = 'black',
		fill = 'white'))

	# Draw text
	dwg.add(dwg.text(line,
		insert = (imageW/2, imageH/2 + textSize*.25	),
		text_anchor = 'middle',
		fill = 'black',
		font_size = str(textSize),
		font_family = 'Arial'
		))

	# Save file
	dwg.save()
	count += 1

# TODO: Convert SVG to image file