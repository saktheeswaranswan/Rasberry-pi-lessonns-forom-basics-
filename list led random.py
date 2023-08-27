
import time
import board
import digitalio

# Define the GPIO pin numbers for the LEDs
led_pins = [board.GP0, board.GP1, board.GP2]

# Create DigitalInOut objects for each LED
leds = [digitalio.DigitalInOut(pin) for pin in led_pins]
for led in leds:
    led.direction = digitalio.Direction.OUTPUT

# Define a list of delay times in seconds
delay_times = [0.2, 0.5, 1.0]

while True:
    for led, delay_time in zip(leds, delay_times):
        led.value = not led.value
        time.sleep(delay_time)
