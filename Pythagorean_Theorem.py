import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets


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
