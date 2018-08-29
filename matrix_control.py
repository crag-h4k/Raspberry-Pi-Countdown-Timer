#!/usr/bin/python
from datetime import datetime
from sys import argv
from time import sleep

from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions
#local modules
from timer import timer, test_timer
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

def to_matrix(_minutes):
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
	
# First for loop takes the initial list of lists and starts itering through
	#print(T)
        #timer_flag = True
	while True:		
	    T = test_timer(_minutes)
	    for i in T:
                #print('here')
# Second for loop takes each individual list itme and iters through, printing to the matrix
                #print(i)
                # this updates later according to the offset
                x_matrix_pos = O[0]
                # with a single row of chars this wont change
                y_matrix_pos = O[1]
                # this is how far away the next char will print from the previous
                x_matrix_offset = O[2]
                #print(i)
                minutes = (i[0],i[1])
                seconds = (i[2],i[3])
                hundreths = (i[4],i[5])
                
                for i in minutes:
                    #sleep(.01)
                        #x_matrix_pos = x_matrix_offset
                    image = Image.open("%s" % png[int(minutes[0])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
                    
                    x_matrix_pos += x_matrix_offset
                    #print x_matrix_pos
                    image = Image.open("%s" % png[int(minutes[1])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)

                    #colon
                    x_matrix_pos += x_matrix_offset
                    image = Image.open("%s" % png[10])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
                    #for secs in seconds:

                    x_matrix_pos += x_matrix_offset
                    image = Image.open("%s" % png[int(seconds[0])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)

                    x_matrix_pos += x_matrix_offset
                    #image = Image.open("%s" % png[int(seconds[1])])
                    image = Image.open("%s" % png[int(seconds[1])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
                    #period
                    x_matrix_pos += x_matrix_offset
                    image = Image.open("./8x13/period.png")
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
                    #for hunds in hundreths:

                    x_matrix_pos += x_matrix_offset
                    image = Image.open("%s" % png[int(hundreths[0])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)

                    x_matrix_pos += x_matrix_offset
                    image = Image.open("%s" % png[int(hundreths[1])])
                    image.load()
                    matrix.SetImage(image.convert('RGB'),x_matrix_pos, y_matrix_pos)
                    #print(minutes[0],minutes[1],seconds[0],seconds[1],hundreths[0],hundreths[1])
                    sleep(.0001693405867)
	        #timer_flag == False
            print(datetime.now())
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

	#except Exception as e:
	#	matrix.Clear()
	#	print e

	#except KeyboardInterrupt:
	#	matrix.Clear()
	#	print 'sorry to see you go'
def validate_input(*args):
	try:
		args = int(argv[1])
		return(args)
	except:
		return 15

x = validate_input()
#15:00 min timer finished 00:58 early
#05:00 min timer finished 00:49 early
#05:00 min timer finished 00:35 early
#05:00 min timer finished 00:33 early
print(datetime.now())
to_matrix(x)

