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

counting = 1

# start loop to continuously check for button presses
while True:
	sense.show_letter(str(counting), blue)
	sleep(1)
	counting = counting + 1
        
