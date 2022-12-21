""" To add tp ui/py file:
    CuteTimer.setFixedSize(900, 675)
    self.less.setEnabled(False)
    self.more.setEnabled(False)
    self.digital.setChecked(True)
    self.green.setEnabled(False)
    self.grey.setEnabled(False)
    self.focus.setCheckable(False)
    self.breaks.setCheckable(False)
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui

from version2 import Ui_CuteTimer


class MainWindow:
    def __init__(self):
        self.go = False
        self.done = False
        self.on = False
        self.isBreak = False
        self.long = False
        self.timeElapsed = 0
        self.timer = QtCore.QTimer()
        self.win = QMainWindow()
        self.win.setWindowIcon(QtGui.QIcon('./images/Alarm_Pink.ico'))
        self.ui = Ui_CuteTimer()
        self.ui.setupUi(self.win)

        self.ui.startTime.clicked.connect(self.startProgram)
        self.ui.listTimers.currentIndexChanged.connect(lambda: self.setDisplay(0))
        self.ui.less.clicked.connect(lambda: self.setGoal(1))
        self.ui.more.clicked.connect(lambda: self.setGoal(0))

        self.ui.digital.toggled.connect(self.setWindow)
        self.ui.progress.toggled.connect(self.setWindow)
        self.ui.checkpoint.toggled.connect(self.setWindow)

        self.ui.icons.stateChanged.connect(self.setDesktopIcons)
        self.ui.seamless.stateChanged.connect(self.setSeamless)

        self.ui.appExit.clicked.connect(self.endIt)

        self.ui.start.clicked.connect(self.startSecond)
        self.ui.start.released.connect(self.stopSecond)
        self.timer.timeout.connect(self.updateTime)
        self.ui.reset.clicked.connect(self.setReset)
        self.ui.setBreak.clicked.connect(lambda: self.setDisplay(1))

    def show(self):
        self.win.show()

    def startSecond(self):
        i = self.ui.listTimers.currentIndex()
        if self.on:
            self.on = False
            self.ui.start.setText("start")
            self.ui.start.update()
        elif not self.on and (i > 0):
            if self.go:
                self.on = True
                self.ui.start.setText("stop")
                self.ui.start.update()
                self.timer.start(1000)

    def stopSecond(self):
        self.timer.stop()

    def updateTime(self):
        i = self.ui.listTimers.currentIndex()
        if self.on and (i > 0):
            if self.ui.digital.isChecked():
                self.updateDigital()
            elif self.ui.progress.isChecked():
                self.updateProgress()
            elif self.ui.checkpoint.isChecked():
                self.updateCheckpoint()

    def setReset(self):
        self.on = False
        self.ui.start.setText("start")
        self.ui.start.update()
        self.setDisplay(0)

    def updateDigital(self):
        if self.on:
            mins = int(self.ui.goal_digital.text().split(":")[0])
            secs = int(self.ui.goal_digital.text().split(":")[1])

            finit = False

            if (mins == 0) and (secs == 1):
                finit = True

            if secs > 0:
                secs -= 1
            else:
                if mins > 0:
                    mins -= 1
                    secs = 59
            if (mins / 10) < 1 :
                mins = "0" + str(mins)

            if (secs / 10) < 1:
                secs = "0" + str(secs)

            self.ui.goal_digital.setText(str(mins) + ":" + str(secs))
            self.ui.goal_digital.update()

    def updateProgress(self):
        finit = False
        goal = int(self.ui.goal_progress.text()) * 60

        if self.timeElapsed < goal:
            self.timeElapsed += 1

        if self.timeElapsed == goal:
            finit = True

        val = int((100 * self.timeElapsed) / goal)
        self.ui.point1.setProperty("value", val)

    def updateCheckpoint(self):
        finit = False
        goal = int(self.ui.goal_checkpoint.text()) * 60

        if self.timeElapsed < goal:
            self.timeElapsed += 1

        if self.timeElapsed == goal:
            finit = True

        val = int((100 * self.timeElapsed) / goal)
        self.ui.progressBar.setProperty("value", val)

    def startProgram(self):
        self.go = True
        self.setWindow()

    @staticmethod
    def endIt():
        sys.exit()

    def setWindow(self):  # 0 = home, 1 = digital, 2 = progress, 3 = done
        if self.go:
            if self.ui.digital.isChecked():
                self.ui.pages.setCurrentIndex(1)
            elif self.ui.progress.isChecked():
                self.ui.pages.setCurrentIndex(2)
            elif self.ui.checkpoint.isChecked():
                self.ui.pages.setCurrentIndex(3)
            self.setDisplay(0)

    def setDisplay(self, b):
        if self.ui.digital.isChecked():
            self.setDigital(b)
        elif self.ui.progress.isChecked():
            self.setProgress(b)
        elif self.ui.checkpoint.isChecked():
            self.setCheckpoint()

    def setDigital(self, b):
        i = self.ui.listTimers.currentIndex()
        self.isBreak = False
        if i == 0:
            self.ui.title_digital.setText("Choose Timer")
            self.ui.title_digital.update()
            self.ui.goal_digital.setText("00:00")
            self.ui.goal_digital.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif b == 0:
            if i == 1:
                self.ui.title_digital.setText("Focus Timer")
                self.ui.title_digital.update()
                self.ui.goal_digital.setText("15:00")
                self.ui.goal_digital.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-15")
                self.ui.more.setText("+15")

            elif i == 2:
                self.ui.title_digital.setText("Pomodoro Timer")
                self.ui.title_digital.update()
                self.ui.goal_digital.setText("25:00")
                self.ui.goal_digital.update()

                self.ui.less.setEnabled(False)
                self.ui.more.setEnabled(False)
                self.ui.less.setText("short")
                self.ui.more.setText("long")

            elif i == 3:
                self.ui.title_digital.setText("Class Timer")
                self.ui.title_digital.update()
                self.ui.goal_digital.setText("50:00")
                self.ui.goal_digital.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-1")
                self.ui.more.setText("+1")

        elif b == 1:
            self.isBreak = True
            if i == 1 or i == 3:
                self.ui.title_digital.setText("Break Timer")
                self.ui.title_digital.update()
                self.ui.goal_digital.setText("05:00")
                self.ui.goal_digital.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-1")
                self.ui.more.setText("+1")

            elif i == 2:
                if self.long:
                    self.ui.title_digital.setText("Long Break")
                    self.ui.goal_digital.setText("10:00")
                else:
                    self.ui.title_digital.setText("Short Break")
                    self.ui.goal_digital.setText("05:00")

                self.ui.title_digital.update()
                self.ui.goal_digital.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("short")
                self.ui.more.setText("long")

    def setProgress(self, b):
        i = self.ui.listTimers.currentIndex()
        self.isBreak = False

        if i == 0:
            self.ui.title_progress.setText("Choose Timer")
            self.ui.title_progress.update()
            self.ui.goal_progress.setText("0")
            self.ui.goal_progress.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif b == 0:
            if i == 1:
                self.ui.title_progress.setText("Focus Timer")
                self.ui.title_progress.update()
                self.ui.goal_progress.setText("15")
                self.ui.goal_progress.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-15")
                self.ui.more.setText("+15")

            elif i == 2:
                self.ui.title_progress.setText("Pomodoro Timer")
                self.ui.title_progress.update()
                self.ui.goal_progress.setText("25")
                self.ui.goal_progress.update()

                self.ui.less.setEnabled(False)
                self.ui.more.setEnabled(False)
                self.ui.less.setText("short")
                self.ui.more.setText("long")

            elif i == 3:
                self.ui.title_progress.setText("Class Timer")
                self.ui.title_progress.update()
                self.ui.goal_progress.setText("50")
                self.ui.goal_progress.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-1")
                self.ui.more.setText("+1")

        elif b == 1:
            self.isBreak = True
            if i == 1 or i == 3:
                self.ui.title_progress.setText("Break Timer")
                self.ui.title_progress.update()
                self.ui.goal_progress.setText("5")
                self.ui.goal_progress.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("-1")
                self.ui.more.setText("+1")

            elif i == 2:
                if self.long:
                    self.ui.title_progress.setText("Long Break")
                    self.ui.goal_progress.setText("10")
                else:
                    self.ui.title_progress.setText("Short Break")
                    self.ui.goal_progress.setText("5")

                self.ui.title_progress.update()
                self.ui.goal_progress.update()

                self.ui.less.setEnabled(True)
                self.ui.more.setEnabled(True)
                self.ui.less.setText("short")
                self.ui.more.setText("long")

        self.ui.progressBar.setProperty("value", 0)

    def setCheckpoint(self):
        i = self.ui.listTimers.currentIndex()

        if i == 0:
            self.ui.title_checkpoint.setText("Choose Timer")
            self.ui.title_checkpoint.update()
            self.ui.goal_checkpoint.setText("0")
            self.ui.goal_checkpoint.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
            self.ui.title_checkpoint.setText("Focus Timer")
            self.ui.title_checkpoint.update()
            self.ui.goal_checkpoint.setText("15")
            self.ui.goal_checkpoint.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-15")
            self.ui.more.setText("+15")

        elif i == 2:
            self.ui.title_checkpoint.setText("Pomodoro Timer")
            self.ui.title_checkpoint.update()
            self.ui.goal_checkpoint.setText("25")
            self.ui.goal_checkpoint.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)
            self.ui.less.setText("short")
            self.ui.more.setText("long")

        elif i == 3:
            self.ui.title_checkpoint.setText("Class Timer")
            self.ui.title_checkpoint.update()
            self.ui.goal_checkpoint.setText("50")
            self.ui.goal_checkpoint.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-1")
            self.ui.more.setText("+1")

        self.ui.point1.setProperty("value", 0)
        self.ui.point2.setProperty("value", 0)
        self.ui.point3.setProperty("value", 0)

    def setGoal(self, c):
        b = 0
        if self.isBreak:
            b = 1
        if self.ui.digital.isChecked():
            self.setDigitalGoal(c, b)
        elif self.ui.progress.isChecked():
            self.setProgressGoal(c, b)
        elif self.ui.checkpoint.isChecked():
            self.setCheckpointGoal(c)

    def setDigitalGoal(self, c, b):  # In reverse order ):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_digital.text().split(":")[0])

        if c == 0:
            if i == 1 and b == 0:
                if mins < 240:
                    self.ui.goal_digital.setText(str(mins + 15) + ":00")
                    self.ui.goal_digital.update()

            elif i == 3 or (i == 1 and b == 1):
                if mins < 360:
                    mins += 1
                    if (mins / 10) < 1:
                        mins = "0" + str(mins)
                    self.ui.goal_digital.setText(str(mins) + ":00")
                    self.ui.goal_digital.update()

            elif i == 2 and b == 1:
                self.long = True
                self.setDigital(1)

        elif c == 1:
            if i == 1 and b == 0:
                if mins > 15:
                    self.ui.goal_digital.setText(str(mins - 15) + ":00")
                    self.ui.goal_digital.update()

            elif i == 3 or (i == 1 and b == 1):
                if mins > 0:
                    mins -= 1
                    if (mins / 10) < 1:
                        mins = "0" + str(mins)
                    self.ui.goal_digital.setText(str(mins) + ":00")
                    self.ui.goal_digital.update()

            elif i == 2 and b == 1:
                self.long = False
                self.setDigital(1)

    def setProgressGoal(self, c, b):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_progress.text())
        self.timeElapsed = 0

        if c == 0:
            if i == 1 and b == 0:
                if mins < 240:
                    self.ui.goal_progress.setText(str(mins + 15))
                    self.ui.goal_progress.update()

            elif i == 3 or (i == 1 and b == 1):
                if mins < 360:
                    self.ui.goal_progress.setText(str(mins + 1))
                    self.ui.goal_progress.update()

            elif i == 2 and b == 1:
                self.long = True
                self.setProgress(1)

        elif c == 1:
            if i == 1 and b == 0:
                if mins > 15:
                    self.ui.goal_progress.setText(str(mins - 15))
                    self.ui.goal_progress.update()

            elif i == 3 or (i == 1 and b == 1):
                if mins > 0:
                    self.ui.goal_progress.setText(str(mins - 1))
                    self.ui.goal_progress.update()

            elif i == 2 and b == 1:
                self.long = False
                self.setProgress(1)

    def setCheckpointGoal(self, c):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_checkpoint.text())
        self.timeElapsed = 0

        if c == 0:
            if i == 1:
                if mins < 240:
                    self.ui.goal_checkpoint.setText(str(mins + 15))
                    self.ui.goal_checkpoint.update()

            elif i == 3:
                if mins < 360:
                    self.ui.goal_checkpoint.setText(str(mins + 1))
                    self.ui.goal_checkpoint.update()

        elif c == 1:
            if i == 1:
                if mins > 15:
                    self.ui.goal_checkpoint.setText(str(mins - 15))
                    self.ui.goal_checkpoint.update()

            elif i == 3:
                if mins > 0:
                    self.ui.goal_checkpoint.setText(str(mins - 1))
                    self.ui.goal_checkpoint.update()

    def setDesktopIcons(self):
        if self.ui.icons.isChecked():
            self.ui.desktop_icons.setVisible(True)
        else:
            self.ui.desktop_icons.setVisible(False)

    def setSeamless(self):
        if self.ui.seamless.isChecked():
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        else:
            flags = QtCore.Qt.WindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.win.setWindowFlags(flags)
        self.win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
