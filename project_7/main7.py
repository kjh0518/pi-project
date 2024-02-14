from gpiozero import PWMOutputDevice
import time

BUZZER_PIN = 21

buzzer = PWMOutputDevice(BUZZER_PIN)

try:
    while True:
        buzzer.value = 0.5  # 50% duty cycle
        buzzer.frequency = 261.6
        time.sleep(1.0)
        buzzer.frequency = 293.6
        time.sleep(1.0)
        buzzer.frequency = 329.6
        time.sleep(1.0)
        buzzer.frequency = 349.2
        time.sleep(1.0)
        buzzer.frequency = 391.9
        time.sleep(1.0)
        buzzer.value = 0  # Turn off the buzzer
        time.sleep(1.0)

except KeyboardInterrupt:
    pass

buzzer.close()
