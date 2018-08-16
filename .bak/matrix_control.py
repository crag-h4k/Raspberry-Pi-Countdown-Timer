#!/usr/bin/python
from PIL import Image
from PIL import ImageDraw
from time import sleep
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from sys import argv

#local modules
from timer import timer
from led_nums import PNG_4x7, PNG_8x13, PNG_8x13_ZERO_DASHED


# finds the best place to print to the matrix
def orient_image(mat_cols, mat_rows, char_width, char_height, n_chars,n_lines):	
	padding = 0	
	x_padding = char_width + padding
	y_padding = char_height + padding
	x = (mat_cols - (n_chars*x_padding))/2
	y = (mat_rows - (n_lines*y_padding))/2
	#offset for printing multiple changing chars to matrix
	arr = [x,y,x_padding]
	#print arr
	return arr

def to_matrix(minutes):
	# How fast for testing
	sleep_i = 1
	
	# matrix options set here
	options = RGBMatrixOptions()	
	options.rows = 32
	options.chain_length = 2
	options.hardware_mapping = 'adafruit-hat'
	options.parallel = 1

	# orient_image arguments here
	mat_x = options.chain_length * options.rows
	mat_y = options.rows
	char_w = 8
	char_h = 13
	num_chars = 8
	lines= 1
	O = orient_image(mat_x, mat_y, char_w ,char_h, num_chars,lines)
	
	matrix = RGBMatrix(options = options)
	image = Image.new("RGB", (64, 32))
	draw = ImageDraw.Draw(image)
	matrix.Clear()
	
	# image files found in respective directories
	png = PNG_8x13
	# create the countdown timer here
	T = timer(minutes)

	try:
# First for loop takes the initial list of lists and starts itering through
		print 'countdown timer started'
		while 1:		
			for i in T:
# Second for loop takes each individual list itme and iters through, printing to the matrix
				# this updates later according to the offset
				x_matrix_pos = O[0]
				# with a single row of chars this wont change
				y_matrix_pos = O[1]
				# this is how far away the next char will print from the previous
				x_matrix_offset = O[2]
				for j in i:
					#print "i ", i,"\nj ", j
					image = Image.open("%s" % png[j])
					image.load()
					matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
					x_matrix_pos += x_matrix_offset
				
				sleep(sleep_i)

			# display zero status at the end of the timer
			print "countdown timer finished"
			while 1:
				# last list item in timer
				zero_status = T[-1]

				x_matrix_pos = O[0]
				y_matrix_pos = O[1]
				x_matrix_offset = O[2]
				
				for i in zero_status:
					image = Image.open("%s" % png[i])
					image.load()
					matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
					x_matrix_pos += x_matrix_offset

	except Exception as e:
		matrix.Clear()
		print e

	except KeyboardInterrupt:
		matrix.Clear()
		print 'sorry to see you go'

x = int(argv[1])
to_matrix(x)
