import time
import datetime

flag = 0

try:
    while True:
        now = datetime.datetime.now()
        nowMin = now.minute
        print(nowMin)
        if nowMin % 5 == 0:
            if flag == 0:
                flag = 1
                print("ok")
        else:
            flag = 0
        time.sleep(1)
except KeyboardInterrupt:
    pass
