from gpiozero import DistanceSensor
import time

TrigPin = 16
EchoPin = 20

sensor = DistanceSensor(echo=EchoPin, trigger=TrigPin)

try:
    while True:
        distance_cm = sensor.distance * 100  # Convert from meters to centimeters
        print("cm:", round(distance_cm, 2))
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    sensor.close()
