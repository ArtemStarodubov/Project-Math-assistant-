import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets


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
