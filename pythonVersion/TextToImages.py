import svgwrite

# Create relevant variables
imageW = 500
imageH = 300
textSize = 75
count = 1

# Load strings from a list
wordList = open('wordlist.txt')
lines = wordList.readlines()

# Grab the next string
for line in lines:
	print(line)

	# TODO: Set size variables based on length of word

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