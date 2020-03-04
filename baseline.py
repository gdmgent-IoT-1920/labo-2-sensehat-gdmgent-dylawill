# import the SenseHat library
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_rotation(180)

while True:
	# Random foreground colour (text colour)
	fg_color = (randint(0, 255), randint(0, 255), randint(0, 255))
	# Random background colour
	bg_color = (randint(0, 255), randint(0, 255), randint(0, 255))
	sense.show_message("Hello! We are New Media Development :)", text_colour=fg_color, back_colour=bg_color)
	# Wait 0.1 sec
	sleep(0.1)