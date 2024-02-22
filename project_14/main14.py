from gpiozero import MotionSensor
import time

pir = MotionSensor(16)

try:
    while True:
        sensorValue = pir.motion_detected
        print(sensorValue)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    pir.close()
