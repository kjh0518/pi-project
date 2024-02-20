from gpiozero import LED
import serial
from signal import pause

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

greenLed = LED(16)
blueLed = LED(20)
redLed = LED(21)

try:
    while True:
        data = bleSerial.readline().decode().strip()

        if data == "green_on":
            print("ok green on")
            greenLed.on()
        elif data == "green_off":
            print("ok green off")
            greenLed.off()
        elif data == "blue_on":
            print("ok blue on")
            blueLed.on()
        elif data == "blue_off":
            print("ok blue off")
            blueLed.off()
        elif data == "red_on":
            print("ok red on")
            redLed.on()
        elif data == "red_off":
            print("ok red off")
            redLed.off()

except KeyboardInterrupt:
    pass

finally:
    bleSerial.close()

pause()
