from sense_emu import SenseHat  # sense_hat for real hardware, sense_emu for emulator

sense = SenseHat()

# clear screen
sense.clear()

sense.show_message("Welcome to the SenseHat")

