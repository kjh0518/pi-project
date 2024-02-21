from gpiozero import Button
from signal import pause

sw_pin = 14
button = Button(sw_pin)

def on_button_pressed():
    print("Click")

button.when_pressed = on_button_pressed

pause()
