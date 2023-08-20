#pip install RPi.GPIO
import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for the LEDs
led_pins = [11, 13, 15]  # You can adjust these pin numbers according to your wiring

# Set up the GPIO pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Function to blink an LED
def blink_led(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for pin in led_pins:
            blink_led(pin, 0.5)  # Blink each LED for 0.5 seconds
except KeyboardInterrupt:
    pass  # Exit the loop if Ctrl+C is pressed

# Clean up the GPIO configuration
GPIO.cleanup()
