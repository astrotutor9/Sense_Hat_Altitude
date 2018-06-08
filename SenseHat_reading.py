from sense_emu import SenseHat  # sense_hat for real hardware, sense_emu for emulator

sense = SenseHat()

# clear screen
sense.clear()

# set a variable to collect pressure reading
pressure_reading = sense.get_pressure()

# show a message with the reading value but change numerical value
# to a string of text
print(pressure_reading)
sense.show_message(str(pressure_reading))

