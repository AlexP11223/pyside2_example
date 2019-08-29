# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui',
# licensing of 'window.ui' applies.
#
# Created: Thu Aug 29 21:57:43 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MyAppWindow(object):
    def setupUi(self, MyAppWindow):
        MyAppWindow.setObjectName("MyAppWindow")
        MyAppWindow.resize(769, 548)
        MyAppWindow.setStyleSheet("* {\n"
"  font: 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton {\n"
"  font-size: 14pt;\n"
"  padding: 5px 25px;\n"
"}\n"
"\n"
"#txtMessages {\n"
"  font-size: 24pt;\n"
"  font-family: \"Segoe UI Symbol\";\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(MyAppWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtMessages = QtWidgets.QTextEdit(MyAppWindow)
        self.txtMessages.setObjectName("txtMessages")
        self.verticalLayout.addWidget(self.txtMessages)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnHello = QtWidgets.QPushButton(MyAppWindow)
        self.btnHello.setObjectName("btnHello")
        self.horizontalLayout.addWidget(self.btnHello)
        self.edtName = QtWidgets.QLineEdit(MyAppWindow)
        self.edtName.setObjectName("edtName")
        self.horizontalLayout.addWidget(self.edtName)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnDraw = QtWidgets.QPushButton(MyAppWindow)
        self.btnDraw.setObjectName("btnDraw")
        self.horizontalLayout.addWidget(self.btnDraw)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MyAppWindow)
        QtCore.QMetaObject.connectSlotsByName(MyAppWindow)

    def retranslateUi(self, MyAppWindow):
        MyAppWindow.setWindowTitle(QtWidgets.QApplication.translate("MyAppWindow", "Form", None, -1))
        self.btnHello.setText(QtWidgets.QApplication.translate("MyAppWindow", "Hello", None, -1))
        self.edtName.setText(QtWidgets.QApplication.translate("MyAppWindow", "world", None, -1))
        self.btnDraw.setText(QtWidgets.QApplication.translate("MyAppWindow", "Draw", None, -1))

