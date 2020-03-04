# import the SenseHat library
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(180)

# Colors
R = [255, 0, 0] # Red
S = [255, 200, 75] # Skin
B = [0, 110, 255] # Blue
W = [50, 50, 50] # White

# Mario normal state
mario = [
W, W, W, W, W, W, W, W,
W, W, W, R, R, W, W, W,
W, W, W, S, S, W, W, W,
W, W, R, B, B, R, W, W,
W, S, W, B, B, W, S, W,
W, W, W, B, B, W, W, W,
W, W, B, W, W, B, W, W,
W, W, S, W, W, S, W, W
]

# Mario jump state
mario_jump = [
W, W, W, R, R, W, W, W,
W, W, W, S, S, W, S, W,
W, W, R, B, B, R, W, W,
W, S, W, B, B, W, W, W,
W, W, W, B, B, W, W, W,
W, W, B, W, W, B, W, W,
W, W, S, W, W, S, W, W,
W, W, W, W, W, W, W, W
]

sense.set_pixels(mario)

while(True):
	event = sense.stick.wait_for_event()
	if (event.direction == 'up'):
		# Update the LED matrix
		sense.set_pixels(mario_jump)
		# Wait 0.5 sec
		sleep(0.5)
		# Return to the previous mario
		sense.set_pixels(mario)
