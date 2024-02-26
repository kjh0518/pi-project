from gpiozero import Button
from signal import pause

swPin = 14

button = Button(swPin)

def on_button_press():
    print("click")

button.when_pressed = on_button_press

pause()
