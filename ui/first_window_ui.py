# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_recordinfo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recordinfo.setGeometry(QtCore.QRect(610, 160, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_recordinfo.setFont(font)
        self.pushButton_recordinfo.setStyleSheet("/*按钮普通态*/\n"
"QPushButton\n"
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
        self.pushButton_recordinfo.setObjectName("pushButton_recordinfo")
        self.pushButton_beginexam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_beginexam.setGeometry(QtCore.QRect(610, 270, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_beginexam.setFont(font)
        self.pushButton_beginexam.setStyleSheet("/*按钮普通态*/\n"
"QPushButton\n"
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
        self.pushButton_beginexam.setObjectName("pushButton_beginexam")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 140, 281, 271))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_systemname = QtWidgets.QLabel(self.centralwidget)
        self.label_systemname.setGeometry(QtCore.QRect(210, 90, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_systemname.setFont(font)
        self.label_systemname.setStyleSheet("QLabel\n"
"{\n"
"    /*字体为微软雅黑*/\n"
"    font-family:Microsoft Yahei;\n"
"    /*字体大小为20点*/\n"
"    font-size:20pt;\n"
"    /*字体颜色为白色*/    \n"
"    color:rgb(0, 170, 255);\n"
"}")
        self.label_systemname.setObjectName("label_systemname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.center()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "首页"))
        self.pushButton_recordinfo.setText(_translate("MainWindow", "录入信息"))
        self.pushButton_beginexam.setText(_translate("MainWindow", "开始考试"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/png/模式识别/ico.png\" /></p></body></html>"))
        self.label_systemname.setText(_translate("MainWindow", "熊猫考试系统"))
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)
import png_rc

