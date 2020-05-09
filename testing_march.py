import sys

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QAbstractItemView, QScrollerProperties, QScroller, QVBoxLayout, QListWidget,
                             QTabWidget, QApplication, QLabel, QListWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(700, 300)

        mainLayout = QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 50px; width: 250px; }")

        mainLayout.addWidget(self.tabWidget)

        myBoxLayout = QHBoxLayout()
        self.tabWidget.setLayout(myBoxLayout)

        self.tab1 = WidgetTab1()
        self.tab2 = WidgetTab2()

        self.tabWidget.addTab(self.tab1, 'Tab1')
        self.tabWidget.addTab(self.tab2, 'Tab2')
        self.setLayout(mainLayout)

class WidgetTab1(QWidget):

    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()

        # Create the list
        self.mylist = QListWidget()
        self.mylist.setStyleSheet("QListWidget::item { border-bottom: 1px solid gray; }")
        self.mylist.setFocusPolicy(Qt.NoFocus)
        self.mylist.setSelectionMode(QAbstractItemView.NoSelection)
        self.mylist.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mylist.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        for i in range(20):
            item = QListWidgetItem(self.mylist)
            self.mylist.addItem(item)
            self.mylist.setItemWidget(item, QLabel(str(i)))

        self.sp = QScrollerProperties()
        self.sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.6)
        self.sp.setScrollMetric(QScrollerProperties.MinimumVelocity, 0.0)
        self.sp.setScrollMetric(QScrollerProperties.MaximumVelocity, 0.2)
        self.sp.setScrollMetric(QScrollerProperties.AcceleratingFlickMaximumTime, 0.1)
        self.sp.setScrollMetric(QScrollerProperties.AcceleratingFlickSpeedupFactor, 1.2)
        self.sp.setScrollMetric(QScrollerProperties.SnapPositionRatio, 0.2)
        self.sp.setScrollMetric(QScrollerProperties.MaximumClickThroughVelocity, 1)
        self.sp.setScrollMetric(QScrollerProperties.DragStartDistance, 0.001)
        self.sp.setScrollMetric(QScrollerProperties.MousePressEventDelay, 0.5)

        self.scroller = QScroller.scroller(self.mylist.viewport())
        self.scroller.setScrollerProperties(self.sp)
        self.scroller.grabGesture(self.mylist.viewport(), QScroller.LeftMouseButtonGesture)

        self.mylist.show()
        self.hbox.addWidget(self.mylist)
        self.setLayout(self.hbox)

class WidgetTab2(QWidget):

    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()

        # Create the list
        self.mylist = QListWidget()
        self.mylist.setStyleSheet("QListWidget::item { border-bottom: 1px solid gray; }")
        self.mylist.setFocusPolicy(Qt.NoFocus)
        self.mylist.setSelectionMode(QAbstractItemView.NoSelection)
        self.mylist.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mylist.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        for i in range(19, 0, -1):
            item = QListWidgetItem(self.mylist)
            self.mylist.addItem(item)
            self.mylist.setItemWidget(item, QLabel(str(i)))

        self.sp = QScrollerProperties()
        self.sp.setScrollMetric(QScrollerProperties.DragVelocitySmoothingFactor, 0.6)
        self.sp.setScrollMetric(QScrollerProperties.MinimumVelocity, 0.0)
        self.sp.setScrollMetric(QScrollerProperties.MaximumVelocity, 0.2)
        self.sp.setScrollMetric(QScrollerProperties.AcceleratingFlickMaximumTime, 0.1)
        self.sp.setScrollMetric(QScrollerProperties.AcceleratingFlickSpeedupFactor, 1.2)
        self.sp.setScrollMetric(QScrollerProperties.SnapPositionRatio, 0.2)
        self.sp.setScrollMetric(QScrollerProperties.MaximumClickThroughVelocity, 1)
        self.sp.setScrollMetric(QScrollerProperties.DragStartDistance, 0.001)
        self.sp.setScrollMetric(QScrollerProperties.MousePressEventDelay, 0.5)

        self.scroller = QScroller.scroller(self.mylist.viewport())
        self.scroller.setScrollerProperties(self.sp)
        self.scroller.grabGesture(self.mylist.viewport(), QScroller.LeftMouseButtonGesture)

        self.mylist.show()
        self.hbox.addWidget(self.mylist)
        self.setLayout(self.hbox)

if __name__ == '__main__':
    qApplication = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    qApplication.exec_()