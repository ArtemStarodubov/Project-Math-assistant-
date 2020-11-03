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


class Ui_Pythagorean_Theorem_Theory(object):
    def setupUi(self, TenthWindow):
        TenthWindow.setObjectName("MainWindow")
        TenthWindow.resize(794, 267)
        self.centralwidget = QtWidgets.QWidget(TenthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 11, 781, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 170, 101, 51))
        self.pushButton.setObjectName("pushButton")
        TenthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TenthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        TenthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TenthWindow)
        self.statusbar.setObjectName("statusbar")
        TenthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TenthWindow)
        QtCore.QMetaObject.connectSlotsByName(TenthWindow)

    def retranslateUi(self, TenthWindow):
        _translate = QtCore.QCoreApplication.translate
        TenthWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Теорема Пифагора:</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">c</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> = a</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> + b</span><span style=\" font-size:12pt; vertical-align:super;\">2</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; vertical-align:super;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Формула для нахождения гипотенузы: c = √(a</span><span style=\" font-size:12pt; vertical-align:super;\">2 </span><span style=\" font-size:12pt;\">+ b</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\">)</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Формула для нахождения катета: a = √(c</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> - b</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\">)</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                                </span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Open Sans\'; font-size:8pt; color:#4e4e3f;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))

class Pythagorean_Theorem_Theory(QMainWindow, Ui_Pythagorean_Theorem_Theory):
    def __init__(self, parent=None):
        super(Pythagorean_Theorem_Theory, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.close)

    def close(self):
        self.hide()


class Ui_Pythagorean_Theorem(object):
    def setupUi(self, FourthWindow):
        FourthWindow.setObjectName("MainWindow")
        FourthWindow.resize(800, 450)
        self.centralwidget = QtWidgets.QWidget(FourthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 571, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 181, 81))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(260, 100, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 171, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 171, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 220, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 170, 361, 41))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 370, 471, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 280, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 350, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 360, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        FourthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FourthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FourthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FourthWindow)
        self.statusbar.setObjectName("statusbar")
        FourthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FourthWindow)
        QtCore.QMetaObject.connectSlotsByName(FourthWindow)

    def retranslateUi(self, FourthWindow):
        _translate = QtCore.QCoreApplication.translate
        FourthWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Нахождение сторон прямоугольного треугольника</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Необходимо найти:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Гипотенуза"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Катет"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Длина стороны 1*:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Длина стороны 2:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">*Порядок введения значения длин сторон не имеет значения.</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.pushButton_2.setText(_translate("MainWindow", "ТЕОРИЯ"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))



class Pythagorean_Theorem(QMainWindow, Ui_Pythagorean_Theorem):
    def __init__(self, parent=None):
        super(Pythagorean_Theorem, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.Pythagorean_theorem)
        self.pushButton_2.clicked.connect(self.Pythagorean_theorem_theory)
        self.pushButton_3.clicked.connect(self.close)

    def Pythagorean_theorem(self):
        self.necessary_side = self.comboBox.currentText()
        self.side1 = self.lineEdit.text()
        self.side2 = self.lineEdit_2.text()
        Thepossiblecharacters = '.0123456789'
        if self.side1 == '' or self.side2 == '' or not self.necessary_side:  # Проверка записи данных
            self.label_5.setText('Неверно введённые данные.')
            return
        for i in self.side1:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_5.setText('Неверно введённые данные.')
                    return
        for i in self.side2:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_5.setText('Неверно введённые данные.')
                    return
        if self.necessary_side == 'Катет' and self.side2 == self.side1:  # Проверка записи данных
            self.label_5.setText('Неверно введённые данные.')
            return

        if self.necessary_side == 'Гипотенуза':  # Нахождение длины гипотенузы
            self.hypotenuse = (float(self.side1) ** 2 + float(self.side2) ** 2) ** 0.5
            self.label_5.setText(f'Ответ: гипотенуза = {self.hypotenuse}.')
        else:  # Нахождение длины катета
            if float(self.side1) > float(self.side2):
                self.hypotenuse = float(self.side1)
                self.cathetus = float(self.side2)
            else:
                self.hypotenuse = float(self.side2)
                self.cathetus = float(self.side1)

            self.cathetus1 = (self.hypotenuse ** 2 - self.cathetus ** 2) ** 0.5
            self.label_5.setText(f'Ответ: катет = {self.cathetus1}.')

    def Pythagorean_theorem_theory(self):
        self.ex10 = Pythagorean_Theorem_Theory()
        self.ex10.show()

    def close(self):
        self.hide()


