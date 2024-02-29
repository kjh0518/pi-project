import RPi.GPIO as GPIO
import time

carLedRed = 2
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(carLedRed,GPIO.OUT)
GPIO.setup(carLedYellow,GPIO.OUT)
GPIO.setup(carLedGreen,GPIO.OUT)
GPIO.setup(humanLedRed,GPIO.OUT)
GPIO.setup(humanLedGreen,GPIO.OUT)

try:
    while 1:
        GPIO.output(carLedRed,GPIO.LOW)
        GPIO.output(carLedYellow,GPIO.LOW)
        GPIO.output(carLedGreen,GPIO.HIGH)
        GPIO.output(humanLedRed,GPIO.HIGH)
        GPIO.output(humanLedGreen,GPIO.LOW)
        time.sleep(5.0)
        
        GPIO.output(carLedRed,GPIO.LOW)
        GPIO.output(carLedYellow,GPIO.HIGH)
        GPIO.output(carLedGreen,GPIO.LOW)
        GPIO.output(humanLedRed,GPIO.HIGH)
        GPIO.output(humanLedGreen,GPIO.LOW)
        time.sleep(5.0)
        
        GPIO.output(carLedRed,GPIO.HIGH)
        GPIO.output(carLedYellow,GPIO.LOW)
        GPIO.output(carLedGreen,GPIO.LOW)
        GPIO.output(humanLedRed,GPIO.LOW)
        GPIO.output(humanLedGreen,GPIO.HIGH)
        time.sleep(5.0)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
        
        