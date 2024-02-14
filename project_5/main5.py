import spidev
import gpiod
import time

led_white_pin = 18

chip = gpiod.Chip("gpiochip0")
led_line = chip.get_line(led_white_pin)
led_line.request(consumer="led_white", type=gpiod.LINE_REQ_DIR_OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def analog_read(ch):
    buf = [(1 << 2) | (1 << 1) | (ch & 4) >> 2, (ch & 3) << 6, 0]
    buf = spi.xfer(buf)
    adc_value = ((buf[1] & 0xF) << 8) | buf[2]
    return adc_value

try:
    while True:
        cds_value = analog_read(0)
        print(cds_value)

        if cds_value < 2000:
            led_line.set_value(1)
        else:
            led_line.set_value(0)
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
    led_line.release()
    chip.close()
    spi.close()