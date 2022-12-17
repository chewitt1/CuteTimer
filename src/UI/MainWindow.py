import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from version2 import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.win)

    def show(self):
        self.win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
