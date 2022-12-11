# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from timeit import default_timer as timer
import timer_normal
import timer_pomodoro

normalTimer = timer_normal.Timer()
pomTimer = timer_pomodoro.Pomodoro()
on = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.timer = QtCore.QTimer();
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.view = QtWidgets.QScrollArea(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(10, 10, 470, 520))
        self.view.setWidgetResizable(True)
        self.view.setObjectName("view")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 468, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.control2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.control2.setGeometry(QtCore.QRect(183, 120, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control2.setFont(font)
        self.control2.setObjectName("control2")
        self.focus = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.focus.setGeometry(QtCore.QRect(10, 200, 450, 140))
        font = QtGui.QFont()
        font.setPointSize(86)
        self.focus.setFont(font)
        self.focus.setAlignment(QtCore.Qt.AlignCenter)
        self.focus.setObjectName("focus")
        self.control1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.control1.setGeometry(QtCore.QRect(10, 120, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control1.setFont(font)
        self.control1.setObjectName("control1")
        self.start_stop = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.start_stop.setGeometry(QtCore.QRect(98, 400, 300, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.start_stop.setFont(font)
        self.start_stop.setObjectName("start_stop")
        self.control3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.control3.setGeometry(QtCore.QRect(350, 120, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.control3.setFont(font)
        self.control3.setObjectName("control3")
        self.Title_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Title_2.setGeometry(QtCore.QRect(80, 10, 311, 91))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(31)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title_2.setFont(font)
        self.Title_2.setAutoFillBackground(False)
        self.Title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_2.setObjectName("Title_2")
        self.view.setWidget(self.scrollAreaWidgetContents)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(489, 10, 311, 91))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(31)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Emoji = QtWidgets.QLabel(self.centralwidget)
        self.Emoji.setGeometry(QtCore.QRect(510, 70, 300, 141))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(41)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Emoji.setFont(font)
        self.Emoji.setAutoFillBackground(False)
        self.Emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.Emoji.setObjectName("Emoji")
        self.pomodoroButton = QtWidgets.QPushButton(self.centralwidget)
        self.pomodoroButton.setGeometry(QtCore.QRect(540, 340, 200, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.pomodoroButton.setFont(font)
        self.pomodoroButton.setObjectName("pomodoroButton")
        self.customButton = QtWidgets.QPushButton(self.centralwidget)
        self.customButton.setGeometry(QtCore.QRect(540, 220, 200, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.customButton.setFont(font)
        self.customButton.setObjectName("customButton")
        self.fifty17Button = QtWidgets.QPushButton(self.centralwidget)
        self.fifty17Button.setGeometry(QtCore.QRect(540, 460, 200, 71))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.fifty17Button.setFont(font)
        self.fifty17Button.setObjectName("fifty17Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuTimer = QtWidgets.QMenu(self.menubar)
        self.menuTimer.setObjectName("menuTimer")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actionPomodoro = QtWidgets.QAction(MainWindow)
        self.actionPomodoro.setObjectName("actionPomodoro")
        self.actionFifty = QtWidgets.QAction(MainWindow)
        self.actionFifty.setObjectName("actionFifty")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionHow_To = QtWidgets.QAction(MainWindow)
        self.actionHow_To.setObjectName("actionHow_To")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionTheme = QtWidgets.QAction(MainWindow)
        self.actionTheme.setObjectName("actionTheme")
        self.menuTimer.addAction(self.actionNormal)
        self.menuTimer.addAction(self.actionPomodoro)
        self.menuTimer.addAction(self.actionFifty)
        self.menuOptions.addAction(self.actionReset)
        self.menuOptions.addAction(self.actionTheme)
        self.menuHelp.addAction(self.actionHow_To)
        self.menuHelp.addAction(self.actionCredits)
        self.menubar.addAction(self.menuTimer.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Timer Control Trackers
        self.control1.clicked.connect(self.control1Clicked)
        self.control2.clicked.connect(self.control2Clicked)
        self.control3.clicked.connect(self.control3Clicked)

        self.start_stop.clicked.connect(self.on_press)
        self.start_stop.released.connect(self.on_release)
        self.timer.timeout.connect(self.startStop)

        # Switch Timers
        self.customButton.clicked.connect(self.normalClicked)
        self.pomodoroButton.clicked.connect(self.pomodoroClicked)
        self.fifty17Button.clicked.connect(self.fiftyClicked)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.control2.setText(_translate("MainWindow", "break"))
        self.focus.setText(_translate("MainWindow", "00:00"))
        self.control1.setText(_translate("MainWindow", "-"))
        self.start_stop.setText(_translate("MainWindow", "S T A R T"))
        self.control3.setText(_translate("MainWindow", "+"))
        self.Title_2.setText(_translate("MainWindow", "Normal"))
        self.Title.setText(_translate("MainWindow", "Cute Timer"))
        self.Emoji.setText(_translate("MainWindow", "(✿◠‿◠) "))
        self.pomodoroButton.setText(_translate("MainWindow", "Pomodoro"))
        self.customButton.setText(_translate("MainWindow", "Normal"))
        self.fifty17Button.setText(_translate("MainWindow", "52/17"))
        self.menuTimer.setTitle(_translate("MainWindow", "Timer"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionNormal.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionPomodoro.setText(_translate("MainWindow", "Pomodoro"))
        self.actionPomodoro.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionFifty.setText(_translate("MainWindow", "Fifty"))
        self.actionFifty.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHow_To.setText(_translate("MainWindow", "How To"))
        self.actionHow_To.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionCredits.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionTheme.setText(_translate("MainWindow", "Theme"))
        self.actionTheme.setShortcut(_translate("MainWindow", "Ctrl+T"))

    # Timer Button Scripts
    def normalClicked(self):
        self.control1.setText("-")
        self.control1.update()
        self.control2.setText("break")
        self.control2.update()
        self.control3.setText("+")
        self.control3.update()

    def pomodoroClicked(self):
        self.control1.setText("pomodoro")
        self.control1.update()
        self.control2.setText("short break")
        self.control2.update()
        self.control3.setText("long break")
        self.control3.update()

    def fiftyClicked(self):
        self.control1.setText("52")
        self.control1.update()
        self.control2.setText("52/17")
        self.control2.update()
        self.control3.setText("17")
        self.control3.update()

    def control1Clicked(self):
        global normalTimer
        if (self.Title_2.text() == "Normal"):
            if(normalTimer.goal > 0):
                normalTimer.goal -= 1
            curr = normalTimer.goal
            self.focus.setText(normalTimer.startTimer(curr))

    def control2Clicked(self):
        if (self.Title_2.text() == "Normal"):
            self.Title_2.setText("Break")
            self.control2.setText("timer")
        elif (self.Title_2.text() == "Break"):
            self.Title_2.setText("Normal")
            self.control2.setText("break")

    def control3Clicked(self):
        global normalTimer
        if(self.Title_2.text() == "Normal"):
            normalTimer.goal +=1
            curr =  normalTimer.goal
            self.focus.setText(normalTimer.startTimer(curr))

    def on_release(self):
        self.timer.stop()

    def on_press(self):
        global on, normalTimer
        if (self.Title_2.text() == "Normal"):
            if(on):
                on = False
                self.focus.setText(normalTimer.getTimeString())
            elif(not on):
                on = True
        self.timer.start(1000)

    def startStop(self):
        if (self.Title_2.text() == "Normal") or (self.Title_2.text() == "Break"):
            global on, normalTimer
            if (self.Title_2.text() == "Normal"):
                if(on):
                    global normalTimer
                    self.focus.setText(normalTimer.getTimeString())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Windows')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
