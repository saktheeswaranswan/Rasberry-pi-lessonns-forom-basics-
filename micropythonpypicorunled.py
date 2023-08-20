import machine
import time

# Define the GPIO pins for the LEDs
led_pins = [ 1, 2,3]  # You can adjust these pin numbers according to your wiring

# Set up the GPIO pins as outputs
for pin in led_pins:
    machine.Pin(pin, machine.Pin.OUT)

# Function to blink an LED
def blink_led(pin, duration):
    pin.on()
    time.sleep(duration)
    pin.off()

# Create Pin objects for each LED
led_objects = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

try:
    while True:
        for led_pin in led_objects:
            blink_led(led_pin, 0.5)  # Blink each LED for 0.5 seconds
except KeyboardInterrupt:
    pass  # Exit the loop if Ctrl+C is pressed

# There's no GPIO cleanup needed for MicroPython on the Raspberry Pi Pico
