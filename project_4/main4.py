import gpiod
import time

ledwhite = 12
swpin = 21

chip = gpiod.Chip('gpiochip4')
line_white = chip.get_line(ledwhite)
line_switch = chip.get_line(swpin)

line_white.request(consumer="my_script", type=gpiod.LINE_REQ_DIR_OUT)
line_switch.request(consumer="my_script", type=gpiod.LINE_REQ_DIR_IN)

swstate = 0
newsw = 0
oldsw = 0

def sw_on():
    global newsw
    global oldsw
    newsw = line_switch.get_value()

    if newsw != oldsw:
        oldsw = newsw
        if newsw == 1:
            return 1
    return 0

try:
    while True:
        if sw_on() == 1:
            swstate = swstate + 1
            if swstate >= 4:
                swstate = 0
            time.sleep(0.2)
            
            print(swstate)

        if swstate == 0:
            line_white.set_value(0)
            print("duty: 0")
        elif swstate == 1:
            line_white.set_value(1)
            time.sleep(0.03)
            line_white.set_value(0)
            time.sleep(0.02)
            print("duty: 30")
        elif swstate == 2:
            line_white.set_value(1)
            time.sleep(0.06)
            line_white.set_value(0)
            time.sleep(0.04)
            print("duty: 60")
        elif swstate == 3:
            line_white.set_value(1)
            time.sleep(0.1)
            line_white.set_value(0)
            time.sleep(0.1)
            print("duty: 100")

except KeyboardInterrupt:
    pass

finally:
    line_white.release()
    line_switch.release()
    chip.close()
