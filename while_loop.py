import time
from machine import Pin

led_pins = [0, 1, 2]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

delay_times = [0.2, 0.5, 1.0]

# Example while loop:
count = 0
while count < 5:
    for led, delay_time in zip(leds, delay_times):
        led.value(not led.value())
        time.sleep(delay_time)
    count += 1

print("Loop completed.")
