import time
from machine import Pin

led_pins = [0, 1, 2]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

delay_times = [0.2, 0.5, 1.0]

while True:
    for led, delay_time in zip(leds, delay_times):
        led.value(not led.value())
        time.sleep(delay_time)

    if leds[0].value() == 0:  # Example condition
        print("LED 1 is off, exiting the loop")
        break  # Exit the loop if the condition is met
