import time
import board
import digitalio
import random

# Define the GPIO pin numbers for the LEDs
led_pins = [board.GP0, board.GP1, board.GP2]

# Create DigitalInOut objects for each LED
leds = [digitalio.DigitalInOut(pin) for pin in led_pins]
for led in leds:
    led.direction = digitalio.Direction.OUTPUT

while True:
    for led in leds:
        led.value = not led.value
        delay_time = random.uniform(0.1, 1.0)  # Generate a random delay between 0.1 and 1.0 seconds
        scaled_delay = delay_time * 2  # Scale the delay time by a factor (e.g., 2)
        time.sleep(scaled_delay)
