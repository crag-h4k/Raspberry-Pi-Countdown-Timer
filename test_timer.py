#! /usr/bin/env python
from time import sleep
from os import system
from sys import getsizeof
def make_num(x):
	arr = []
	for i in range(x):
		if i<10:
			y = '0'+str(i)
			arr.append(y)
		else:
			y = str(i)
			arr.append(y)
	arr.reverse()
	return arr

def less_than_ten(x):
	if x < 10:
		return True
	else:
		return False

def to_seconds(mins):
	return round(60+((mins - round(mins,0))*60))%60

def test_timer(*mins):
	if not mins:
		mins = 15
	hundreth = make_num(100)
	seconds = make_num(60)
	minutes = make_num(mins)

	_timer = []
	for i in range(len(minutes)):
		_minute = minutes[i]
		for j in range(len(seconds)):
			_second = seconds[j]
			for k in range(len(hundreth)):
				_hundreth = hundreth[k]
				countdown = _minute + ':' + _second + '.' + _hundreth
				_timer.append(countdown)
	#for i in _timer:
	#	print(i)
	#	sleep(.001)
	return _timer

def timer(minutes):
	arr = []
	seconds = minutes * 60
	colon_index = 10	
	for i in range(seconds):
		_min = (seconds - i)/60
		
		remaining_min = int(_min)
		remaining_sec = int(to_seconds(_min)-i)%60
# The if else statements below take the current countdown time and format it as <xx:xx>. 
# This function returns a list of lists with countdown sublist properly mapped to the png list in matrix_control.py

		if less_than_ten(remaining_min) == True and less_than_ten(remaining_sec) == True:
			countdown = '0'+str(remaining_min)+':0'+str(remaining_sec)
			x = '0'+str(remaining_min)+'0'+str(remaining_sec)
			digits = [int(i) for i in x]

		elif less_than_ten(remaining_min) == True and less_than_ten(remaining_sec)== False:
			countdown = '0'+str(remaining_min)+':'+str(remaining_sec)
			x = '0'+str(remaining_min)+str(remaining_sec)
			digits = [int(i) for i in x]

		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec) == True:
			countdown = str(remaining_min)+':0'+str(remaining_sec)	
			x = str(remaining_min)+'0'+str(remaining_sec)	
			digits = [int(i) for i in x]

		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec) == False:
			countdown = str(remaining_min)+':'+str(remaining_sec)
			x = str(remaining_min)+str(remaining_sec)
			digits = [int(i) for i in x]
		
		digits.insert(2,colon_index)
		arr.append(digits)
		digits = []
	arr.append([0,0,colon_index,0,0])
	return arr

def get_current(minutes):
	arr = timer(minutes)
	print arr[-1]		
	return arr[-1]	

def map_to_png(timer_arr, png_arr):
	return

#timer(1)
#timer(15)
#get_current(15)
test_timer()
