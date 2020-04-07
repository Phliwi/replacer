# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R:\Python\Project\Test_Files\test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 258)
        Dialog.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"width: 75px;\n"
"height: 50px;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"border: none;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: blue;\n"
"}\n"
"")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 30, 160, 166))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(37, 30, 211, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FormatBankClient"))
        self.pushButton_2.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_3.setText(_translate("Dialog", "Форматировать"))
        self.pushButton.setText(_translate("Dialog", "Выбрать файл"))
        self.label.setText(_translate("Dialog", "Название файла"))
