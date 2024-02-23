import time
import datetime

try:
    while True:
        now = datetime.datetime.now()
        nowMin = now.minute
        print(nowMin)
        if nowMin % 5 ==0:
            print("ok")
        time.sleep(1)
except KeyboardInterrupt:
    pass
