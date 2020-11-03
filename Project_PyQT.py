import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
from Convert_Numbers import *
from Solution_of_Equation import *
from Pythagorean_Theorem import *
from Arithmetic_Progression import *


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
