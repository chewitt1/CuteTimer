""" To add tp ui/py file:
    MainWindow.setFixedSize(900, 675)
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
from PyQt5 import QtCore

from version2 import Ui_MainWindow

seamless = False


class MainWindow:
    def __init__(self):
        self.go = False
        self.win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)

        self.ui.startTime.clicked.connect(self.startProgram)
        self.ui.listTimers.currentIndexChanged.connect(self.setDisplay)
        self.ui.less.clicked.connect(lambda: self.setGoal(1))
        self.ui.more.clicked.connect(lambda: self.setGoal(0))

        self.ui.digital.toggled.connect(self.setWindow)
        self.ui.progress.toggled.connect(self.setWindow)
        self.ui.checkpoint.toggled.connect(self.setWindow)

        self.ui.icons.stateChanged.connect(self.setDesktopIcons)
        self.ui.seamless.stateChanged.connect(self.setSeamless)

    def show(self):
        self.win.show()

    def startProgram(self):
        self.go = True
        self.setWindow()

    def setWindow(self):  # 0 = home, 1 = digital, 2 = progress, 3 = done
        if self.go:
            if self.ui.digital.isChecked():
                self.ui.pages.setCurrentIndex(1)
            elif self.ui.progress.isChecked():
                self.ui.pages.setCurrentIndex(2)
            elif self.ui.checkpoint.isChecked():
                self.ui.pages.setCurrentIndex(3)
            self.setDisplay()

    def setDisplay(self):
        if self.ui.digital.isChecked():
            self.setDigital()
        elif self.ui.progress.isChecked():
            self.setProgress()
        elif self.ui.checkpoint.isChecked():
            self.setCheckpoint()

    def setDigital(self):
        i = self.ui.listTimers.currentIndex()

        if i == 0:
            self.ui.title_digital.setText("Choose Timer")
            self.ui.title_digital.update()
            self.ui.goal_digital.setText("00:00")
            self.ui.goal_digital.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
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

    def setProgress(self):
        i = self.ui.listTimers.currentIndex()

        if i == 0:
            self.ui.title_progress.setText("Choose Timer")
            self.ui.title_progress.update()
            self.ui.goal_progress.setText("0")
            self.ui.goal_progress.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
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
        if self.ui.digital.isChecked():
            self.setDigitalGoal(c)
        elif self.ui.progress.isChecked():
            self.setProgressGoal(c)
        elif self.ui.checkpoint.isChecked():
            self.setCheckpointGoal(c)

    def setDigitalGoal(self, c):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_digital.text().split(":")[0])

        if c == 0:
            if i == 1:
                if mins < 240:
                    self.ui.goal_digital.setText(str(mins + 15) + ":00")
                    self.ui.goal_digital.update()

            elif i == 3:
                if mins < 360:
                    mins += 1
                    if (mins / 10) < 1:
                        mins = "0" + str(mins)
                    self.ui.goal_digital.setText(str(mins) + ":00")
                    self.ui.goal_digital.update()

        elif c == 1:
            if i == 1:
                if mins > 15:
                    self.ui.goal_digital.setText(str(mins - 15) + ":00")
                    self.ui.goal_digital.update()

            elif i == 3:
                if mins > 0:
                    mins -= 1
                    if (mins / 10) < 1:
                        mins = "0" + str(mins)
                    self.ui.goal_digital.setText(str(mins) + ":00")
                    self.ui.goal_digital.update()

    def setProgressGoal(self, c):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_progress.text())

        if c == 0:
            if i == 1:
                if mins < 240:
                    self.ui.goal_progress.setText(str(mins + 15))
                    self.ui.goal_progress.update()

            elif i == 3:
                if mins < 360:
                    self.ui.goal_progress.setText(str(mins + 1))
                    self.ui.goal_progress.update()

        elif c == 1:
            if i == 1:
                if mins > 15:
                    self.ui.goal_progress.setText(str(mins - 15))
                    self.ui.goal_progress.update()

            elif i == 3:
                if mins > 0:
                    self.ui.goal_progress.setText(str(mins - 1))
                    self.ui.goal_progress.update()

    def setCheckpointGoal(self, c):
        i = self.ui.listTimers.currentIndex()
        mins = int(self.ui.goal_checkpoint.text())

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

    """def settings(self):
        if self.ui.icons.isChecked():
            self.setDesktopIcons()
        elif self.ui.seamless.isChecked():
            self.setSeamless()
     if self.ui.focus.isChecked():
            self.setAutoFocus()
       elif self.ui.breaks.isChecked():
            self.setAutoBreaks()
       elif self.ui.breaks.isChecked():
            self.setAutoBreaks()
       elif self.ui.shortcuts.isChecked():
            self.setShortcuts()
    """

    def setDesktopIcons(self):
        if self.ui.icons.isChecked():
            self.ui.desktop_icons.setVisible(True)
        else:
            self.ui.desktop_icons.setVisible(False)

    def setSeamless(self):
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.ui.MainWindow.setWindowFlags(flags)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
