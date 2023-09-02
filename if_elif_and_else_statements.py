import time
from machine import Pin

led_pins = [0, 1, 2]  # GPIO pins for LEDs
leds = [Pin(pin, Pin.OUT) for pin in led_pins]

delay_times = [0.2, 0.5, 1.0]

while True:
    for led, delay_time in zip(leds, delay_times):
        led.value(not led.value())
        time.sleep(delay_time)

    # Conditional statements
    if leds[0].value() == 0:
        print("LED 1 is off")
    elif leds[1].value() == 0:
        print("LED 2 is off")
    else:
        print("LED 3 is off")
