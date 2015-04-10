# -*- coding: utf-8 -*-

import sys
import math
from PIL import Image

pixels = ['✊🏻', '✊🏼', '✊🏽', '✊🏾', '✊🏿']
# pixels = ['👴🏻', '👴🏼', '👴🏽', '👴🏾', '👴🏿']
# pixels = ['🙏🏻', '🙏🏼', '🙏🏽', '🙏🏾', '🙏🏿']

if len(sys.argv) < 2:
	print ("ERROR: No argument for source image provided")	
else:
	# At least one argument provided, proceed	
	try:
		# Load Image
		print ("Loading image: '%s'" % sys.argv[1])
		img = Image.open(sys.argv[1])
		img = img.convert('RGB')
# 		pixels = img.load()
		width = img.size[0]
		height = img.size[1]
		
		#Prep file to write to
		outputFilePath = 'output/output.txt'
		if len(sys.argv) >= 3:
			outputFilePath = sys.argv[2]
		outputFile = open(outputFilePath, 'w')
		outputFile.truncate()
		
		for y in range(0, height):
			row = ""
			for x in range(0, width):
				# Get the value of the current pixel
				pixelRGB = img.getpixel((x,y))
				R,G,B = pixelRGB
				# !TODO - find better brightness algorithm, processing.org works better
				# Get brightness
# 				brightness = sum([R,G,B])/3
# 				#Standard
# 				brightness = (0.2126*R) + (0.7152*G) + (0.0722*B)
# 				#Percieved A
#				brightness = (0.299*R + 0.587*G + 0.114*B)
# 				#Perceived B, slower to calculate
 				brightness = math.sqrt( 0.241*(R**2) + 0.691*(G**2) + 0.068*(B**2) )
				# Covert to scale same as number of emoji in spectrum
				brightness = brightness/255*(len(pixels)-1)
				row += pixels[len(pixels)-1-int(brightness)]
			outputFile.write(row)
			outputFile.write("\n")
		
	finally:
		outputFile.close()
		print("COMPLETE: Output in: '%s'" % outputFilePath)