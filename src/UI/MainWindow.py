""" To add tp ui/py file:
    MainWindow.setFixedSize(900, 675)
    self.less.setEnabled(False)
    self.more.setEnabled(False)
    self.digital.setChecked(True)
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from version2 import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)

        self.ui.startTime.clicked.connect(lambda: self.setWindow(1))
        self.ui.listTimers.currentIndexChanged.connect(self.setType)

    def show(self):
        self.win.show()

    def setWindow(self, num):  # 0 = home, 1 = digital, 2 = progress, 3 = done
        self.ui.pages.setCurrentIndex(num)

    def setType(self):
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
            self.ui.timeToGo.setText("00:00")
            self.ui.timeToGo.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
            self.ui.title_digital.setText("Focus Timer")
            self.ui.title_digital.update()
            self.ui.timeToGo.setText("15:00")
            self.ui.timeToGo.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-15")
            self.ui.more.setText("+15")

        elif i == 2:
            self.ui.title_digital.setText("Pomodoro Timer")
            self.ui.title_digital.update()
            self.ui.timeToGo.setText("25:00")
            self.ui.timeToGo.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)
            self.ui.less.setText("short")
            self.ui.more.setText("long")

        elif i == 3:
            self.ui.title_digital.setText("Class Timer")
            self.ui.title_digital.update()
            self.ui.timeToGo.setText("50:00")
            self.ui.timeToGo.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-1")
            self.ui.more.setText("+1")

    def setProgress(self):
        i = self.ui.listTimers.currentIndex()

        if i == 0:
            self.ui.title_progress.setText("Choose Timer")
            self.ui.title_progress.update()
            self.ui.progress_goal.setText("0")
            self.ui.progress_goal.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
            self.ui.title_progress.setText("Focus Timer")
            self.ui.title_progress.update()
            self.ui.progress_goal.setText("15")
            self.ui.progress_goal.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-15")
            self.ui.more.setText("+15")

        elif i == 2:
            self.ui.title_progress.setText("Pomodoro Timer")
            self.ui.title_progress.update()
            self.ui.progress_goal.setText("25")
            self.ui.progress_goal.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)
            self.ui.less.setText("short")
            self.ui.more.setText("long")

        elif i == 3:
            self.ui.title_progress.setText("Class Timer")
            self.ui.title_progress.update()
            self.ui.progress_goal.setText("50")
            self.ui.progress_goal.update()

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
            self.ui.checkpoint_goal.setText("0")
            self.ui.checkpoint_goal.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)

        elif i == 1:
            self.ui.title_checkpoint.setText("Focus Timer")
            self.ui.title_checkpoint.update()
            self.ui.checkpoint_goal.setText("15")
            self.ui.checkpoint_goal.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-15")
            self.ui.more.setText("+15")

        elif i == 2:
            self.ui.title_checkpoint.setText("Pomodoro Timer")
            self.ui.title_checkpoint.update()
            self.ui.checkpoint_goal.setText("25")
            self.ui.checkpoint_goal.update()

            self.ui.less.setEnabled(False)
            self.ui.more.setEnabled(False)
            self.ui.less.setText("short")
            self.ui.more.setText("long")

        elif i == 3:
            self.ui.title_checkpoint.setText("Class Timer")
            self.ui.title_checkpoint.update()
            self.ui.checkpoint_goal.setText("50")
            self.ui.checkpoint_goal.update()

            self.ui.less.setEnabled(True)
            self.ui.more.setEnabled(True)
            self.ui.less.setText("-1")
            self.ui.more.setText("+1")

        self.ui.point1.setProperty("value", 0)
        self.ui.point2.setProperty("value", 0)
        self.ui.point3.setProperty("value", 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
