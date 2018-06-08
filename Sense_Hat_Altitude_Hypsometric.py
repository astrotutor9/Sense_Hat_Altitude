from sense_hat import SenseHat  # sense_hat for real hardware, sense_emu for emulator
from time import sleep
from math import log
sense = SenseHat()

# set colours to use on print out on SenseHat
green = (0, 255, 0)
red = (255, 0, 0)

# clear screen and rotate
sense.clear()
sense.set_rotation(180)

def calculate_altitude(stairs_bottom, stairs_top):
        # calculate altitude from air pressures and temperature of 20 deg C
        alt_accurate = 44330*(1-((stairs_top/stairs_bottom)**(1/5.257)))
        #alt_accurate = ((287.05/9.80665)*(20 + 273.15))*log(stairs_bottom/stairs_top)
        print(alt_accurate)
        alt_m = round(alt_accurate, 2)
        return alt_m

sense.show_message("Ready to go")

# start loop to continuously check for button presses
while True:
        for event in sense.stick.get_events():
                # Check if the joystick was pressed
                if event.action == "pressed":
      
                        # Check which direction
                        if event.direction == "down":
                                sense.show_letter("T", green)   # Letter T for top of stairs
                                sleep(0.5)                              
                                stairs_top = sense.get_pressure()
                                sense.show_message(str(stairs_top))
                                print(stairs_top)
                                
                        if event.direction == "up":
                                sense.show_letter("B", red)     # Letter B for bottom of stairs
                                sleep(0.5)
                                stairs_bottom = sense.get_pressure()
                                sense.show_message(str(stairs_bottom))
                                print(stairs_bottom)
                                
                        if event.direction == "middle":         # Middle to calculate height
                                altitude = calculate_altitude(stairs_bottom, stairs_top)

                                sense.show_message(str(altitude) + " metres")
                                print(str(altitude) + " metres")
                                
      
                        # Wait a while and then clear the screen
                        sleep(0.5)
                        sense.clear()
			
			
