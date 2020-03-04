# import the SenseHat library
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Number of rows
R = 7
# Number of columns
C = 7

is_cleared = True

# Get random colors
def get_random_color():
	random_red = randint(0, 255)
	random_green = randint(0, 255)
	random_blue = randint(0, 255)
	return (random_red, random_green, random_blue)

# Loop through all LEDS
while True:
	# Starting positions
	x_pos = 0
	y_pos = 0

	while (y_pos <= R):
		# Clear previous pixel
		if is_cleared:
			sense.clear()

		sense.set_pixel(x_pos, y_pos, get_random_color())

		# Wait 0.1 sec to move on to the next pixel
		sleep(0.1)

		# Change position
		x_pos = (x_pos + 1) if (x_pos + 1 <= C) else (0)
		y_pos = (y_pos + 1) if (x_pos + 1 == C + 1) else (y_pos)

		# Wait 0.2 sec to go to the next pixel
		sleep(0.2)