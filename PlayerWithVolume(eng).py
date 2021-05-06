from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
)  # library, for connect work 
import os, random
from os import path
from tkinter import filedialog
from tkinter import *
from pygame import mixer
import pygame

# The class in which the window created in QDesigner is initialized
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 681, 164))
        self.listWidget.setStyleSheet(
            "QPushButton {\n" "background-color:rgb(0,203,150)\n" "}"
        )
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 210, 681, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(650, 0, 41, 41))
        self.dial.setObjectName("dial")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 644, 25))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(114, 255, 234);\n"
            "color: brown;\n"
            "font: Tahoma,sans-serif italic 10px;\n"
            "}"
        )
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 5, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 6, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setStyleSheet(
            "QPushButton {\n"
            "background-color:rgb(150, 230, 45);\n"
            "color: white;\n"
            "font: Tahoma,sans-serif italic 18px;\n"
            "}"
        )
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Кнопка включения/выключения</p></body></html>",
            )
        )
        self.pushButton.setText(_translate("MainWindow", "On/Off"))
        self.pushButton_2.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Кнопка для воспроизведения песен</p></body></html>",
            )
        )
        self.pushButton_2.setText(_translate("MainWindow", "Play"))
        self.pushButton_3.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Кнопка для случайного воспроизведения</p></body></html>",
            )
        )
        self.pushButton_3.setText(_translate("MainWindow", "Rand"))
        self.pushButton_6.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Включить предыдущую песню</p></body></html>",
            )
        )
        self.pushButton_6.setText(_translate("MainWindow", "Prev"))
        self.pushButton_5.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Включить следующую песню</p></body></html>",
            )
        )
        self.pushButton_5.setText(_translate("MainWindow", "Next"))
        self.pushButton_4.setToolTip(
            _translate(
                "MainWindow", "<html><head/><body><p>Остановить песни</p></body></html>"
            )
        )
        self.pushButton_4.setText(_translate("MainWindow", "Stop"))
        self.pushButton_7.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Поставить песню на паузу</p></body></html>",
            )
        )
        self.pushButton_7.setText(_translate("MainWindow", "Pause"))
        self.pushButton_8.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Выключение программы</p></body></html>",
            )
        )
        self.pushButton_8.setText(_translate("MainWindow", "Exit"))


# Start of program
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
# Constant, need to works
CheckParamert = True
filename = ""
ui.listWidget.setAcceptDrops(True)
ui.listWidget.setDragEnabled(True)
s = []
n = []
i = 0
count = 0
rightNow = 0
Pause = False


# A method for creating playlist
def browse_button():
    global filename, s, count
    s = []  # create empty list
    ui.listWidget.clear()  # clear input list (if program gonna be change playlist in future)
    root = Tk()  # function, work to set ur path
    filename = filedialog.askdirectory()  # variable of path
    for image in sorted(os.listdir(filename)):  # A loop that outputs music to the screen
        if (
            (image.endswith(".mp3"))
            or (image.endswith(".wav"))
            or (image.endswith(".ogg"))
            or (image.endswith(".m4a"))
        ):
            ui.listWidget.addItem(image)
            s.append(image)
            count = count + 1
    root.destroy()  # Destroying the window responsible for selecting the path
    return filename, s


# A method designed to randomize a list
def rand():
    global s, n, i
    i = 0
    ui.listWidget.clear()  # clear list
    k = []  # empty list
    # Song list
    while len(s) > 0:
        choizen = random.choice(s)  # Selecting a random song from the s list
        s.remove(choizen)  # Deleting a given song from the s list
        k.append(choizen)  # Adding a given list to the k list
    for x in k:
        ui.listWidget.addItem(x)  # Output of k list items
        n.append(x)
    s = n[:]  # Cloning the list to avoid data loss
    n[:] = []
    mixer.music.stop()  # stop the song, and play a new list
    play()


# Method intended for on / off of the player
def sostoyanya():
    global CheckParamert
    if CheckParamert == False:
        # show puttons
        ui.pushButton_2.show()
        ui.pushButton_3.show()
        ui.pushButton_4.show()
        ui.pushButton_5.show()
        ui.pushButton_6.show()
        ui.pushButton_7.show()
        ui.textBrowser.show()
        ui.listWidget.show()
        CheckParamert = True
    else:
        # hide buttons
        mixer.music.stop()
        ui.listWidget.hide()
        ui.pushButton_2.hide()
        ui.pushButton_3.hide()
        ui.pushButton_4.hide()
        ui.pushButton_5.hide()
        ui.pushButton_6.hide()
        ui.pushButton_7.hide()
        ui.textBrowser.hide()
        CheckParamert = False
    return CheckParamert


# Method, music playback
def play():
    global i, filename, count, rightNow
    if (i > count - 1) or (
        i < 0
    ):  # Condition to avoid leaving the list value area
        ui.textBrowser.clear()  # Clearing the output field of the current track
        ui.textBrowser.append("Song end")
        i = 0
        mixer.music.stop()  # Stopping Music
        return
    else:
        ui.textBrowser.clear()
        p = (
            filename + "/" + s[i]
        )  # Variable, for simplified playback operation
        ui.textBrowser.append("Now playing: " + s[i])  # show currect track
        mixer.init()  # Initializing the music plugin
        mixer.music.load(p)  # Load music inside program
        mixer.music.play()  # Play music
        rightNow = 1


# Method for switching music to the next one
def next():
    global i
    i = i + 1
    play()


# Music pause method
def pause():
    global rightNow, pause
    if pause == False:  # Checking if the music is turned off, the pause does not work (it seems to work and it seems not)
        pause = True
        rightNow = 0
        mixer.music.pause()
        ui.pushButton_7.setText("Unpause")
    else:
        pause = False
        rightNow = 1
        mixer.music.unpause()
        ui.pushButton_7.setText("Pause")


# Method for switching music to the previous one
def prev():
    global i
    i = i - 1
    play()


# Method, stop the music completely
def stop():
    global rightNow
    rightNow = 0
    mixer.music.stop()


# Method for setting the volume
def volume():
    global rightNow
    if rightNow == 1:  # works only when the music works
        value = ui.dial.value()  # Takes the value from the slider
        pygame.mixer.music.set_volume(value / 10)  # Set volume


# Settings for currect work
mixer.init()
mixer.music.set_volume(0.1)
ui.dial.setMinimum(0)
ui.dial.setMaximum(10)
ui.dial.setRange(0, 10)
ui.dial.setSingleStep(1)
ui.dial.setValue(1)
# push button to method
ui.dial.valueChanged.connect(lambda: volume())
ui.listWidget.clicked.connect(browse_button)
ui.pushButton_2.clicked.connect(play)
ui.pushButton_3.clicked.connect(rand)
ui.pushButton_4.clicked.connect(stop)
ui.pushButton_5.clicked.connect(next)
ui.pushButton_6.clicked.connect(prev)
ui.pushButton_7.clicked.connect(pause)
browse_button()
ui.pushButton.clicked.connect(sostoyanya)
# Exit from program
ui.pushButton_8.clicked.connect(sys.exit)
sys.exit(app.exec_())
