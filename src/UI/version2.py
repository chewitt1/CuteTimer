# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'version2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CuteTimer(object):
    def setupUi(self, CuteTimer):
        CuteTimer.setObjectName("CuteTimer")
        CuteTimer.resize(900, 675)
        font = QtGui.QFont()
        font.setPointSize(51)
        CuteTimer.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Alarm_Pink.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CuteTimer.setWindowIcon(icon)
        CuteTimer.setAutoFillBackground(True)
        CuteTimer.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(CuteTimer)
        self.centralwidget.setStyleSheet("background-color: #967d8c")
        self.centralwidget.setObjectName("centralwidget")
        self.taskbar = QtWidgets.QFrame(self.centralwidget)
        self.taskbar.setGeometry(QtCore.QRect(-1, 643, 902, 32))
        self.taskbar.setStyleSheet("background-color: #E2C2C6")
        self.taskbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.taskbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taskbar.setObjectName("taskbar")
        self.Start = QtWidgets.QPushButton(self.taskbar)
        self.Start.setGeometry(QtCore.QRect(3, 3, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Start.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../WindowsGUI/Windows95/images/win95.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Start.setIcon(icon1)
        self.Start.setObjectName("Start")
        self.Welcome = QtWidgets.QLineEdit(self.taskbar)
        self.Welcome.setGeometry(QtCore.QRect(80, 3, 191, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Welcome.setFont(font)
        self.Welcome.setStyleSheet("")
        self.Welcome.setObjectName("Welcome")
        self.Sroll_Time = QtWidgets.QScrollArea(self.taskbar)
        self.Sroll_Time.setGeometry(QtCore.QRect(934, 3, 64, 26))
        self.Sroll_Time.setWidgetResizable(True)
        self.Sroll_Time.setObjectName("Sroll_Time")
        self.Sroll_TimeContents = QtWidgets.QWidget()
        self.Sroll_TimeContents.setGeometry(QtCore.QRect(0, 0, 62, 24))
        self.Sroll_TimeContents.setObjectName("Sroll_TimeContents")
        self.currentTime = QtWidgets.QLabel(self.Sroll_TimeContents)
        self.currentTime.setGeometry(QtCore.QRect(0, 1, 64, 20))
        self.currentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime.setObjectName("currentTime")
        self.Sroll_Time.setWidget(self.Sroll_TimeContents)
        self.Sroll_Time_2 = QtWidgets.QScrollArea(self.taskbar)
        self.Sroll_Time_2.setGeometry(QtCore.QRect(834, 3, 64, 26))
        self.Sroll_Time_2.setWidgetResizable(True)
        self.Sroll_Time_2.setObjectName("Sroll_Time_2")
        self.Sroll_TimeContents_3 = QtWidgets.QWidget()
        self.Sroll_TimeContents_3.setGeometry(QtCore.QRect(0, 0, 62, 24))
        self.Sroll_TimeContents_3.setObjectName("Sroll_TimeContents_3")
        self.currentTime_3 = QtWidgets.QLabel(self.Sroll_TimeContents_3)
        self.currentTime_3.setGeometry(QtCore.QRect(0, 1, 64, 20))
        self.currentTime_3.setAlignment(QtCore.Qt.AlignCenter)
        self.currentTime_3.setObjectName("currentTime_3")
        self.Sroll_Time_2.setWidget(self.Sroll_TimeContents_3)
        self.app = QtWidgets.QFrame(self.centralwidget)
        self.app.setGeometry(QtCore.QRect(100, 20, 790, 600))
        self.app.setStyleSheet("background-color: #E2C2C6")
        self.app.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app.setObjectName("app")
        self.appBar = QtWidgets.QWidget(self.app)
        self.appBar.setGeometry(QtCore.QRect(1, 1, 787, 31))
        self.appBar.setStyleSheet("background-color: #846075")
        self.appBar.setObjectName("appBar")
        self.appName = QtWidgets.QLabel(self.appBar)
        self.appName.setGeometry(QtCore.QRect(3, 5, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.appName.setFont(font)
        self.appName.setStyleSheet("color: white")
        self.appName.setObjectName("appName")
        self.appExit = QtWidgets.QPushButton(self.appBar)
        self.appExit.setGeometry(QtCore.QRect(760, 3, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.appExit.setFont(font)
        self.appExit.setStyleSheet("background-color: #E2C2C6")
        self.appExit.setObjectName("appExit")
        self.mainTimer = QtWidgets.QScrollArea(self.app)
        self.mainTimer.setGeometry(QtCore.QRect(20, 100, 541, 440))
        self.mainTimer.setWidgetResizable(True)
        self.mainTimer.setObjectName("mainTimer")
        self.mainTimerChildren = QtWidgets.QWidget()
        self.mainTimerChildren.setGeometry(QtCore.QRect(0, 0, 539, 438))
        self.mainTimerChildren.setObjectName("mainTimerChildren")
        self.pages = QtWidgets.QStackedWidget(self.mainTimerChildren)
        self.pages.setGeometry(QtCore.QRect(0, 0, 550, 440))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pages.setFont(font)
        self.pages.setToolTip("")
        self.pages.setStyleSheet("")
        self.pages.setObjectName("pages")
        self.page_home = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(15)
        self.page_home.setFont(font)
        self.page_home.setObjectName("page_home")
        self.welcome = QtWidgets.QLabel(self.page_home)
        self.welcome.setGeometry(QtCore.QRect(40, 30, 471, 181))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(42)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("background-color:0; color: #ffdeda")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.startTime = QtWidgets.QPushButton(self.page_home)
        self.startTime.setGeometry(QtCore.QRect(130, 370, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startTime.setFont(font)
        self.startTime.setObjectName("startTime")
        self.bkgrnd = QtWidgets.QLabel(self.page_home)
        self.bkgrnd.setGeometry(QtCore.QRect(0, 0, 550, 440))
        self.bkgrnd.setText("")
        self.bkgrnd.setPixmap(QtGui.QPixmap("pixel.png"))
        self.bkgrnd.setObjectName("bkgrnd")
        self.bkgrnd.raise_()
        self.startTime.raise_()
        self.welcome.raise_()
        self.pages.addWidget(self.page_home)
        self.page_digital = QtWidgets.QWidget()
        self.page_digital.setObjectName("page_digital")
        self.title_digital = QtWidgets.QLabel(self.page_digital)
        self.title_digital.setGeometry(QtCore.QRect(30, 10, 481, 151))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(46)
        self.title_digital.setFont(font)
        self.title_digital.setStyleSheet("background-color:0; color: #ffdeda")
        self.title_digital.setAlignment(QtCore.Qt.AlignCenter)
        self.title_digital.setObjectName("title_digital")
        self.goal_digital = QtWidgets.QLabel(self.page_digital)
        self.goal_digital.setGeometry(QtCore.QRect(30, 160, 471, 151))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(102)
        self.goal_digital.setFont(font)
        self.goal_digital.setStyleSheet("background-color:0; color: #ffdeda")
        self.goal_digital.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_digital.setObjectName("goal_digital")
        self.bkgrnd_2 = QtWidgets.QLabel(self.page_digital)
        self.bkgrnd_2.setGeometry(QtCore.QRect(0, 0, 550, 440))
        self.bkgrnd_2.setText("")
        self.bkgrnd_2.setPixmap(QtGui.QPixmap("pixel.png"))
        self.bkgrnd_2.setObjectName("bkgrnd_2")
        self.bkgrnd_2.raise_()
        self.title_digital.raise_()
        self.goal_digital.raise_()
        self.pages.addWidget(self.page_digital)
        self.page_progress = QtWidgets.QWidget()
        self.page_progress.setObjectName("page_progress")
        self.title_progress = QtWidgets.QLabel(self.page_progress)
        self.title_progress.setGeometry(QtCore.QRect(30, 10, 481, 151))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(46)
        self.title_progress.setFont(font)
        self.title_progress.setStyleSheet("background-color:0; color: #ffdeda")
        self.title_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.title_progress.setObjectName("title_progress")
        self.bkgrnd_3 = QtWidgets.QLabel(self.page_progress)
        self.bkgrnd_3.setGeometry(QtCore.QRect(0, 0, 550, 440))
        self.bkgrnd_3.setStyleSheet("")
        self.bkgrnd_3.setText("")
        self.bkgrnd_3.setPixmap(QtGui.QPixmap("pixel.png"))
        self.bkgrnd_3.setObjectName("bkgrnd_3")
        self.progressBar = QtWidgets.QProgressBar(self.page_progress)
        self.progressBar.setGeometry(QtCore.QRect(40, 140, 501, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color:#ffdeda; color: #ffdeda")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.goal_progress = QtWidgets.QLabel(self.page_progress)
        self.goal_progress.setGeometry(QtCore.QRect(218, 160, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.goal_progress.setFont(font)
        self.goal_progress.setStyleSheet("background-color:0; color: #ffdeda")
        self.goal_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_progress.setObjectName("goal_progress")
        self.bkgrnd_3.raise_()
        self.title_progress.raise_()
        self.progressBar.raise_()
        self.goal_progress.raise_()
        self.pages.addWidget(self.page_progress)
        self.page_checkpoint = QtWidgets.QWidget()
        self.page_checkpoint.setObjectName("page_checkpoint")
        self.bkgrnd_4 = QtWidgets.QLabel(self.page_checkpoint)
        self.bkgrnd_4.setGeometry(QtCore.QRect(0, 0, 540, 440))
        self.bkgrnd_4.setText("")
        self.bkgrnd_4.setPixmap(QtGui.QPixmap("pixel.png"))
        self.bkgrnd_4.setObjectName("bkgrnd_4")
        self.title_checkpoint = QtWidgets.QLabel(self.page_checkpoint)
        self.title_checkpoint.setGeometry(QtCore.QRect(30, 10, 481, 151))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(46)
        self.title_checkpoint.setFont(font)
        self.title_checkpoint.setStyleSheet("background-color:0; color: #ffdeda")
        self.title_checkpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.title_checkpoint.setObjectName("title_checkpoint")
        self.point1 = QtWidgets.QSlider(self.page_checkpoint)
        self.point1.setGeometry(QtCore.QRect(0, 377, 180, 22))
        self.point1.setStyleSheet("background-color:0; color: #ffdeda")
        self.point1.setMaximum(33)
        self.point1.setOrientation(QtCore.Qt.Horizontal)
        self.point1.setObjectName("point1")
        self.point2 = QtWidgets.QSlider(self.page_checkpoint)
        self.point2.setGeometry(QtCore.QRect(180, 377, 180, 22))
        self.point2.setStyleSheet("background-color:0; color: #ffdeda")
        self.point2.setMaximum(34)
        self.point2.setOrientation(QtCore.Qt.Horizontal)
        self.point2.setObjectName("point2")
        self.point3 = QtWidgets.QSlider(self.page_checkpoint)
        self.point3.setGeometry(QtCore.QRect(360, 377, 180, 22))
        self.point3.setStyleSheet("background-color:0; color: #ffdeda")
        self.point3.setMaximum(33)
        self.point3.setOrientation(QtCore.Qt.Horizontal)
        self.point3.setObjectName("point3")
        self.goal_checkpoint = QtWidgets.QLabel(self.page_checkpoint)
        self.goal_checkpoint.setGeometry(QtCore.QRect(218, 130, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.goal_checkpoint.setFont(font)
        self.goal_checkpoint.setStyleSheet("background-color:0; color: #ffdeda")
        self.goal_checkpoint.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_checkpoint.setObjectName("goal_checkpoint")
        self.pages.addWidget(self.page_checkpoint)
        self.mainTimer.setWidget(self.mainTimerChildren)
        self.theme = QtWidgets.QGroupBox(self.app)
        self.theme.setGeometry(QtCore.QRect(580, 40, 191, 141))
        self.theme.setObjectName("theme")
        self.pink = QtWidgets.QPushButton(self.theme)
        self.pink.setGeometry(QtCore.QRect(10, 20, 170, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pink.setFont(font)
        self.pink.setObjectName("pink")
        self.green = QtWidgets.QPushButton(self.theme)
        self.green.setGeometry(QtCore.QRect(10, 60, 170, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.green.setFont(font)
        self.green.setObjectName("green")
        self.grey = QtWidgets.QPushButton(self.theme)
        self.grey.setGeometry(QtCore.QRect(10, 100, 170, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.grey.setFont(font)
        self.grey.setObjectName("grey")
        self.display = QtWidgets.QGroupBox(self.app)
        self.display.setGeometry(QtCore.QRect(580, 190, 191, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.display.setFont(font)
        self.display.setObjectName("display")
        self.digital = QtWidgets.QRadioButton(self.display)
        self.digital.setGeometry(QtCore.QRect(10, 30, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.digital.setFont(font)
        self.digital.setObjectName("digital")
        self.progress = QtWidgets.QRadioButton(self.display)
        self.progress.setGeometry(QtCore.QRect(10, 60, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progress.setFont(font)
        self.progress.setObjectName("progress")
        self.checkpoint = QtWidgets.QRadioButton(self.display)
        self.checkpoint.setGeometry(QtCore.QRect(10, 90, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkpoint.setFont(font)
        self.checkpoint.setObjectName("checkpoint")
        self.settings = QtWidgets.QGroupBox(self.app)
        self.settings.setGeometry(QtCore.QRect(580, 320, 191, 221))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.settings.setFont(font)
        self.settings.setObjectName("settings")
        self.sounds = QtWidgets.QCheckBox(self.settings)
        self.sounds.setGeometry(QtCore.QRect(10, 120, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sounds.setFont(font)
        self.sounds.setChecked(True)
        self.sounds.setObjectName("sounds")
        self.stop = QtWidgets.QCheckBox(self.settings)
        self.stop.setGeometry(QtCore.QRect(10, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.icons = QtWidgets.QCheckBox(self.settings)
        self.icons.setGeometry(QtCore.QRect(10, 150, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.icons.setFont(font)
        self.icons.setChecked(True)
        self.icons.setObjectName("icons")
        self.breaks = QtWidgets.QCheckBox(self.settings)
        self.breaks.setGeometry(QtCore.QRect(10, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.breaks.setFont(font)
        self.breaks.setStyleSheet("color: #d1d9e3")
        self.breaks.setObjectName("breaks")
        self.focus = QtWidgets.QCheckBox(self.settings)
        self.focus.setGeometry(QtCore.QRect(10, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.focus.setFont(font)
        self.focus.setStyleSheet("color: #d1d9e3")
        self.focus.setObjectName("focus")
        self.seamless = QtWidgets.QCheckBox(self.settings)
        self.seamless.setGeometry(QtCore.QRect(10, 180, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.seamless.setFont(font)
        self.seamless.setObjectName("seamless")
        self.listTimers = QtWidgets.QComboBox(self.app)
        self.listTimers.setGeometry(QtCore.QRect(100, 53, 281, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listTimers.setFont(font)
        self.listTimers.setObjectName("listTimers")
        self.listTimers.addItem("")
        self.listTimers.addItem("")
        self.listTimers.addItem("")
        self.listTimers.addItem("")
        self.type = QtWidgets.QLabel(self.app)
        self.type.setGeometry(QtCore.QRect(22, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.less = QtWidgets.QPushButton(self.app)
        self.less.setGeometry(QtCore.QRect(392, 50, 80, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.less.setFont(font)
        self.less.setStyleSheet("")
        self.less.setCheckable(False)
        self.less.setChecked(False)
        self.less.setDefault(False)
        self.less.setFlat(False)
        self.less.setObjectName("less")
        self.more = QtWidgets.QPushButton(self.app)
        self.more.setGeometry(QtCore.QRect(484, 50, 80, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.more.setFont(font)
        self.more.setObjectName("more")
        self.start = QtWidgets.QPushButton(self.app)
        self.start.setGeometry(QtCore.QRect(488, 560, 90, 28))
        self.start.setStyleSheet("")
        self.start.setObjectName("start")
        self.reset = QtWidgets.QPushButton(self.app)
        self.reset.setGeometry(QtCore.QRect(588, 560, 90, 28))
        self.reset.setStyleSheet("")
        self.reset.setObjectName("reset")
        self.setBreak = QtWidgets.QPushButton(self.app)
        self.setBreak.setGeometry(QtCore.QRect(689, 560, 90, 28))
        self.setBreak.setStyleSheet("")
        self.setBreak.setObjectName("setBreak")
        self.label = QtWidgets.QLabel(self.app)
        self.label.setGeometry(QtCore.QRect(80, 560, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.desktop_icons = QtWidgets.QWidget(self.centralwidget)
        self.desktop_icons.setGeometry(QtCore.QRect(10, 19, 81, 601))
        self.desktop_icons.setObjectName("desktop_icons")
        self.img_lofi = QtWidgets.QLabel(self.desktop_icons)
        self.img_lofi.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.img_lofi.setText("")
        self.img_lofi.setPixmap(QtGui.QPixmap("images/Music Disc Pink.ico"))
        self.img_lofi.setObjectName("img_lofi")
        self.lofi = QtWidgets.QLabel(self.desktop_icons)
        self.lofi.setGeometry(QtCore.QRect(20, 45, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lofi.setFont(font)
        self.lofi.setStyleSheet("color: #E2C2C6")
        self.lofi.setAlignment(QtCore.Qt.AlignCenter)
        self.lofi.setObjectName("lofi")
        self.img_yt = QtWidgets.QLabel(self.desktop_icons)
        self.img_yt.setGeometry(QtCore.QRect(22, 410, 31, 31))
        self.img_yt.setText("")
        self.img_yt.setPixmap(QtGui.QPixmap("images/Cine-film-Pink.ico"))
        self.img_yt.setObjectName("img_yt")
        self.yt = QtWidgets.QLabel(self.desktop_icons)
        self.yt.setGeometry(QtCore.QRect(10, 440, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.yt.setFont(font)
        self.yt.setStyleSheet("color: #E2C2C6")
        self.yt.setAlignment(QtCore.Qt.AlignCenter)
        self.yt.setObjectName("yt")
        self.img_web = QtWidgets.QLabel(self.desktop_icons)
        self.img_web.setGeometry(QtCore.QRect(20, 110, 31, 31))
        self.img_web.setText("")
        self.img_web.setPixmap(QtGui.QPixmap("images/MSN Pink.ico"))
        self.img_web.setObjectName("img_web")
        self.web = QtWidgets.QLabel(self.desktop_icons)
        self.web.setGeometry(QtCore.QRect(20, 141, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.web.setFont(font)
        self.web.setStyleSheet("color: #E2C2C6")
        self.web.setAlignment(QtCore.Qt.AlignCenter)
        self.web.setObjectName("web")
        self.img_help = QtWidgets.QLabel(self.desktop_icons)
        self.img_help.setGeometry(QtCore.QRect(22, 208, 31, 31))
        self.img_help.setText("")
        self.img_help.setPixmap(QtGui.QPixmap("images/My Computer Pink.ico"))
        self.img_help.setObjectName("img_help")
        self.help = QtWidgets.QLabel(self.desktop_icons)
        self.help.setGeometry(QtCore.QRect(20, 240, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.help.setFont(font)
        self.help.setStyleSheet("color: #E2C2C6")
        self.help.setAlignment(QtCore.Qt.AlignCenter)
        self.help.setObjectName("help")
        self.img_credits = QtWidgets.QLabel(self.desktop_icons)
        self.img_credits.setGeometry(QtCore.QRect(21, 310, 31, 31))
        self.img_credits.setText("")
        self.img_credits.setPixmap(QtGui.QPixmap("images/Book 2 Pink.ico"))
        self.img_credits.setObjectName("img_credits")
        self.credits = QtWidgets.QLabel(self.desktop_icons)
        self.credits.setGeometry(QtCore.QRect(7, 340, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.credits.setFont(font)
        self.credits.setStyleSheet("color: #E2C2C6")
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.setObjectName("credits")
        self.garbage = QtWidgets.QLabel(self.desktop_icons)
        self.garbage.setGeometry(QtCore.QRect(8, 550, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.garbage.setFont(font)
        self.garbage.setStyleSheet("color: #E2C2C6")
        self.garbage.setAlignment(QtCore.Qt.AlignCenter)
        self.garbage.setObjectName("garbage")
        self.img_garbage = QtWidgets.QLabel(self.desktop_icons)
        self.img_garbage.setGeometry(QtCore.QRect(20, 520, 31, 31))
        self.img_garbage.setText("")
        self.img_garbage.setPixmap(QtGui.QPixmap("images/Empty Recycle Bin Pink.ico"))
        self.img_garbage.setObjectName("img_garbage")
        CuteTimer.setCentralWidget(self.centralwidget)

        self.retranslateUi(CuteTimer)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CuteTimer)

    def retranslateUi(self, CuteTimer):
        _translate = QtCore.QCoreApplication.translate
        CuteTimer.setWindowTitle(_translate("CuteTimer", "MainWindow"))
        self.Start.setText(_translate("CuteTimer", "Start"))
        self.Welcome.setText(_translate("CuteTimer", " Welcome"))
        self.currentTime.setText(_translate("CuteTimer", "10:00 AM"))
        self.currentTime_3.setText(_translate("CuteTimer", "10:00 AM"))
        self.appName.setText(_translate("CuteTimer", "Cute Timer"))
        self.appExit.setText(_translate("CuteTimer", "X"))
        self.welcome.setText(_translate("CuteTimer", "Cute\n"
"Timer"))
        self.startTime.setText(_translate("CuteTimer", "START A TIMER"))
        self.title_digital.setText(_translate("CuteTimer", "Choose Timer"))
        self.goal_digital.setText(_translate("CuteTimer", "00:00"))
        self.title_progress.setText(_translate("CuteTimer", "Choose Timer"))
        self.goal_progress.setText(_translate("CuteTimer", "0"))
        self.title_checkpoint.setText(_translate("CuteTimer", "Choose Timer"))
        self.goal_checkpoint.setText(_translate("CuteTimer", "0"))
        self.theme.setTitle(_translate("CuteTimer", "Theme"))
        self.pink.setText(_translate("CuteTimer", "Pink"))
        self.green.setText(_translate("CuteTimer", "Green"))
        self.grey.setText(_translate("CuteTimer", "Grey"))
        self.display.setTitle(_translate("CuteTimer", "Display"))
        self.digital.setText(_translate("CuteTimer", "Digital"))
        self.progress.setText(_translate("CuteTimer", "Progress"))
        self.checkpoint.setText(_translate("CuteTimer", "Checkpoint"))
        self.settings.setTitle(_translate("CuteTimer", "Settings"))
        self.sounds.setText(_translate("CuteTimer", "Alarm Sound"))
        self.stop.setText(_translate("CuteTimer", "Auto Stop"))
        self.icons.setText(_translate("CuteTimer", "Desktop Icons"))
        self.breaks.setText(_translate("CuteTimer", "Auto Breaks"))
        self.focus.setText(_translate("CuteTimer", "Auto Focus"))
        self.seamless.setText(_translate("CuteTimer", "Seamless"))
        self.listTimers.setItemText(0, _translate("CuteTimer", "Choose Your Timer!"))
        self.listTimers.setItemText(1, _translate("CuteTimer", "Focus Timer (15 minute increments)"))
        self.listTimers.setItemText(2, _translate("CuteTimer", "Pomodoro (25/5/10 minutes)"))
        self.listTimers.setItemText(3, _translate("CuteTimer", "Class (50 minute lecture)"))
        self.type.setText(_translate("CuteTimer", "Timer:"))
        self.less.setText(_translate("CuteTimer", "-15"))
        self.more.setText(_translate("CuteTimer", "+15"))
        self.start.setText(_translate("CuteTimer", "Start"))
        self.reset.setText(_translate("CuteTimer", "Reset"))
        self.setBreak.setText(_translate("CuteTimer", "Break"))
        self.label.setText(_translate("CuteTimer", "Cute Timer 2.0 - A simple, yet cute Windows 95 timer"))
        self.lofi.setText(_translate("CuteTimer", "lofi"))
        self.yt.setText(_translate("CuteTimer", "youtube"))
        self.web.setText(_translate("CuteTimer", "web"))
        self.help.setText(_translate("CuteTimer", "help"))
        self.credits.setText(_translate("CuteTimer", "credits"))
        self.garbage.setText(_translate("CuteTimer", "garbage"))
        CuteTimer.setFixedSize(900, 675)
        self.less.setEnabled(False)
        self.more.setEnabled(False)
        self.digital.setChecked(True)
        self.green.setEnabled(False)
        self.grey.setEnabled(False)
        self.focus.setCheckable(False)
        self.breaks.setCheckable(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CuteTimer = QtWidgets.QMainWindow()
    ui = Ui_CuteTimer()
    ui.setupUi(CuteTimer)
    CuteTimer.show()
    sys.exit(app.exec_())