class Ui_Solution_of_Equation_Theory(object):
    def setupUi(self, NinthWindow):
        NinthWindow.setObjectName("MainWindow")
        NinthWindow.resize(796, 497)
        self.centralwidget = QtWidgets.QWidget(NinthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 781, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 400, 101, 41))
        self.pushButton.setObjectName("pushButton")
        NinthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NinthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        NinthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NinthWindow)
        self.statusbar.setObjectName("statusbar")
        NinthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NinthWindow)
        QtCore.QMetaObject.connectSlotsByName(NinthWindow)

    def retranslateUi(self, NinthWindow):
        _translate = QtCore.QCoreApplication.translate
        NinthWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Алгоритм решения квадратного уравнения:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) Раскрыть скобки, перенести все слагаемые в левую часть, чтобы уравнение приняло вид:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ax</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> + bx + c = 0</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2) Выписать, чему равны в числах коэффициенты a, b и c</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3) Вычислить дискриминант по формуле:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">D = b</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> - 4ac</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">4) Если D&gt;0, будет два различных корня, которые находятся по формулам:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">x</span><span style=\" font-size:12pt; vertical-align:sub;\">1 </span><span style=\" font-size:12pt;\">= (-b - √D)/2a и x</span><span style=\" font-size:12pt; vertical-align:sub;\">2</span><span style=\" font-size:12pt;\"> = (-b + √D)/2a</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">5) Если D=0, будет один корень, который находится по формуле:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">x=-b/2a</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">6) Если D&lt;0, решений нет.</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))


class Solution_of_Equation_Theory(QMainWindow, Ui_Solution_of_Equation_Theory):
    def __init__(self, parent=None):
        super(Solution_of_Equation_Theory, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.close)

    def close(self):
        self.hide()


class Ui_Solution_of_Equation(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("MainWindow")
        ThirdWindow.resize(800, 481)
        self.centralwidget = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 471, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 321, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 220, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 220, 41, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 220, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 220, 47, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 220, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(536, 220, 61, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 330, 91, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 330, 311, 31))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(284, 400, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 370, 131, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 390, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        ThirdWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThirdWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ThirdWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThirdWindow)
        self.statusbar.setObjectName("statusbar")
        ThirdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Решение квадратных уравнений</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Введите коэффициенты уравнения</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">x</span><span style=\" font-size:14pt; vertical-align:super;\">2  </span><span style=\" font-size:14pt;\">+</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">x +</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">= 0</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Ответ:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Решить"))
        self.pushButton_2.setText(_translate("MainWindow", "ТЕОРИЯ"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))


class Solution_of_Equation(QMainWindow, Ui_Solution_of_Equation):
    def __init__(self, parent=None):
        super(Solution_of_Equation, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.solution_of_equation)
        self.pushButton_2.clicked.connect(self.solution_of_equation_theory)
        self.pushButton_3.clicked.connect(self.close)

    def solution_of_equation(self):
        self.a = self.lineEdit.text()
        self.b = self.lineEdit_2.text()
        self.c = self.lineEdit_3.text()
        Thepossiblecharacters = '-.0123456789'
        if self.a == '' or self.b == '' or self.c == '':  # Проверка записи данных
            self.label_7.setText('Неверно введённые данные.')
            return
        for i in self.a:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_7.setText('Неверно введённые данные.')
                    return

        for i in self.b:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_7.setText('Неверно введённые данные.')
                    return

        for i in self.c:  # Проверка записи данных
            for y in i.split():
                if y not in Thepossiblecharacters:
                    self.label_7.setText('Неверно введённые данные.')
                    return
        # Если данные записаны верно, алгоритм находит корни уравнения.
        self.a, self.b, self.c = int(self.a), int(self.b), int(self.c)
        if self.a == 0 and self.b == 0 and self.c == 0:
            self.label_7.setText('Уравнение имеет бесконечное множество решений.')
        elif self.a == 0 and self.b == 0:
            self.label_7.setText('Уравнение не имеет решений.')
        elif self.a == 0:
            x = (self.c * (-1)) / self.b
            self.label_7.setText(f'{x}.')
        elif self.b == 0:
            x = math.sqrt((-1 * self.b) / self.a)
            self.label_7.setText(f'{x}.')
        elif self.c == 0:
            x = (-1 * self.b) / self.a
            self.label_7.setText(f'x = 0,x = {x}.')
        else:  # Решение полного квадратного уравнения
            discriminate = self.b ** 2 + (-4 * self.a * self.c)
            if discriminate < 0:
                self.label_7.setText('Уравнение не имеет решений; дискриминант меньше 0.')
            elif discriminate == 0:
                x = (-1 * self.b) / (2 * self.a)
                self.label_7.setText(f'x = {x}.')
            else:
                discriminate = math.sqrt(discriminate)
                x1 = ((-1 * self.b) - discriminate) / (2 * self.a)
                x2 = ((-1 * self.b) + discriminate) / (2 * self.a)
                self.label_7.setText(f'x = {x1}, {x2}.')

    def solution_of_equation_theory(self):
        self.ex9 = Solution_of_Equation_Theory()
        self.ex9.show()

    def close(self):
        self.hide()


