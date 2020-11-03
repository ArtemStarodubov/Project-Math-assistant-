import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Arithmetic_Progression_Theory(object):
    def setupUi(self, Eleventh):
        Eleventh.setObjectName("MainWindow")
        Eleventh.resize(733, 585)
        self.centralwidget = QtWidgets.QWidget(Eleventh)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 0, 271, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 671, 431))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 101, 41))
        self.pushButton.setObjectName("pushButton")
        Eleventh.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Eleventh)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        Eleventh.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Eleventh)
        self.statusbar.setObjectName("statusbar")
        Eleventh.setStatusBar(self.statusbar)

        self.retranslateUi(Eleventh)
        QtCore.QMetaObject.connectSlotsByName(Eleventh)

    def retranslateUi(self, Eleventh):
        _translate = QtCore.QCoreApplication.translate
        Eleventh.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Арифметическая прогрессия</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">Последовательность, в которой каждый следующий член можно найти,</span></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">прибавив к предыдущему одно и то же число </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#ff0000; background-color:#ffffff;\">d</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">,</span></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">называется </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#ff0000; background-color:#ffffff;\">арифметической прогрессией</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">.</span></p><p><br/></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">Число </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#ff0000; background-color:#ffffff;\">d</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> называется </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#ff0000; background-color:#ffffff;\">разностью</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> арифметической прогрессии.</span></p><p><br/></p><p align=\"center\"><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">n</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> = a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> + (n - 1) * d,</span></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">где n </span><span style=\" font-family:\'Open Sans\'; font-size:16px; color:#4e4e3f; background-color:#ffffff;\">— </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:600; color:#4e4e3f; background-color:#ffffff;\">порядковый номер члена прогрессии, a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:600; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'Open Sans\'; font-size:16px; color:#4e4e3f; background-color:#ffffff;\">—</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:600; color:#4e4e3f; background-color:#ffffff;\"> первый член прогрессии,</span></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:600; color:#4e4e3f; background-color:#ffffff;\">d </span><span style=\" font-family:\'Open Sans\'; font-size:16px; color:#4e4e3f; background-color:#ffffff;\">— </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:600; color:#4e4e3f; background-color:#ffffff;\">разность.</span></p><p><br/></p><p><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">Сумма членов геометрической прогрессии:</span></p><p><br/></p><p align=\"center\"><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">S</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">n</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> = (a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">1 </span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">+ a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">n</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\">)/2 * n     или     S</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">n</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> = (2a</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'Open Sans\'; font-size:16px; font-weight:696; color:#4e4e3f; background-color:#ffffff;\"> + d(n - 1))/2 * n</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))

class Arithmetic_Progression_Theory(QMainWindow, Ui_Arithmetic_Progression_Theory):
    def __init__(self, parent=None):
        super(Arithmetic_Progression_Theory, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.close)

    def close(self):
        self.hide()


class Ui_Arithmetic_Progression(object):
    def setupUi(self, FifthWindow):
        FifthWindow.setObjectName("MainWindow")
        FifthWindow.resize(421, 262)
        self.centralwidget = QtWidgets.QWidget(FifthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 311, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 60, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 180, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 180, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        FifthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FifthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        FifthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FifthWindow)
        self.statusbar.setObjectName("statusbar")
        FifthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FifthWindow)
        QtCore.QMetaObject.connectSlotsByName(FifthWindow)

    def retranslateUi(self, FifthWindow):
        _translate = QtCore.QCoreApplication.translate
        FifthWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\""
                                                         " font-size:12pt; font-weight:600;\""
                                                         ">Выберете необходимую величину:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\""
                                                    " font-size:12pt; font-weight:600;\">Выберете небоходимую величину"
                                                    ":</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "N-ный член"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Сумма"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать"))
        self.pushButton_2.setText(_translate("MainWindow", "Теория"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))


