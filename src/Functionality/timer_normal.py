# The normal timer behavior
# import time
# import datetime
from timeit import default_timer as timer
from math import floor

class Timer:
    goal = 0
    start = 0
    elapsed = last = -1

    def getTimeString(self):
        min = sec = 0
        global goal

        sec = (goal*60) - (timer() - start)

        if(sec < 1):
            return "00:00"
        elif(sec > 60):
            min = int(sec/60)
            sec = int(sec%60)
        else:
            sec = floor(sec)

        if (min / 10) < 1:
            min = "0" + str(min)

        if (sec / 10) < 1:
            sec = "0" + str(sec)

        minSec = str(min) + ":" + str(sec)
        return minSec

    def setTimer(self, goalIn):
        global goal
        goal = goalIn
        if (goal / 10) < 1:
            return "0" + str(goal) + ":00"
        else:
            return str(goal) + ":00"

    def getTimer(self):
        global goal
        return goal

    def startTimer(self, goalIn):
        global start
        start = timer()
        return self.setTimer(goalIn);

    def oldTimer(self, num, start):
        elapsed = last = -1
        while elapsed < num:
            if int(elapsed) > last:
                print((num - 1) - int(elapsed))
                last = int(elapsed)
            end = time.time()
            elapsed = end - start

# boo = Timer()
# boo.startTimer(3)
# print(boo.getTimeString())