class Ui_Convert_Numbers_Theory(object):
    def setupUi(self, EighthWindow):
        EighthWindow.setObjectName("MainWindow")
        EighthWindow.resize(802, 660)
        self.centralwidget = QtWidgets.QWidget(EighthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 1, 801, 621))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 570, 121, 41))
        self.pushButton.setObjectName("pushButton")
        EighthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EighthWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        EighthWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EighthWindow)
        self.statusbar.setObjectName("statusbar")
        EighthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EighthWindow)
        QtCore.QMetaObject.connectSlotsByName(EighthWindow)

    def retranslateUi(self, EighthWindow):
        _translate = QtCore.QCoreApplication.translate
        EighthWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">Для перевода числа в систему счисления, бОльшим основанием, необходимо его записать в виде многочлена, состоящего из произведений цифр числа и соответствующей степени числа, совпадающего с основанием исходной системы счисления, и вычислить по правилам десятичной арифметики:</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">X</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">z</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> = A</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">n </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">*  z</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">n-1 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">+ A</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">n-1 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">* z</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">n-2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + A</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">n-2 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">* z</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">n-3 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">+ ... + A</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> * z</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">0</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\"><br /></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">Пример : Число из двоичной системы счисления</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242;\"> перевести в десятичную систему счисления.</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">11101000</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> = 1 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">7</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + 1 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">6</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + 1 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">5 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">+ 0 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">4</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + 1 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">3</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + 0 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">2 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> + 0 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">1 </span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">+ 0 * 2</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:super;\">0</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> = 232</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">10</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\"><br /></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">Для перевода  числа в систему,  с меньшим основанием,   его необходимо последовательно делить на основание конечной системы счисления до тех пор, пока не останется остаток, меньший или равный 1.  Полученное число записывается как последовательность последнего результата деления и остатков от деления в обратном порядке.</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\"><br /></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">Пример: Переведем десятичное число 672 в восьмеричную систему счисления.</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">672 : 8 = 84 (0)</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">84 : 8 = 10 (4)</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">10 : 8 = 1 (2)</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">8 : 8 = 1</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">672</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">10</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\"> = 1240</span><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\">8</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff; vertical-align:sub;\"><br /></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">Для системы счисления, с основанием больше 10:</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">A-10   C-12   E-14</span></p>\n"
                                            "<p style=\" margin-top:8px; margin-bottom:8px; margin-left:8px; margin-right:30px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Verdana\'; font-size:12pt; color:#424242; background-color:#ffffff;\">B-11   D-13   F-15</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))