class Ui_N_Member(object):
    def setupUi(self, SixthWindow):
        SixthWindow.setObjectName("MainWindow")
        SixthWindow.resize(477, 343)
        self.centralwidget = QtWidgets.QWidget(SixthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 181, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 141, 221))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 200, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 181, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 300, 113, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 285, 80, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        SixthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SixthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        SixthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SixthWindow)
        self.statusbar.setObjectName("statusbar")
        SixthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SixthWindow)
        QtCore.QMetaObject.connectSlotsByName(SixthWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\""
                                                    ">Введите данные:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Первый член прогрессии:</p><p><br/></p><p>"
                                                      "Номер члена:</p><p><br/></p><p>Разность прогрессии:</p><p><br/>"
                                                      "</p><p>""<span style=\" font-size:12pt;\">Ответ:<br/></span></p>"
                                                      "</body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))


class Ui_Arithmetic_Sum(object):
    def setupUi(self, SeventhWindow):
        SeventhWindow.setObjectName("MainWindow")
        SeventhWindow.resize(642, 577)
        self.centralwidget = QtWidgets.QWidget(SeventhWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 301, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 121, 271))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 380, 371, 101))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 480, 161, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 110, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 190, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 260, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 330, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(484, 470, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 490, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        SeventhWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SeventhWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        SeventhWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SeventhWindow)
        self.statusbar.setObjectName("statusbar")
        SeventhWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SeventhWindow)
        QtCore.QMetaObject.connectSlotsByName(SeventhWindow)

    def retranslateUi(self, SeventhWindow):
        _translate = QtCore.QCoreApplication.translate
        SeventhWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Сумма n-членов прогрессии</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Первый член:</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\">n-ный член*:</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\">n:</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\">Разность:</span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">*Если неизвестен n-ный член, ничего не вводите.</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))


class N_Member(QMainWindow, Ui_N_Member):
    def __init__(self, parent=None):
        super(N_Member, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.calculation)
        self.pushButton_2.clicked.connect(self.close)

    def calculation(self):
        self.first = self.lineEdit.text()
        self.n = self.lineEdit_2.text()
        self.d = self.lineEdit_3.text()
        Thepossiblecharacters = '.-0123456789'
        for i in self.first:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_3.setText('Неверно введённые данные.')
                    return
        for i in self.n:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_3.setText('Неверно введённые данные.')
                    return

        for i in self.d:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_3.setText('Неверно введённые данные.')
                    return
        if self.first == '' or self.n == '' or self.d == '':
            self.label_3.setText('Неверно введённые данные.')
            return

        self.member = float(self.first) + (float(self.n) - 1) * float(self.d)
        self.label_3.setText(f'{self.member}')

    def close(self):
        self.hide()

class Arithmetic_Sum(QMainWindow, Ui_Arithmetic_Sum):
    def __init__(self, parent=None):
        super(Arithmetic_Sum, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.calculation1)
        self.pushButton_2.clicked.connect(self.close)

    def calculation1(self):
        self.first = self.lineEdit.text()
        self.n_member = self.lineEdit_2.text()
        self.n = self.lineEdit_3.text()
        self.d = self.lineEdit_4.text()

        Thepossiblecharacters = '.-0123456789'
        for i in self.first:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_4.setText('Неверно введённые данные.')
                    return
        for i in self.n:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_4.setText('Неверно введённые данные.')
                    return

        for i in self.d:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_4.setText('Неверно введённые данные.')
                    return
        for i in self.n_member:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_4.setText('Неверно введённые данные.')
                    return

        if self.first == '' or self.n == '' or (self.n_member == '' and self.d == ""):
            self.label_4.setText('Неверно введённые данные.')
            return
        if self.d == '':  # Нахождение суммы n-членов арифметической прогрессии
            self.summ = (float(self.first) + float(self.n_member)) / 2 * float(self.n)
            self.label_4.setText(f'Ответ:{self.summ}.')
        else:
            self.summ = (float(self.first) * 2 + (int(self.n) - 1) * float(self.d)) / 2 * float(self.n)
            self.label_4.setText(f'Ответ:{self.summ}.')

    def close(self):
        self.hide()



class Arithmetic_Progression(QMainWindow, Ui_Arithmetic_Progression):
    def __init__(self, parent=None):
        super(Arithmetic_Progression, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.arifhmetic_theory)
        self.pushButton_3.clicked.connect(self.close)

    def choose(self):
        if self.comboBox.currentText() == "N-ный член":
            self.ex5 = N_Member()
            self.ex5.show()
        else:
            self.ex6 = Arithmetic_Sum()
            self.ex6.show()

    def arifhmetic_theory(self):
        self.ex11 = Arithmetic_Progression_Theory()
        self.ex11.show()

    def close(self):
        self.hide()
