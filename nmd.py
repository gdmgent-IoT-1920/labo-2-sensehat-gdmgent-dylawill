# import the SenseHat library
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

letters = ['N', 'M', 'D']

while True:
	for letter in letters:
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
		sense.show_letter(letter, text_colour=color)
		# Wait 0.5 sec between each letter
		sleep(0.5)
	# Wait 1.5 sec after the last letter
	sleep(1.5)