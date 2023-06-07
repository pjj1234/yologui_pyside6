import sys
import cv2
import torch
import time
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer
from window_yolo_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.hub.load(repo_or_dir="./", model="custom",
                                    path="E:yolov5s.pt", source="local")
        self.model.to(device=self.device)
        self.timer = QTimer()  # 计时器
        self.timer.setInterval(20)  # 设置计时器间隔为20ms，即每隔20ms发出信号推理一帧
        self.video = None
        self.bind_slots()

    def convert2QImage(self, img):  # 将array转换为QImage以便显示
        height, width, channel = img.shape
        return QImage(img, width, height, width * channel, QImage.Format_RGB888)

    def open_image(self):  # 打开图片
        print("open image!")
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(
            self, dir="./data/images", filter="images(*.jpg; *.png; *.jpeg)")  # 传入待检测文件
        print(file_path)
        if file_path[0]:
            file_path = file_path[0]
            self.input.setPixmap(QPixmap(file_path))
            pred_image = self.image_pred(file_path)  # 已转为QImage
            self.output.setPixmap(QPixmap.fromImage(
                pred_image))  # QImage转为QPixmap并显示

    def image_pred(self, file_path):  # 图片检测
        results = self.model(file_path)
        image = results.render()[0]  # results.render()将框画在原图上;[0]表示第一张图
        return self.convert2QImage(image)

    def open_video(self):  # 打开视频
        print("open video!")
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(
            self, dir="./data/videos", filter="videos(*.mp4;*.avi;*.flv)")
        if file_path[0]:
            file_path = file_path[0]
            self.video = cv2.VideoCapture(file_path)
            self.timer.start()

    def video_pred(self):  # 视频检测
        ret, frame = self.video.read()  # ret表示是否读取到帧，frame表示读取到的帧
        # 每次read()时才会读取下一帧
        if not ret:
            self.timer.stop()
        else:
            print()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.input.setPixmap(QPixmap.fromImage(self.convert2QImage(frame)))
            start = time.perf_counter()
            results = self.model(frame)
            end = time.perf_counter()
            print("time: {} ms".format((end - start) * 1000))
            image = results.render()[0]
            self.output.setPixmap(
                QPixmap.fromImage(self.convert2QImage(image)))

    def bind_slots(self):  # 绑定槽函数
        self.det_image.clicked.connect(self.open_image)
        self.det_video.clicked.connect(self.open_video)
        self.timer.timeout.connect(self.video_pred)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