class Convert_Numbers_Theory(QMainWindow, Ui_Convert_Numbers_Theory):
    def __init__(self, parent=None):
        super(Convert_Numbers_Theory, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.pushButton.clicked.connect(self.close)

    def close(self):
        self.hide()


class Ui_Convert_Numbers(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("MainWindow")
        SecondWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 470, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 351, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 81, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 140, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(306, 140, 311, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 180, 411, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 370, 621, 81))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(620, 140, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 190, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 340, 501, 16))
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 260, 461, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 500, 141, 51))
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 500, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ПЕРЕВЕСТИ"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Переводчик систем счисления*</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Число**</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">в системе счисления с основанием</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">перевести в систему счисления с основанием</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">**Важно помнить, что в записи числа ни одна цифра не должна</span></p><p><span style=\" font-size:14pt; font-style:italic;\">быть больше основания исходной системы счисления.</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "5"))
        self.comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox.setItemText(4, _translate("MainWindow", "10"))
        self.comboBox.setItemText(5, _translate("MainWindow", "16"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "10"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "16"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-style:italic;\">*Число должно быть целым.</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Теория"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))


class Convert_Numbers(QMainWindow, Ui_Convert_Numbers):
    def __init__(self, parent=None):
        super(Convert_Numbers, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(' ')
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 260, 461, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton.clicked.connect(self.convert_numbers)
        self.pushButton_2.clicked.connect(self.convert_numbers_theory)
        self.pushButton_3.clicked.connect(self.close)

    def convert_numbers(self):  # функция перевода чисел
        self.number = self.lineEdit.text()
        self.from_base = int(self.comboBox.currentText())
        self.to_base = int(self.comboBox_2.currentText())
        alphabet = {2: '01', 3: '012', 5: '01234', 8: '01234567',
                    10: '0123456789', 16: '0123456789ABCDEF'}
        NUMBER = self.number
        flag = True  # проверка записи числа
        for i in str(self.number):
            for y in i:
                if y not in alphabet[self.from_base]:
                    flag = False

        if flag == False:
            self.textBrowser.setText('Ошибка, неверно введено число.')
            return

        if self.from_base == self.to_base:
            self.textBrowser.setText(self.number)
            return

        if self.from_base != 10:  # перевод в десятичную систему
            if self.from_base < 10:
                k, Num10 = 1, 0
                while NUMBER != 0:
                    NUMBER = int(NUMBER)
                    Num10 = Num10 + (NUMBER % 10) * k
                    k = k * self.from_base
                    NUMBER = NUMBER // 10
            else:
                Num10 = int(NUMBER, 16)
        else:
            Num10 = NUMBER

        if self.to_base == 10:
            self.textBrowser.setText(str(Num10))
        else:  # перевод из десятичной системы
            if self.to_base < 10:
                total_num, k = 0, 1
                while True:
                    if Num10 == 0:
                        break
                    else:
                        Num10 = int(Num10)
                        total_num += (Num10 % self.to_base) * int(k)
                        k *= 10
                        Num10 = Num10 // self.to_base
                    self.textBrowser.setText(str(total_num))
            if self.to_base == 16:
                Num10 = int(Num10)
                alphabet1 = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                             10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
                total_num = ""
                while Num10 != 0:
                    k = Num10 % 16
                    Num10 = Num10 // 16
                    total_num += alphabet1[k]
                total_num = ''.join(reversed(total_num))
                self.textBrowser.setText(str(total_num))

    def convert_numbers_theory(self):
        self.ex8 = Convert_Numbers_Theory()
        self.ex8.show()

    def close(self):
        self.hide()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Меню")
        MainWindow.resize(543, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 331, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 261, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 80, 251, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 130, 141, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\""
                                                    " font-size:18pt; font-style:italic;\""
                                                    ">Математический помощник</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\""
                                                      ">Выберете одну из программ:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Переводчик систем счисления"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Решение квадратных уравнений"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Нахождение сторон  прямоугольного треугольника"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Арифметическая прогрессия"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))


class All_programs(QMainWindow, Ui_MainWindow):  # Класс главного меню
    def __init__(self):
        super(All_programs, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.menu)

    def menu(self):
        self.necessary_task = self.comboBox.currentText()
        if self.necessary_task == "Переводчик систем счисления":
            self.ex = Convert_Numbers()
            self.ex.show()
        elif self.necessary_task == "Решение квадратных уравнений":
            self.ex1 = Solution_of_Equation()
            self.ex1.show()
        elif self.necessary_task == "Нахождение сторон  прямоугольного треугольника":
            self.ex2 = Pythagorean_Theorem()
            self.ex2.show()
        else:
            self.ex3 = Arithmetic_Progression()
            self.ex3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = All_programs()
    ex.show()
    sys.exit(app.exec_())
