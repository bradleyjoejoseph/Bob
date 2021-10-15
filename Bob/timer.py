#timer - everything to do with the /timer command
import time

def timer(h, m, s):

    t = h * 360 + m * 60 + s
    timerLength = t
    while t:
        hours = t // 360
        mins = t // 60
        secs = t % 60
        timeer = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(timeer, end="\r")
        time.sleep(1)
        t -= 1
    
    print(timerLength, " timer completed")
    print("TimerOverSound: TODO")