from gpiozero import DistanceSensor, Buzzer
import time

TrigPin = 16
EchoPin = 20

sensor = DistanceSensor(echo=EchoPin, trigger=TrigPin)
buzzer = Buzzer(21)

def distance():
    start_time = time.time()
    end_time = time.time()

    while sensor.distance == 0:
        start_time = time.time()

    while sensor.distance > 0:
        end_time = time.time()

    duration = end_time - start_time
    distanceCm = duration * 17000 / 2  # Divide by 2 as it's a round trip
    distanceCm = round(distanceCm, 2)
    return distanceCm

try:
    while True:
        distanceCm = distance()
        if 0 <= distanceCm < 10:
            print("do")
            buzzer.frequency = 261.6
            buzzer.on()
        elif 10 <= distanceCm < 13:
            print("re")
            buzzer.frequency = 293.6
            buzzer.on()
        elif 13 <= distanceCm < 16:
            print("mi")
            buzzer.frequency = 329.6
            buzzer.on()
        elif 16 <= distanceCm < 19:
            print("fa")
            buzzer.frequency = 349.2
            buzzer.on()
        elif 19 <= distanceCm < 22:
            print("sol")
            buzzer.frequency = 392.0
            buzzer.on()
        elif 22 <= distanceCm < 25:
            print("la")
            buzzer.frequency = 440.0
            buzzer.on()
        elif 25 <= distanceCm < 28:
            print("si")
            buzzer.frequency = 493.9
            buzzer.on()
        elif 28 <= distanceCm < 31:
            print("5oc do")
            buzzer.frequency = 523.0
            buzzer.on()
        else:
            buzzer.off()
        print("cm:", distanceCm)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    buzzer.off()
