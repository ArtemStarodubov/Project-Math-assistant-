import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets


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
