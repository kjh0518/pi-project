import gpiod
import time

carLEDred = 2
carLEDyellow = 3
carLEDgreen = 4
humanLEDred = 20
humanLEDgreen = 21

chip = gpiod.Chip('gpiochip4')

# Create lines for each LED
car_led_lines = [chip.get_line(pin) for pin in [carLEDred, carLEDyellow, carLEDgreen]]
human_led_lines = [chip.get_line(pin) for pin in [humanLEDred, humanLEDgreen]]

# Request the lines for output
for line in car_led_lines + human_led_lines:
    line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        for line in car_led_lines:
            line.set_value(0)  # GPIO.LOW
        for line in human_led_lines:
            line.set_value(1)  # GPIO.HIGH
        time.sleep(3.0)

        for line in car_led_lines[1:]:  # Skip carLEDred
            line.set_value(1)  # GPIO.HIGH
        for line in human_led_lines[:1]:  # Only humanLEDred
            line.set_value(1)  # GPIO.HIGH
        time.sleep(1.0)

        car_led_lines[0].set_value(1)  # Set carLEDred to GPIO.HIGH
        for line in car_led_lines[1:]:  # Skip carLEDred
            line.set_value(0)  # GPIO.LOW
        for line in human_led_lines[1:]:  # Skip humanLEDred
            line.set_value(1)  # GPIO.HIGH
        time.sleep(3.0)

except KeyboardInterrupt:
    pass

finally:
    for line in car_led_lines + human_led_lines:
        line.release()
