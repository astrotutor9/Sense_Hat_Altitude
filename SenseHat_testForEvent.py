from sense_emu import SenseHat  # sense_hat for real hardware, sense_emu for emulator
from time import sleep

sense = SenseHat()

# set colours to use on print out on SenseHat
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# clear screen and rotate
sense.clear()

sense.show_message("Ready to go")

# start loop to continuously check for button presses
while True:
	for event in sense.stick.get_events():
		# Check if the joystick was pressed
		if event.action == "pressed":
			# Check which direction
			if event.direction == "up":
				sense.show_letter("T", green)   # Letter T for top of stairs
				sleep(0.5)
			if event.direction == "down":
				sense.show_letter("B", red)     # Letter B for bottom of stairs
				sleep(0.5)
			if event.direction == "middle":         # Middle M for joystick press
				sense.show_letter("M", blue)     # Letter B for bottom of stairs
				sleep(0.5)
			# Wait a while and then clear the screen
			sense.clear()
        
