import os

def speak(option, msg):
    os.system("espeak {} ' {} ' ".format(option,msg))
option = '-s 180 -p 50 -a 200 -v ko+f5'
msg = 'hello this is raspberrypi 5 project'

print('espeak',option,msg)
speak(option,msg)