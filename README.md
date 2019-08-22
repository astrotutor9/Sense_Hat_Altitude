# Altitude Calculator using a SenseHat
This project has been initially written for a Abseiling day, updated for
a camera tethered to a kite and now is to be used in a school to demonstrate
coding in a science club.

# Altimeter with a Raspberry Pi & SenseHat

We live at the bottom of a sea of air. And just like the oceans of water where the pressure at the sea bed is far greater than that at the surface. The air pressure at sea level is greater than that on a mountain top. By measuring the air pressure it is possible to calculate your altitude above, or below, sea level. Or by measuring it at two levels calculate the difference in height. Which is the aim of this worksheet.

In this exercise you will be utilising the SenseHat board for the Raspberry Pi. Developed for use on the International Space Station it is also freely available. On the board is a matrix of 64 RGB LED. Each LED consists of three separate red, green and blue LED. By varying the brightness of each a multitude of different colours can be produced. 

Also on the board are various sensors for movement, temperature, humidity and air pressure. And also a joystick that can be used as an input device.

This exercise will create a simple interface using the LED and the joystick so that the Raspberry Pi can be used headless (without a keyboard, mouse or screen). The screen shall also be used to display the values calculated for the altitude.

### Items Needed
Raspberry Pi
SenseHat
Android Mobile Phone Powerbank

## The Code

The exercise will start with the basics and build up. It uses the built in SenseHat emulator within the Raspberry Pi.

One of the sensors on the SenseHat is to measure air pressure. It is remarkably sensitive, just a gentle blow on the board will register a change. There is a formula called the Hypsometric Formula from which a change in altitude can be calculated by comparing the change in air pressure. It is utilised in aircraft to determine the aircraft’s altitude above the ground but today you will be measuring your altitude as you climb some stairs.

But first you need to get the sensor working.

Open up Thonny Python IDE and a New File. Save it in the Documents folder as sensealtitude.py.

The first lines of code are:
```
from sense_emu import SenseHat
from time import sleep
```
These import into the program pre written information that the program calls upon to be utilised. As you can probably tell the first is about the board itself, the other is about time. The time commands enable us to pause the code a bit in places.
```
sense = SenseHat()
sense.clear()
```
This line sets up the sense hat. Every time the code states ‘sense’ the instruction is called from the senseHat library imported at the top. The next line clears the LED should any be lit up.
```
# Write a message.
sense.show_message("Welcome to the SenseHat")
```
These lines include some comments. These are marked with the hash # at the beginning. Comments are ignored in the program but are useful for us to read the code and remember what it is supposed to be doing.
The next line will scroll a message across the LED. Change the text to make your own message if you like.

Save the code (Ctrl + S) and run the script by clicking the arrow. The message should scroll across the SenseHat Emulator that opens up.

## Moving On

The final code will use a loop to continually check if the joystick has been used. This next code demonstrates how this loop works. This will be with a simple counting code. Alter your code so that it now reads like this:
```
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

counting = 1

# start loop to count upwards every second
while True:
    sense.show_letter(str(counting))
    sleep(1)
    counting = counting + 1
```
First a variable, here called counting, just because that is what you will be doing, is declared and set to be equal to one. Then a simple comment line and then the start of the loop. A while loop will run as long as it is True. Here the line actually says ‘while is true’ so the loop will always be true and will therefore always loop.

The next lines are indented by one space but that should be automatic as long the colon (:) at the end wasn’t missed out. Any code within the indented text belongs to this loop.

The next line converts the counting number (1 to start with) to a text figure to be written on the LED. Only text can be written on the SenseHat not numbers. The str changes the number into a string (of text). There is then a one second sleep (pause in the code) then counting which is one has a one added to it and then made equal to counting. So counting is now two. And so on.

Save and run the code as before.


## Obtaining the Readings
To get the reading change the previous code by adding this:
```
from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

# Take pressure readings when script starts
stairs_bottom = sense.get_pressure()
stairs_top = sense.get_pressure()

while True:
    stairs_top = sense.get_pressure()
    sense.show_message(str(stairs_top))
    sleep(5)
```

This will read the current air pressure from the emulator at the start and set it to be the higher air pressure felt at the bottom of the stairs. We live under a sea of air with the pressure of the air pushing down on us. As we climb mountains the height of the column of air above us becomes shorter so there is less air pushing down so therefore the air pressure drops. The rate of drop is consistent with altitude up to about 11 km. 	

Then the loop will every 5 seconds take another reading and print this new reading saved as the stairs_top. Save and run to check it works. Move the slider on the emulator pressure to see what happens. The next step is to make a calculation based on the readings.

Now for the calculation. This is the formula to use.

This is in the downloadable pdf.

The only thing about the formula for this exercise to worry about is the P and P0. These are the two air pressure readings. P0 is the base or zero reading, the other is the one to which there has been a change to.

