import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
import first_window_ui
import second_window_ui
import third_window_ui
import second_function
from PyQt5.QtGui import *
import cv2
import os  #打开文件
from PyQt5.QtWidgets import QApplication ,QMainWindow,QMessageBox,QFileDialog
from baiduvoice import baidu_voice
from time import time

class mythirdwindow(QMainWindow,third_window_ui.Ui_Form):
    def __init__(self):
        super(mythirdwindow,self).__init__()
        self.setupUi(self)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_enter.clicked.connect(self.back)
    def back(self):
        mysender=self.sender()
        if mysender.text()=="后 退":
            self.close()
            firstwindow.show()
        if mysender.text()=="确 定":
            #截图保存
            photo_save_path = os.path.join(os.path.dirname(os.path.abspath('__file__')), 'photo/')
            #self.showImage=self.showImage[100:500, 100:480]
            self.showImage.save(photo_save_path + self.lineEdit1.text()+".jpg")
            pc = cv2.imread('./photo/'+ self.lineEdit1.text()+'.jpg')
            pc = pc[0:400, 60:310]
            cv2.imwrite('./photo/'+ self.lineEdit1.text()+'.jpg', pc)
            QMessageBox.information(self, "Information", self.tr("报名成功!"))
            #保存个人信息
            fr = open("./src/text.txt", 'r+')
            infor_dic = eval(fr.read())
            fr.close()
            fr2 = open("./src/text.txt", 'w+')
            infor_dic[self.lineEdit1.text()] = {'学校': self.lineEdit_2.text(), '学号': self.lineEdit_3.text(), '专业': self.lineEdit_4.text(),
                                       '班级': self.lineEdit_5.text()}
            mystr = str(infor_dic)
            fr2.write(mystr)
            fr2.close()
            self.close()
            firstwindow.show()
    def third_camera(self):
        self.cap = cv2.VideoCapture()
        self.source = "./src/video.mp4"
        self.cap.open(self.source)
        print(self.cap.isOpened())
        while (self.cap.isOpened()):
            ret, self.image = self.cap.read()
            QApplication.processEvents()  # QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者  减少代码卡顿
            show = cv2.resize(self.image, (400, 320))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
            # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
            self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.label_camera3.setPixmap(QPixmap.fromImage(self.showImage))
        #  因为他最后会存留一张 图像在lable上需要对 label_camera3进行清理
        self.label_camera3.clear()

class mywindow(QMainWindow,first_window_ui.Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton_beginexam.clicked.connect(self.change)
        self.pushButton_recordinfo.clicked.connect(self.change)
    def change(self):
        mysender = self.sender()
        if mysender.text()=="录入信息":
            self.close()
            third_win=mythirdwindow()
            third_win.show()
            recordinfo_camera = third_win.third_camera()
        if mysender.text()=="开始考试":
            self.close()
            myWin = second_function.MyMainWindow()
            myWin.show()


if __name__ =='__main__':
    app=QApplication(sys.argv)
    firstwindow=mywindow()
    firstwindow.show()
    app.exec_()
