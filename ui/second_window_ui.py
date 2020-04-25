# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
# 这段代码是 主要的ui界面  包含了八个按钮 七个lable 一个进度条
# 八个按钮对应想要的八个功能 一个lable是用来显示摄像头 画面 其余六个lable是用来显示找到的人的详细信息 最多显示三个人的  进度条是当加载人脸识别模块的时候粗略显示进度的

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap,QPainter
from PyQt5.QtWidgets import QDesktopWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 741)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 741))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 741))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1224, 731))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 40)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(14, -1, -1, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("/*按钮普通态*/\n"
                                               "QPushButton\n"
                                               "{\n"
                                               "    /*字体为微软雅黑*/\n"
                                               "    font-family:Microsoft Yahei;\n"
                                               "    /*字体大小为20点*/\n"
                                               "    font-size:20pt;\n"
                                               "    /*字体颜色为白色*/    \n"
                                               "    color:white;\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(50, 153, 50);\n"
                                               "    /*边框圆角半径为8像素*/ \n"
                                               "    border-radius:8px;\n"
                                               "}\n"
                                               "\n"
                                               "/*按钮停留态*/\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(80 , 140 , 160);\n"
                                               "}\n"
                                               "\n"
                                               "/*按钮按下态*/\n"
                                               "QPushButton:pressed\n"
                                               "{\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(80 , 140 , 160);\n"
                                               "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                               "    padding-left:3px;\n"
                                               "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                               "    padding-top:3px;\n"
                                               "}")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("/*按钮普通态*/\n"
                                               "QPushButton\n"
                                               "{\n"
                                               "    /*字体为微软雅黑*/\n"
                                               "    font-family:Microsoft Yahei;\n"
                                               "    /*字体大小为20点*/\n"
                                               "    font-size:20pt;\n"
                                               "    /*字体颜色为白色*/    \n"
                                               "    color:white;\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(50, 50, 150);\n"
                                               "    /*边框圆角半径为8像素*/ \n"
                                               "    border-radius:8px;\n"
                                               "}\n"
                                               "\n"
                                               "/*按钮停留态*/\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(80 , 140 , 160);\n"
                                               "}\n"
                                               "\n"
                                               "/*按钮按下态*/\n"
                                               "QPushButton:pressed\n"
                                               "{\n"
                                               "    /*背景颜色*/  \n"
                                               "    background-color:rgb(80 , 140 , 160);\n"
                                               "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                               "    padding-left:3px;\n"
                                               "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                               "    padding-top:3px;\n"
                                               "}")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(800, 494))
        self.label_5.setMaximumSize(QtCore.QSize(800, 494))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(180, 230))
        self.label_7.setMaximumSize(QtCore.QSize(180, 230))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 247))
        self.label_2.setMaximumSize(QtCore.QSize(200, 247))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_nextstep = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_nextstep.setGeometry(QtCore.QRect(900, 500, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft Yahei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_nextstep.setFont(font)
        self.pushButton_nextstep.setStyleSheet("/*按钮普通态*/\n"
                                                 "QPushButton\n"
                                                 "{\n"
                                                 "    /*字体为微软雅黑*/\n"
                                                 "    font-family:Microsoft Yahei;\n"
                                                 "    /*字体大小为20点*/\n"
                                                 "    font-size:20pt;\n"
                                                 "    /*字体颜色为白色*/    \n"
                                                 "    color:white;\n"
                                                 "    /*背景颜色*/  \n"
                                                 "    background-color:rgb(61, 153, 138);\n"
                                                 "    /*边框圆角半径为8像素*/ \n"
                                                 "    border-radius:8px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "/*按钮停留态*/\n"
                                                 "QPushButton:hover\n"
                                                 "{\n"
                                                 "    /*背景颜色*/  \n"
                                                 "    background-color:rgb(80 , 140 , 160);\n"
                                                 "}\n"
                                                 "\n"
                                                 "/*按钮按下态*/\n"
                                                 "QPushButton:pressed\n"
                                                 "{\n"
                                                 "    /*背景颜色*/  \n"
                                                 "    background-color:rgb(80 , 140 , 160);\n"
                                                 "    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
                                                 "    padding-left:3px;\n"
                                                 "    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
                                                 "    padding-top:3px;\n"
                                                 "}")
        self.pushButton_nextstep.setObjectName("pushButton_nextstep")

        self.retranslateUi(MainWindow)
        self.center()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton_4.setText(_translate("MainWindow", "人脸识别"))
        self.label_5.setText(_translate("MainWindow", ""))# 摄像头视频
        self.label_7.setText(_translate("MainWindow", ""))#图片1
        self.label_2.setText(_translate("MainWindow", ""))#信息1
        self.pushButton_nextstep.setText(_translate("MainWindow", "开始答题"))

        self.setWindowTitle("人脸识别")# 设置标题
        self.setWindowIcon(QIcon('./src/Amg.jpg'))#设置logo

    def paintEvent(self,event):  #设置背景图
        painter = QPainter(self)
        pixmap = QPixmap("./src/face3.jpg")
        #绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(),pixmap)
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)