import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

try:
    while True:
        humi, temp = Adafruit_DHT.read_try(sensor, pin)
        now = datetime.datetime.now()
        print(now,temp,humi)
        f = open('temphumi.txt','a')
        f.write(str(now) + ',' + str(temp) + ',' + str(humi) + '\r\n')
        f.close()
        time.sleep(1.0)
except KeyboardInterrupt:
    pass