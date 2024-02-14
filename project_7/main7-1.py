import RPi.GPIO as GPIO
import time

sw1 = 14
sw2 = 15
sw3 = 18
sw4 = 23
sw5 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)