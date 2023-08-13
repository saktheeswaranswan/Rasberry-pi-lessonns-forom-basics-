import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define LED pins
led_pins = [18, 23, 24, 25]  # Example pins, adjust based on your setup

# Initialize LED pins
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Number of scrolling iterations
scroll_iterations = 15

# Function to perform right-to-left scrolling
def scroll_leds():
    for i in range(len(led_pins)):
        GPIO.output(led_pins[i], GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led_pins[i], GPIO.LOW)

# Perform scrolling for the specified number of iterations
for _ in range(scroll_iterations):
    scroll_leds()

# Clean up GPIO settings
GPIO.cleanup()
