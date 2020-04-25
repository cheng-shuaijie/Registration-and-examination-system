# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow
# import cv2
# from PyQt5.QtGui import *
# import third_window_ui
# class recordimage(QMainWindow,third_window_ui.Ui_Form):
#     def __init__(self):
#         super(recordimage,self).__init__()
#         self.setupUi(self)
#     def third_camera(self):
#         self.cap = cv2.VideoCapture()
#         self.source = "./src/video.mp4"
#         self.cap.open(self.source)
#         print(self.cap.isOpened())
#         while (self.cap.isOpened()):
#             ret, self.image = self.cap.read()
#             QApplication.processEvents()  # QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者  减少代码卡顿
#             show = cv2.resize(self.image, (400, 320))
#             show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
#             # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
#             self.showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
#             self.label_camera3.setPixmap(QPixmap.fromImage(self.showImage))
#         #  因为他最后会存留一张 图像在lable上需要对 label_camera3进行清理
#         self.label_camera3.clear()
#
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     firstwindow=recordimage()
#     firstwindow.show()
#     firstwindow.third_camera()
#     app.exec_()