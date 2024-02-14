import spidev
import gpiod
import time

buzzer_pin = 18

chip = gpiod.Chip("gpiochip0")
buzzer_line = chip.get_line(buzzer_pin)
buzzer_line.request(consumer="buzzer", type=gpiod.LINE_REQ_DIR_OUT)

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
        gas_value = analog_read(0)
        print(gas_value)

    
        if gas_value > 2000: 
            buzzer_line.set_value(1)
        else:
            buzzer_line.set_value(0)

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

finally:
 
    buzzer_line.release()
    chip.close()
    spi.close()
