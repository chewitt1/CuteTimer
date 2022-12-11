# The pomodoro timer behavior
from timeit import default_timer as timer
from math import floor

POM_VAL = 25
BREAK_SHORT = 5
BREAK_LONG = 10

class Pomodoro:
    start = 0
    elapsed = last = -1

    def getTimeString(self):

        min = sec = 0

        sec = (POM_VAL*60) - (timer() - start)

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

    def setTimer(self):
            return str(POM_VAL) + ":00"

    def setShortBreak(self):
        return str(BREAK_SHORT) + ":00"

    def setLongBreak(self):
        return str(BREAK_LONG) + ":00"

    def getTimer(self):
        return POM_VAL

    def startTimer(self):
        global start
        start = timer()
        return self.setTimer();

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