So now in the code define a function that will use the two air pressure values and then calculate the result. Put this definition under the sense.clear() line. Functions like this are read Python, remembered and then used whenever needed. They are placed at the top of the program.
```
def calculate_altitude(stairs_bottom, stairs_top):
    # calculate altitude from air pressures and temperature of 20 deg C
    alt_accurate = 44330*(1-((stairs_top/stairs_bottom)**(1/5.255)))
    alt_m = round(alt_accurate, 2)
    return alt_m
```
This uses two figures gathered from the bottom and the top of the stairs and runs the calculation. You can compare the alt_accurate line to the equation. The next line alt_m rounds the answer down to two decimal places in metres (altitude metres) then returns the answer to the line that calls it.

To make the calculation run the function must be called into operation once the two readings are known.

Change the while loop again to this and run the script.
```
while True:
	stairs_top = sense.get_pressure()
	height_climbed = calculate_altitude(stairs_bottom, stairs_top)
	sense.show_message(str(height_climbed))
	sleep(5)
```
Now save and run the code and adjust the slider for the air pressure on the emulator to give a different reading and watch the answers appear.

## Adding the Final Pieces
This next piece of code demonstrates how to use the SenseHat joystick to take the readings. So change the while loop again to read:
```
while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
      
            # Check which direction
            if event.direction == "up":
                sense.show_letter("T")   # Letter T for top
                sleep(0.5)				
                stairs_top = sense.get_pressure()
                sense.show_message(str(stairs_top))
```
This looks a little complicated. It consists of nested code. Take it a line at a time. The ‘for event’ checks if there has been any sort of input from the SenseHat. If an event has happened called ‘pressed’ then if that event is also an ‘up’ event (the joystick is pushed upwards) then show the letter T, take the reading and show the reading.

Run this code and use the joystick on the emulator to take a reading.

The same checking for an event is required for the down press for the bottom reading and the inward middle press to make the calculation.

So the final pieces of code get the readings for the bottom of the stairs again without restarting the code and also to calculate the code.
```
           if event.direction == "down":
		    sense.show_letter("B")	# Letter B for bottom
		    sleep(0.5)
		    stairs_bottom = sense.get_pressure()
		    sense.show_message(str(cliff_bottom))
		    print(cliff_bottom)
				
           if event.direction == "middle":   # Middle to calculate heights
               stairs_height = calculate_altitude(stairs_bottom, stairs_top)
               sense.show_message(str(stairs_height))
               sleep(0.5)
               sense.clear()
```
Running this code with the emulator will finish the task. Except for climbing the stairs. For this the Raspberry Pi will need to run headless (without a keyboard, mouse or screen).

## Running Around Headless
Attach the real SenseHat to the Raspberry Pi and then add the small final parts to the code from the listing on the last page below. Run the code to make sure it works. The SenseHat is sensitive enough to read the pressure difference just by lifting the Raspberry Pi off the desk about one metre.

To run headless from a powerbank the script will need to run as soon as the Pi has booted. To do this a Crontab setting will be set.

Open a terminal (Alt + T) then type the following and Enter.
```
crontab -e
```
Select 2 and Enter.

Scroll to the bottom and add this line of code.
```
@reboot sudo python3 /home/pi/Documents/sensealtitude.py
```
This presumes that you have saved the script in the Documents folder with the sensealtitude.py name as instructed at the start of the worksheet.
Save this file (Ctrl + X, Y, Enter)

Power down the Pi and reboot and see if the script starts correctly. If all is well power down again, disconnect the screen, keyboard and mouse. Connect the powerbank and go and walk up the stairs!


The full code is shown below. There are some added flourishes to add some colour to the messages. Compare to make sure that everything is as it should be.
```
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# clear screen and rotate
sense.clear()
sense.set_rotation(180)

# set colours to use
green = (0, 255, 0)
red = (255, 0, 0)

# define top and bottom readings to start
stairs_bottom = sense.get_pressure()
stairs_top = sense.get_pressure()

# function to calculate the altitude
def calculate_altitude(stairs_bottom, stairs_top):
    # calculate altitude from air pressures and temperature of 20 deg C
    alt_accurate = 44330*(1-((stairs_top/stairs_bottom)**(1/5.255)))
    alt_m = round(alt_accurate, 2)
    return alt_m

sense.show_message("Ready to go")

# start loop to continuously check for button presses
while True:
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
      
            # Check which direction
	      if event.direction == "up":
               sense.show_letter("T", green)   # Letter T for top
		   sleep(0.5)				
		   stairs_top = sense.get_pressure()
               sense.show_message(str(cliff_top))
               print(cliff_top)
				
           if event.direction == "down":
               sense.show_letter("B", red)	# Letter B for bottom
               sleep(0.5)
               stairs_bottom = sense.get_pressure()
               sense.show_message(str(cliff_bottom))
               print(cliff_bottom)
				
           if event.direction == "middle":  # Middle to calculate heights
               stairs_height = calculate_altitude(stairs_bottom, stairs_top)
               sense.show_message(str(stairs_height))
               # Wait a while and then clear the screen
               sleep(0.5)
               sense.clear()
