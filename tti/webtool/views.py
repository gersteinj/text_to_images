from django.shortcuts import render
from django.http import HttpResponse

import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import random
# Create your views here.

def index(request):
	return HttpResponse("Hi! Try going to the image page!")

def image(request):
	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
	# create image
	image = Image.new("RGB", (400, 300), random.choice(colors	))

	# serialize to HTTP response
	response = HttpResponse(content_type='image/png')
	image.save(response, 'PNG')
	return response

def word_image(request):
	# config
	TEXT_SIZE = 75
	BG_COLOR = 'lime'
	TEXT_COLOR = 'black'
	FNT = ImageFont.truetype('SourceSansPro-Bold.ttf', int(TEXT_SIZE))
	
	# word to make an image of
	word = 'abc'

	# create placeholder image
	img = Image.new("RGB", (10, 10), 'purple')
	draw = ImageDraw.Draw(img)

	# calculate size of needed image
	w, h = draw.textsize(word, font=FNT)
	new_img = Image.new('RGB', (w, int(h * 1.2)), BG_COLOR)
	new_draw = ImageDraw.Draw(new_img)
	new_draw.text((0, 0), word, fill=TEXT_COLOR, font=FNT)


	# create and return HTTP response
	response = HttpResponse(content_type='image/png')
	new_img.save(response, 'PNG')

	return response

def selected_word(request, sent_word):
	# config
	TEXT_SIZE = 75
	BG_COLOR = 'lime'
	TEXT_COLOR = 'black'
	FNT = ImageFont.truetype('SourceSansPro-Bold.ttf', int(TEXT_SIZE))
	
	# word to make an image of
	word = sent_word

	# create placeholder image
	img = Image.new("RGB", (10, 10), 'purple')
	draw = ImageDraw.Draw(img)

	# calculate size of needed image
	w, h = draw.textsize(word, font=FNT)
	new_img = Image.new('RGB', (w, int(h * 1.2)), BG_COLOR)
	new_draw = ImageDraw.Draw(new_img)
	new_draw.text((0, 0), word, fill=TEXT_COLOR, font=FNT)


	# create and return HTTP response
	response = HttpResponse(content_type='image/png')
	new_img.save(response, 'PNG')

	return response