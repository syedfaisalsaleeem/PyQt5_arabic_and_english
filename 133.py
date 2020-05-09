#import RPi.GPIO as IO
import cv2
import sys
import time
import pytz
from pandas import DataFrame
import pandas as pd
from random import randint
from temp_reading1 import temperature_read
from functools import partial
from python_7_feb_2020 import Switch,AnalogGaugeWidget
#from keyboards import numerickeyboard,keyboard,capital_keyboard
from time import sleep
import time
import sqlite3
import gc
from datetime import datetime

from PyQt5.QtGui import QPixmap,QPainter,QFont,QCursor,QMovie,QTextCursor,QColor,QPen,QImage
from PyQt5.QtCore import QThread, pyqtSignal,QTimer,QTime,Qt,QRect
from PyQt5.QtWidgets import (QPlainTextEdit,QHeaderView,QScroller,QAbstractItemView,QComboBox,QGraphicsDropShadowEffect,QWidget,QMainWindow,QFrame,
  QApplication, QDialog,QProgressBar, QPushButton,QMdiSubWindow,QTreeWidget,QLabel,QLineEdit,QTreeWidgetItem,QMdiArea,QGraphicsView)
#import math
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os
import numpy
from pyqtgraph import AxisItem
from datetime import datetime, timedelta
from time import mktime
import psutil
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Video'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(1800, 1200)
        #create a label
        label = QLabel(self)
        cap = cv2.VideoCapture('anamed.mp4')
        ret, frame = cap.read()
        while(cap.isOpened()):
          rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                           QImage.Format_RGB888)
          convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
          pixmap = QPixmap(convertToQtFormat)
          resizeImage = pixmap.scaled(1024, 768, Qt.KeepAspectRatio)
          QApplication.processEvents()
          label.setPixmap(resizeImage)
          self.show()
          if cv2.waitKey(25) & 0xFF == ord('q'):
                break
          else: 
              break
          #self.countChanged.emit('stop')
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())