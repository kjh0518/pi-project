import gpiod
import time

ledred = 23
ledgreen = 24
swpin = 21

chip = gpiod.Chip('gpiochip4')
line_red = chip.get_line(ledred)
line_green = chip.get_line(ledgreen)
line_switch = chip.get_line(swpin)

line_red.request(consumer="my_script", type=gpiod.LINE_REQ_DIR_OUT)
line_green.request(consumer="my_script", type=gpiod.LINE_REQ_DIR_OUT)
line_switch.request(consumer="my_script", type=gpiod.LINE_REQ_DIR_IN)

swstate = 0

try:
    while True:
        swvalue = line_switch.get_value()

        if swvalue == 1:
            if swstate == 0:
                swstate = 1
            else:
                swstate = 0
            time.sleep(0.5)

        if swstate == 1:
            line_red.set_value(1)
            line_green.set_value(0)
            time.sleep(0.1)
            line_red.set_value(0)
            line_green.set_value(1)
            time.sleep(0.1)
        else:
            line_red.set_value(0)
            line_green.set_value(0)

except KeyboardInterrupt:
    pass

finally:
    line_red.release()
    line_green.release()
    line_switch.release()
    chip.close()
