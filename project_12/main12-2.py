import serial

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
try:
    while True:
        data = bleSerial.readline()
        data = data.decode()
        if data.find("green_on")>=0:
            print("ok green on")
        elif data.find("green_off")>=0:
            print("ok green off")
        elif data.find("blue_on")>=0:
            print("ok blue on")
        elif data.find("blue_off")>=0:
            print("ok blue off")
        elif data.find("red_on")>=0:
            print("ok red on")
        elif data.find("red_off")>=0:
            print("ok red off")
except KeyboardInterrupt:
    pass
bleSerial.close()