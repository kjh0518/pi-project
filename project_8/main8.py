from gpiozero import DistanceSensor
from signal import pause

TrigPin = 16
EchoPin = 20

# Create DistanceSensor object with the specified GPIO pins
ultrasonic_sensor = DistanceSensor(echo=EchoPin, trigger=TrigPin)

def print_distance(distance):
    print(f"Distance: {distance:.2f} cm")

# Set up an event handler for distance changes
ultrasonic_sensor.when_distance_changed = print_distance

# Keep the program running
pause()
