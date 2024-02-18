import time
from gpiozero import LED
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

green_led = LED(16)
blue_led = LED(20)
red_led = LED(21)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        comfort_index = (1.8 * temperature) - (0.55 * (1 - humidity / 100.0) * (1.8 * temperature - 26)) + 32
        print(comfort_index)

        if comfort_index <= 69:
            green_led.on()
            blue_led.off()
            red_led.off()
        elif 70 <= comfort_index <= 75:
            green_led.off()
            blue_led.on()
            red_led.off()
        elif comfort_index >= 76:
            green_led.off()
            blue_led.off()
            red_led.on()

        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    green_led.off()
    blue_led.off()
    red_led.off()
