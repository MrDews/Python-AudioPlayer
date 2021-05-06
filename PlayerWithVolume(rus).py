from PyQt5 import (
    QtCore,
    QtGui,
    QtWidgets,
)  # Библиотеки, необходимы для коректной работы программы
import os, random
from os import path
from tkinter import filedialog
from tkinter import *
from pygame import mixer
import pygame

# Класс, в котором иницилизируется окно, созданное в QDesigner
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


# Основная точка входа метода
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
# Константы, необходимые для корректной работы программы
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


# Метод, отвечающий за создания списка в плейлисте
def browse_button():
    global filename, s, count
    s = []  # Создание пустого списка
    ui.listWidget.clear()  # Очищение выводимого списка
    root = Tk()  # Функция, требуемая для указания пути
    filename = filedialog.askdirectory()  # переменная пути
    for image in sorted(os.listdir(filename)):  # Цикл, выводящий музыку на экран
        if (
            (image.endswith(".mp3"))
            or (image.endswith(".wav"))
            or (image.endswith(".ogg"))
            or (image.endswith(".m4a"))
        ):
            ui.listWidget.addItem(image)
            s.append(image)
            count = count + 1
    root.destroy()  # Уничтожение окна, отвечающий за выбор пути
    return filename, s


# Метод, предназначенный для рандомизации списка
def rand():
    global s, n, i
    i = 0
    ui.listWidget.clear()  # Очищение списка
    k = []  # Пустой список
    # Список песен
    while len(s) > 0:
        choizen = random.choice(s)  # Выбор случайной песни из списка s
        s.remove(choizen)  # Удаление данной песни из списка s
        k.append(choizen)  # Добавление данной списки в список k
    for x in k:
        ui.listWidget.addItem(x)  # Вывод элементов списка k
        n.append(x)
    s = n[:]  # Клонирование списка, во избежание потерь данных
    n[:] = []
    mixer.music.stop()  # остановка песни, и воспроизведение нового списка
    play()


# Метод, предназначенный за вкл/выкл плеера
def sostoyanya():
    global CheckParamert
    if CheckParamert == False:
        # Показ кнопок
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
        # Скрытие кнопок
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


# Метод, воспроизведения музыки
def play():
    global i, filename, count, rightNow
    if (i > count - 1) or (
        i < 0
    ):  # Условие, во избежание выхода из области значений списка
        ui.textBrowser.clear()  # Очистка выводимого поля текущего трека
        ui.textBrowser.append("Музыка закончилась")
        i = 0
        mixer.music.stop()  # Остановка музыки
        return
    else:
        ui.textBrowser.clear()
        p = (
            filename + "/" + s[i]
        )  # Переменная, для упрощённой работы с воспроизведением
        ui.textBrowser.append("Сейчас играет: " + s[i])  # Вывод текущего трека
        mixer.init()  # Иницилизация плагина музыки
        mixer.music.load(p)  # Загрузка музыки
        mixer.music.play()  # Воспроизведение
        rightNow = 1


# Метод, для переключения музыки на следующую
def next():
    global i
    i = i + 1
    play()


# Метод паузы музыки
def pause():
    global rightNow, pause
    if pause == False:  # Проверка, если музыка выключена, пауза не работает
        pause = True
        rightNow = 0
        mixer.music.pause()
        ui.pushButton_7.setText("Unpause")
    else:
        pause = False
        rightNow = 1
        mixer.music.unpause()
        ui.pushButton_7.setText("Pause")


# Метод, для переключения музыки на предыдущую
def prev():
    global i
    i = i - 1
    play()


# Метод, полной остановки музыки
def stop():
    global rightNow
    rightNow = 0
    mixer.music.stop()


# Метод, для настройки громкости
def volume():
    global rightNow
    if rightNow == 1:  # работает, только тогда, когда
        value = ui.dial.value()  # Берет значение из ползунка
        pygame.mixer.music.set_volume(value / 10)  # Выставляет громкость


# Основные плюшечки, настроечки, и т.д (Мне уже лень расписывать)
mixer.init()
mixer.music.set_volume(0.1)
ui.dial.setMinimum(0)
ui.dial.setMaximum(10)
ui.dial.setRange(0, 10)
ui.dial.setSingleStep(1)
ui.dial.setValue(1)
# Ну тут уже короче жмёшь, и оно включается
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
# ВООО, а вот тут выход, на крестик и на кнопку exit
ui.pushButton_8.clicked.connect(sys.exit)
sys.exit(app.exec_())
