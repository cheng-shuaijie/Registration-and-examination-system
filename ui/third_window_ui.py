# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'third_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(952, 648)
        self.label_camera3 = QtWidgets.QLabel(Form)
        self.label_camera3.setGeometry(QtCore.QRect(530, 80, 400, 320))
        self.label_camera3.setStyleSheet("QLabel{background:white;}\n"
"QLabel{font: 75 10pt \"微软雅黑\";}\n"
"\n"
"\n"
"")
        self.label_camera3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camera3.setObjectName("label_camera3")
        self.pushButton_enter = QtWidgets.QPushButton(Form)
        self.pushButton_enter.setGeometry(QtCore.QRect(490, 470, 161, 71))
        self.pushButton_enter.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:20pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(0, 170, 255);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:8px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.pushButton_back = QtWidgets.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(300, 470, 161, 71))
        self.pushButton_back.setStyleSheet("QPushButton\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:20pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:white;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(0, 170, 255);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:8px;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 110, 451, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("QLabel{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit1.setStyleSheet("QLineEdit{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.lineEdit1.setObjectName("lineEdit1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("QLabel{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("QLineEdit{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("QLabel{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setStyleSheet("QLineEdit{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("QLabel{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setStyleSheet("QLineEdit{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("QLabel{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setStyleSheet("QLineEdit{font: 75 10pt \"微软雅黑\";}\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem3)

        self.retranslateUi(Form)
        self.center()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_camera3.setText(_translate("Form", "摄像头"))
        self.pushButton_enter.setText(_translate("Form", "确 定"))
        self.pushButton_back.setText(_translate("Form", "后 退"))
        self.label.setText(_translate("Form", "姓名"))
        self.label_5.setText(_translate("Form", "学校"))
        self.label_2.setText(_translate("Form", "学号"))
        self.label_3.setText(_translate("Form", "专业"))
        self.label_4.setText(_translate("Form", "班级"))
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)