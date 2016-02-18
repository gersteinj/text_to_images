import svgwrite

# Create relevant variables
imageW = 500
imageH = 300

# TODO: Load strings from a list

# TODO: Grab the next string

# TODO: Set size variables based on length of word

# create an SVG file
dwg = svgwrite.Drawing('testfile.svg', (imageW, imageH), profile = 'tiny')

# Draw background
dwg.add(dwg.rect(insert = (0,0), size = ('100%', '100%'), fill = 'purple'))

# TODO: Draw text
dwg.add(dwg.text("I AM TEXT", insert = (imageW/2, imageH/2), text_anchor = 'middle', fill = 'white', stroke = 'black'))

# Save file
dwg.save()

# TODO: Convert SVG to image file