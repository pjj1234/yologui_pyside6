# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'window_yolo.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1197, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.det_image = QPushButton(self.centralwidget)
        self.det_image.setObjectName(u"det_image")
        self.det_image.setGeometry(QRect(210, 510, 181, 41))
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(30, 60, 541, 401))
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.output = QLabel(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(620, 60, 541, 401))
        self.output.setTextFormat(Qt.AutoText)
        self.output.setScaledContents(True)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.det_video = QPushButton(self.centralwidget)
        self.det_video.setObjectName(u"det_video")
        self.det_video.setGeometry(QRect(760, 510, 181, 41))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(580, 40, 31, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.det_image.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u56fe\u7247", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5185\u5bb9", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7ed3\u679c", None))
        self.det_video.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u89c6\u9891", None))
    # retranslateUi
