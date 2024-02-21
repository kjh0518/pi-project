from gpiozero import Button
import picamera
import datetime

sw_pin = 14

button = Button(sw_pin)

camera = picamera.PiCamera()

camera.resolution = (1024, 768)

def on_button_pressed():
    now = datetime.datetime.now()
    print(now)
    file_name = now.strftime('%Y-%m-%d %H:%M:%S')
    camera.capture(file_name + '.jpg')

button.when_pressed = on_button_pressed

try:
    while True:
        pass  # Keep the script running

except KeyboardInterrupt:
    pass

finally:
    camera.close()
