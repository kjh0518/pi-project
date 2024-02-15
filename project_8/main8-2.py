from gpiozero import DistanceSensor
import time

TrigPin = 16
EchoPin = 20

sensor = DistanceSensor(echo=EchoPin, trigger=TrigPin)

def distance():
    start_time = time.time()
    end_time = time.time()

    while sensor.distance == 0:
        start_time = time.time()

    while sensor.distance > 0:
        end_time = time.time()

    duration = end_time - start_time
    distance_cm = duration * 17000 / 2  # Divide by 2 as it's a round trip
    distance_cm = round(distance_cm, 2)
    return distance_cm

try:
    while True:
        distanceCm = distance()
        if 0 <= distanceCm < 10:
            print("do")
        elif 10 <= distanceCm < 13:
            print("re")
        elif 13 <= distanceCm < 16:
            print("mi")
        elif 16 <= distanceCm < 19:
            print("fa")
        elif 19 <= distanceCm < 22:
            print("sol")
        elif 22 <= distanceCm < 25:
            print("la")
        elif 25 <= distanceCm < 28:
            print("si")
        elif 28 <= distanceCm < 31:
            print("5oc do")
        else:
            print("cm:", distanceCm)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    sensor.close()
