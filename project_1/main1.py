import gpiod
import time

LED_PINS = [16, 20, 21]

chip = gpiod.Chip('gpiochip4')

lines = [chip.get_line(pin) for pin in LED_PINS]

for line in lines:
    line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        for line in lines:
            line.set_value(1)
        time.sleep(0.5)
        for line in lines:
            line.set_value(0)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    for line in lines:
        line.release()
