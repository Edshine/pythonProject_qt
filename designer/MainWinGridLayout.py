# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinGridLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 100, 195, 65))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(130, 280, 295, 135))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 2, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 2, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 2, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 3, 0, 1, 2)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Button1"))
        self.pushButton_2.setText(_translate("MainWindow", "Button2"))
        self.pushButton_3.setText(_translate("MainWindow", "Button3"))
        self.pushButton_4.setText(_translate("MainWindow", "Button4"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_12.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "3"))
        self.pushButton_14.setText(_translate("MainWindow", "0"))
        self.pushButton_15.setText(_translate("MainWindow", "="))