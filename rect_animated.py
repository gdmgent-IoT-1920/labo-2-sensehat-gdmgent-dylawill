# import the SenseHat library
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

while True:
	# Border (random color)
	X = (randint(0, 255), randint(0, 255), randint(0, 255))
	# No fill
	O = [0, 0, 0] # Black

	# 4 rectangles of different sizes
	rect1 = [
		X, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
	]
	rect2 = [
		X, X, X, X, O, O, O, O,
		X, O, O, X, O, O, O, O,
		X, O, O, X, O, O, O, O,
		X, X, X, X, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
	]
	rect3 = [
		X, X, X, X, X, X, O, O,
		X, O, O, O, O, X, O, O,
		X, O, O, O, O, X, O, O,
		X, O, O, O, O, X, O, O,
		X, O, O, O, O, X, O, O,
		X, X, X, X, X, X, O, O,
		O, O, O, O, O, O, O, O,
		O, O, O, O, O, O, O, O,
	]
	rect4 = [
		X, X, X, X, X, X, X, X,
		X, O, O, O, O, O, O, X,
		X, O, O, O, O, O, O, X,
		X, O, O, O, O, O, O, X,
		X, O, O, O, O, O, O, X,
		X, O, O, O, O, O, O, X,
		X, O, O, O, O, O, O, X,
		X, X, X, X, X, X, X, X,
	]

	# Let the rectangle grow and shrink
	sense.set_pixels(rect1)
	sleep(0.5)
	sense.set_pixels(rect2)
	sleep(0.5)
	sense.set_pixels(rect3)
	sleep(0.5)
	sense.set_pixels(rect4)
	sleep(0.5)
	sense.set_pixels(rect3)
	sleep(0.5)
	sense.set_pixels(rect2)
	sleep(0.5)
