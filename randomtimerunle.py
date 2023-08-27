import RPi.GPIO as GPIO
import time
import random  # We'll use the random module to generate different delays

# Set up the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the LEDs
led_pins = [11, 13, 15]  # You can adjust these pin numbers according to your wiring

# Set up the GPIO pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Function to blink an LED with a random delay
def blink_led(pin):
    GPIO.output(pin, GPIO.HIGH)
    delay = random.uniform(0.2, 1.0)  # Generate a random delay between 0.2 and 1.0 seconds
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for pin in led_pins:
            blink_led(pin)
except KeyboardInterrupt:
    pass  # Exit the loop if Ctrl+C is pressed

# Clean up the GPIO configuration
GPIO.cleanup()
