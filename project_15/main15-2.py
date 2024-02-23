import time
import datetime
import picamera

flag = 0

camera = picamera.PiCamera()
camera.resolution = (1024,768)

filePath = "/home/jongho/myProjects/project_15/timelabs/"

try:
    while True:
        now = datetime.datetime.now()
        nowMin = now.minute
        print(nowMin)
        if nowMin % 5 == 0:
            if flag == 0:
                flag = 1
                fileName = now.strftime('%Y-%m-%d %H:%M:%S')
                camera.capture(filePath + fileName + '.jpg')
                print("ok")
        else:
            flag = 0
        time.sleep(1)
except KeyboardInterrupt:
    pass