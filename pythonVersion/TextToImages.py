import svgwrite

# TODO: Load strings from a list

# TODO: Grab the next string

# TODO: Set size variables based on length of word

# create an SVG file
dwg = svgwrite.Drawing('testfile.svg', (500,300), profile = 'tiny')

# Draw background
dwg.add(dwg.rect(insert = (0,0), size = ('100%', '100%'), fill = 'purple'))

# TODO: Draw text
dwg.add(dwg.text("I AM TEXT", insert = (0,100), fill = 'white', stroke = 'black'))

# Save file
dwg.save()

# TODO: Convert SVG to image file