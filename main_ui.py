# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QtSource\Main_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 10, 601, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lcdNumber = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 360, 601, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 140, 601, 211))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.A_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.A_label.setFont(font)
        self.A_label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.A_label.setAlignment(QtCore.Qt.AlignCenter)
        self.A_label.setObjectName("A_label")
        self.horizontalLayout_3.addWidget(self.A_label)
        self.sign_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.sign_label.setFont(font)
        self.sign_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sign_label.setObjectName("sign_label")
        self.horizontalLayout_3.addWidget(self.sign_label)
        self.B_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B_label.setFont(font)
        self.B_label.setAlignment(QtCore.Qt.AlignCenter)
        self.B_label.setObjectName("B_label")
        self.horizontalLayout_3.addWidget(self.B_label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.confirmButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.confirmButton.setMinimumSize(QtCore.QSize(60, 60))
        self.confirmButton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_3.addWidget(self.confirmButton)
        self.Display_Label = QtWidgets.QLabel(self.centralwidget)
        self.Display_Label.setGeometry(QtCore.QRect(200, 69, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Display_Label.setFont(font)
        self.Display_Label.setText("")
        self.Display_Label.setObjectName("Display_Label")
        self.UsernameBox = QtWidgets.QComboBox(self.centralwidget)
        self.UsernameBox.setGeometry(QtCore.QRect(90, 80, 69, 22))
        self.UsernameBox.setObjectName("UsernameBox")
        self.UsernameBox.addItem("")
        self.UsernameBox.addItem("")
        self.UsernameBox.addItem("")
        self.UsernameBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(26, 80, 51, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Math Game"))
        self.label_2.setText(_translate("MainWindow", "Rate:"))
        self.label.setText(_translate("MainWindow", "Score:"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Pause"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.A_label.setText(_translate("MainWindow", "A"))
        self.sign_label.setText(_translate("MainWindow", "+"))
        self.B_label.setText(_translate("MainWindow", "B"))
        self.label_3.setText(_translate("MainWindow", "="))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.UsernameBox.setItemText(0, _translate("MainWindow", "Lucas"))
        self.UsernameBox.setItemText(1, _translate("MainWindow", "Luna"))
        self.UsernameBox.setItemText(2, _translate("MainWindow", "Sasha"))
        self.UsernameBox.setItemText(3, _translate("MainWindow", "Alex"))
        self.label_4.setText(_translate("MainWindow", "Useranme:"))
        self.menuHelp.setTitle(_translate("MainWindow", "File"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))