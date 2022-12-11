# The normal timer behavior
import time
import datetime

class Timer:
    goal = 0
    start = 0
    elapsed = last = -1

    def getTimeString(self):
        global goal
        minSec = (str(datetime.timedelta(seconds= (goal*60) - (start - time.time()))))[2:]
        return minSec

    def setTimer(self, goalIn):
        global goal
        goal = goalIn

    def getTimer(self):
        global goal
        return goal

    def startTimer(self, goalIn):
        self.setTimer(goalIn);
        global start
        start = time.time()
        end = time.time()

    def oldTimer(self, num, start):
        elapsed = last = -1
        while elapsed < num:
            if int(elapsed) > last:
                print((num - 1) - int(elapsed))
                last = int(elapsed)
            end = time.time()
            elapsed = end - start
