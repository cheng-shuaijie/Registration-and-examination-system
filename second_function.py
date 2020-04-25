import sys
import os  #打开文件
import threading  #多线程
import ft2  #汉字标框模块
from os import listdir  # 地址 用于打开位置
from datetime import datetime  #可以用于获取当前的时间
from time import time   #用于计算时间差 可以用来计算一个模块运行的时间
import xlrd    # 计入excel
from xlutils.copy import copy   #记录在记录信息到excel的时候用
import cv2  #打开摄像头
import face_recognition  #人脸识别模块
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QBasicTimer,pyqtSignal,Qt
from second_window_ui import Ui_MainWindow  # 主窗体ui代码
from PyQt5.QtWidgets import QApplication ,QMainWindow,QMessageBox,QFileDialog
from voice_syn_ui import Ui_MainWindow2  # 第二个界面用于 语音合成
from baiduvoice import baidu_voice   #百度语音合成模块
import fourth_window_ui
t=time()
class myfourthwindow(QMainWindow, fourth_window_ui.Ui_Form):
    def __init__(self):
        print("hahaha")
        super(myfourthwindow, self).__init__()
        self.setupUi(self)
class MyMainWindow(QMainWindow,Ui_MainWindow):
    signal=pyqtSignal()  #初始化信号  为了实现双重界面
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_nextstep.clicked.connect(self.nextwindow)
        self.source=0
        # self.timer_camera = QTimer()  # 需要定时器刷新摄像头界面
        self.cap = cv2.VideoCapture()
        self.video_btn=0    # 用去区分打开摄像头和人脸识别 当打开人脸识别按钮的时候 video_btn 就会变成1  这样的话 关闭人脸识别 摄像头还是处于打开的状态
        self.need_record_name="Unknown"
        # 信号槽设置  ------------------------------
        self.pushButton_6.clicked.connect(lambda:self.video_source(2)) # 对打开摄像头2 按钮进行连接函数
        self.pushButton_4.clicked.connect(self.face_recognition_btn) # 人脸识别按钮连接函数 调用face_recogniton_btn
        print('mainwindow  is running')
        self.show()
    # 信号槽对应的函数
    def nextwindow(self):
        self.close()
        fourth_win = myfourthwindow()
        fourth_win.show()
    def video_source(self,num):  # 打开摄像头123  这三个按钮 的响应函数 词函数只是提供一个rtsp地址实际的打开摄像头的函数还是下面的btn_opoen_cam_click
        print('打开摄像头')
        #self.source = "rtsp://admin:admin@192.168.0.102:8554/live"
        self.source = "./src/video.mp4"
        self.btn_open_cam_click()
    def btn_open_cam_click(self):  #打开摄像头 按钮函数
        self.t3=time()
        self.qingping()
        print('click is ok')
        self.cap.open(self.source)    
        print(self.cap.isOpened())
        self.show_camera()
        self.qingping()
    def face_recognition_btn(self):  # 人脸识别按钮  通过video_btn的值来控制
        self.t2=time()
        self.time_step=0
        if self.video_btn==0:
            self.video_btn=1
            self.pushButton_4.setText(u'关闭人脸识别')
            self.show_camera()
        elif self.video_btn==1:
            self.video_btn=0
            self.pushButton_4.setText(u'人脸识别')
            self.qingping()
            self.show_camera()
            self.qingping()
    def show_camera(self):  #展示摄像头画面并进行人脸识别的功能
        print('show_camera is open ')
        if self.video_btn==0:    #在前面就设置了video_btn为0 为了在人脸识别的时候直接把这个值给改了 这样人脸识别和摄像头展示就分开了
            self.pushButton_6.setText(u'关闭摄像头')
            while (self.cap.isOpened()):
                ret, self.image = self.cap.read()
                QApplication.processEvents()  #QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者  减少代码卡顿
                show = cv2.resize(self.image, (800, 494))
                show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                self.label_5.setPixmap(QPixmap.fromImage(self.showImage))
              #  因为他最后会存留一张 图像在lable上需要对 lable_5进行清理
            self.label_5.clear()
            print('打开摄像头时间',time()-self.t3)
        elif self.video_btn==1: 
            #这段代码是 获取photo文件夹中 人的信息
             filepath='photo'
             filename_list=listdir(filepath)
             known_face_names=[]
             known_face_encodings=[]
             a=0
             print('2')
             for filename in filename_list:#依次读入列表中的内容
                a+=1
                QApplication.processEvents()
                if filename.endswith('jpg'):# 后缀名'jpg'匹对
                    known_face_names.append(filename[:-4])#把文件名字的后四位.jpg去掉获取人名
                    file_str='./photo/'+filename
                    a_images=face_recognition.load_image_file(file_str)
                    print(file_str)
                    a_face_encoding = face_recognition.face_encodings(a_images)[0]
                    known_face_encodings.append(a_face_encoding)
             print(known_face_names,a)
            #knowe_face_names里面放着每个人的名字   known_face_encodings里面放着提取出来的每个人的人脸特征信息

             face_locations = []
             face_encodings = []
             face_names =[]
             process_this_frame = True
             while (self.cap.isOpened()):
                 ret, frame = self.cap.read()
                 QApplication.processEvents()
                    # 改变摄像头图像的大小，图像小，所做的计算就少
                 small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
                # print('3 is running')
                    # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
                 rgb_small_frame = small_frame[:, :, ::-1]
                 #print('4 is running')
                 if process_this_frame:
                     QApplication.processEvents()
                        # 根据encoding来判断是不是同一个人，是就输出true，不是为flase
                     face_locations = face_recognition.face_locations(rgb_small_frame)
                     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                     face_names = []
                    # print('5 is  running')
                     for face_encoding in face_encodings:
                            # 默认为unknown
                         matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.42)
                            #阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
                            #print(matches)
                         name = "Unknown"

                         if True in matches:
                             first_match_index = matches.index(True)
                             name = known_face_names[first_match_index]

                         face_names.append(name)
                 process_this_frame = not process_this_frame
                    # 将捕捉到的人脸显示出来
                 self.set_name=set(face_names)
                 self.set_names=tuple(self.set_name) # 把名字先设为了一个 集合 把重复的去掉 再设为tuple 以便于下面显示其他信息和记录 调用
                 voice_syn=str()
                 print(self.set_names) #把人脸识别检测到的人 用set_names 这个集合收集起来
                 for (top, right, bottom, left), name in zip(face_locations, face_names):
                        #由于我们检测到的帧被缩放到1/4大小，所以要缩小面位置
                     top *= 3
                     right *= 3
                     bottom *= 3
                     left *= 3
                        # 矩形框
                     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
                     ft = ft2.put_chinese_text('./src/msyh.ttf')
                        #引入ft2中的字体
                     frame = ft.draw_text(frame, (left+10 , bottom ), name, 25, (0, 0, 255))
                     print('face recognition is running')
                 self.show_picture() # 调用显示详细信息的函数

                 show_video = cv2.resize(frame, (800, 494))
                 show_video = cv2.cvtColor(show_video,cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                 self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0], QImage.Format_RGB888)
                 self.label_5.setPixmap(QPixmap.fromImage(self.showImage))
             print('打开人脸识别所需要的时间',time()-self.t2)
    def show_picture(self):  #  在人脸识别的右边显示 识别出来人的详细信息
         if self.video_btn==1:
             fr = open("./src/text.txt",'r+')  #读取information.txt中的信息  里面是录入信息时写入的
             infor_dic = eval(fr.read())   #从information.txt文件中读取的str转换为字
             person1 = self.set_names[0]
             infor_names = infor_dic[person1]
             name_str = 'photo/' + person1 + '.jpg'
             picture = QPixmap(name_str)

             infor_str = '姓名：' + person1 + '                ' + '学校：' + infor_names[
                 '学校'] + '                 ' + '学号: ' + infor_names['学号'] + '                   ' + '专业：' + infor_names[
                             '专业'] + '                       ' + '班级：' + infor_names['班级']

             self.label_2.setText(infor_str)
             self.label_2.setStyleSheet("color:rgb(192,192,192);font-size:20px;font-family:Microsoft YaHei;")
             self.label_2.setWordWrap(True)  # 自适应大小换行
             self.label_7.setPixmap(picture)  # 把照片放到label_7上面去
             self.label_7.setScaledContents(True)  # 让照片能够在label上面自适应大小
             need_voice_name = str(person1)
             # if need_voice_name == 'Unknown':
             #     QMessageBox.about(self, 'warning', '还未识别出人脸')
             # else:
             #     print("begin voice")
             #     voice_str = need_voice_name + '同学，欢迎参加本场考试'
             #     baidu_voice(voice_str)
             fr.close()
    def qingping(self):  # 不需要显示信息的时候   把显示到信息的那部分清除掉 在循环中保存了几次那些lable就不在发生变化了
         self.label_7.clear()  # 照片1
         self.label_2.setText("")  # 信息1

if __name__=="__main__" :
    app=QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.show()  #连接信号
    print('打开ui界面所需时间',time()-t)
    sys.exit(app.exec_())