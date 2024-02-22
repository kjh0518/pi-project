from gpiozero import MotionSensor
import picamera
import datetime
import time

pir = MotionSensor(16)

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

try:
    while True:
        if pir.motion_detected:
            now = datetime.datetime.now()
            print(now)
            file_name = now.strftime('%Y-%m-%d %H:%M:%S')
            camera.capture(file_name + '.jpg')
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    camera.close()