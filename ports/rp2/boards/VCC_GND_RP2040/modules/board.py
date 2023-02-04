from machine import Pin, Timer

led = Pin(25, Pin.OUT)
ws2812 = Pin(23, Pin.OUT, Pin.PULL_UP)
key = Pin(24, Pin.IN, Pin.PULL_UP)

led_status = 1
key_status = key.value()
led.value(led_status)

def toggle_led_by_button():
    global led_status
    led_status = 0 if led_status == 1 else 1
    led.value(led_status)

while True:
    if key.value() != key_status:
        key_status = key.value()
        if key_status == 0:
            print("pressdown")
            toggle_led_by_button()
        else:
            print("pressup")
