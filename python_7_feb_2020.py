
import sys
import math
from PyQt5.QtGui import QPolygon, QPolygonF, QColor, QPen, QFont,QPainter, QFontMetrics, QConicalGradient,QPixmap
# QtGui -> QPolygon, QPolygonF, QColor, QPen, QFont, QPainter, QFontMetrics, QConicalGradient

from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize,QObject, pyqtSignal,QRectF,QPropertyAnimation,  pyqtProperty
from PyQt5.QtWidgets import (
    QAbstractButton,
    QApplication,
    QHBoxLayout,
    QSizePolicy,
    QWidget,
    QMainWindow,
    QLabel,QPushButton,QLineEdit
)


class Switch(QAbstractButton):
    def __init__(self, parent=None,text=' ',track_radius=40, thumb_radius=40):
        super().__init__(parent=parent)
        self.setCheckable(True)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.text=text
        self._track_radius = track_radius
        self._thumb_radius = thumb_radius

        self._margin = max(0, self._thumb_radius - self._track_radius)
        self._base_offset = max(self._thumb_radius, self._track_radius)
        self._end_offset = {
            True: lambda: self.width() - self._base_offset,
            False: lambda: self._base_offset,
        }
        self._offset = self._base_offset

        palette = self.palette()
        if self._thumb_radius > self._track_radius:
            self._track_color = {
                True: palette.highlight(),
                False: palette.dark(),
            }
            self._thumb_color = {
                True: palette.highlight(),
                False: palette.light(),
            }
            self._text_color = {
                True: palette.highlightedText().color(),
                False: palette.dark().color(),
            }
            self._thumb_text = {
                True: '',
                False: '',
            }
            self._track_opacity = 0.5
        else:
            self._thumb_color = {
                True: palette.highlightedText(),
                False: palette.light(),
            }
            self._track_color = {
                True: palette.highlight(),
                False: palette.dark(),
            }
            self._text_color = {
                True: palette.highlight().color(),
                False: palette.dark().color(),
            }
            if(self.text=='Time'):
                self._thumb_text = {
                    False: '12H',
                    True:'24H',
                }
            elif(self.text=='Temperature'):
                self._thumb_text = {
                    False: 'C',
                    True:'F',
                } 
            self._track_opacity = 1

    @pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.update()

    def sizeHint(self):  # pylint: disable=invalid-name
        return QSize(
            4 * self._track_radius + 2 * self._margin,
            2 * self._track_radius + 2 * self._margin,
        )

    def setChecked(self, checked):
        super().setChecked(checked)
        self.offset = self._end_offset[checked]()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.offset = self._end_offset[self.isChecked()]()

    def paintEvent(self, event):  # pylint: disable=invalid-name, unused-argument
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setPen(Qt.NoPen)
        track_opacity = self._track_opacity
        thumb_opacity = 1.0
        text_opacity = 1.0
        if self.isEnabled():
            track_brush = self._track_color[self.isChecked()]
            thumb_brush = self._thumb_color[self.isChecked()]
            text_color = self._text_color[self.isChecked()]
        else:
            track_opacity *= 0.8
            track_brush = self.palette().shadow()
            thumb_brush = self.palette().mid()
            text_color = self.palette().shadow().color()

        p.setBrush(track_brush)
        p.setOpacity(track_opacity)
        p.drawRoundedRect(
            self._margin,
            self._margin,
            self.width() - 2 * self._margin,
            self.height() - 2 * self._margin,
            self._track_radius,
            self._track_radius,
        )
        p.setBrush(thumb_brush)
        p.setOpacity(thumb_opacity)
        p.drawEllipse(
            self.offset - self._thumb_radius,
            self._base_offset - self._thumb_radius,
            2 * self._thumb_radius,
            2 * self._thumb_radius,
        )
        p.setPen(text_color)
        p.setOpacity(text_opacity)
        font = p.font()
        font.setPixelSize(1.0 * self._thumb_radius)
        p.setFont(font)
        p.drawText(
            QRectF(
                self.offset - self._thumb_radius,
                self._base_offset - self._thumb_radius,
                2 * self._thumb_radius,
                2 * self._thumb_radius,
            ),
            Qt.AlignCenter,
            self._thumb_text[self.isChecked()],
        )

    def mouseReleaseEvent(self, event):  # pylint: disable=invalid-name
        super().mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            anim = QPropertyAnimation(self, b'offset', self)
            anim.setDuration(120)
            anim.setStartValue(self.offset)
            anim.setEndValue(self._end_offset[self.isChecked()]())
            anim.start()

    def enterEvent(self, event):  # pylint: disable=invalid-name
        self.setCursor(Qt.PointingHandCursor)
        super().enterEvent(event)


class AnalogGaugeWidget(QWidget):

    valueChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(AnalogGaugeWidget, self).__init__(parent)

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
        self.setCursor(Qt.BlankCursor)
        self.activateWindow()


        self.use_timer_event = True
        self.black = QColor(0, 0, 0, 255)

        # self.valueColor = QColor(50, 50, 50, 255)
        # self.set_valueColor(50, 50, 50, 255)
        # self.NeedleColor = QColor(50, 50, 50, 255)
        self.set_NeedleColor(50, 50, 50, 255)
        self.NeedleColorReleased = self.NeedleColor
        # self.NeedleColorDrag = QColor(255, 0, 00, 255)
        self.set_NeedleColorDrag(255, 0, 00, 255)

        self.set_ScaleValueColor(50, 50, 50, 255)
        self.set_DisplayValueColor(50, 50, 50, 255)

        # self.CenterPointColor = QColor(50, 50, 50, 255)
        self.set_CenterPointColor(50, 50, 50, 255)

        # self.valueColor = black
        # self.black = QColor(0, 0, 0, 255)

        self.value_needle_count = 1
        self.value_needle = QObject
        self.change_value_needle_style([QPolygon([
            QPoint(4, 4),
            QPoint(-4, 4),
            QPoint(-3, -120),
            QPoint(0, -126),
            QPoint(3, -120)
        ])])

        self.value_min = 0
        self.value_max = 300
        self.value = 50
        self.value_offset = 0
        self.value_needle_snapzone = 0.05
        self.last_value = 0

        # self.value2 = 0
        # self.value2Color = QColor(0, 0, 0, 255)

        self.gauge_color_outer_radius_factor = 1
        self.gauge_color_inner_radius_factor = 0.95
        self.center_horizontal_value = 0
        self.center_vertical_value = 0
        self.debug1 = None
        self.debug2 = None
        self.scale_angle_start_value = 135
        self.scale_angle_size = 270
        self.angle_offset = 0

        # self.scala_main_count = 10
        self.set_scala_main_count(10)
        self.scala_subdiv_count = 6

        self.pen = QPen(QColor(0, 0, 0))
        self.font = QFont('Decorative', 20)

        self.scale_polygon_colors = []
        self.l_1=(0,[])
        self.l_2=[]
        self.set_scale_polygon_colors([[.00, Qt.red],
                                     [.1, Qt.yellow],
                                     [.15, Qt.green],
                                     [1, Qt.transparent]])

        # initialize Scale value text
        # self.enable_scale_text = True
        self.set_enable_ScaleText(True)
        self.scale_fontname = "Decorative"
        self.initial_scale_fontsize = 15
        self.scale_fontsize = self.initial_scale_fontsize

        # initialize Main value text
        self.enable_value_text = True
        self.value_fontname = "Decorative"
        self.initial_value_fontsize = 40
        self.value_fontsize = self.initial_value_fontsize
        self.text_radius_factor = 0.7

        # En/disable scale / fill
        # self.enable_barGraph = True
        self.set_enable_barGraph(True)
        # self.enable_filled_Polygon = True
        self.set_enable_filled_Polygon(True)


        self.enable_CenterPoint = True
        self.enable_fine_scaled_marker = True
        self.enable_big_scaled_marker = True

        self.needle_scale_factor = 0.8
        self.enable_Needle_Polygon = True

        # necessary for resize
        self.setMouseTracking(False)

        if self.use_timer_event:
            timer = QTimer(self)
            timer.timeout.connect(self.update)
            timer.start(50)

        else:
            self.update()


        # self.connect(self, SIGNAL("resize()"), self.rescaleMethod)

        # self.resize(300 , 300)
        self.rescale_method()
        
    def rescale_method(self):
        # print("slotMethod")
        if self.width() <= self.height():
            self.widget_diameter = self.width()
        else:
            self.widget_diameter = self.height()

        self.change_value_needle_style([QPolygon([
            QPoint(4, 30),
            QPoint(-4, 30),
            QPoint(-2, - self.widget_diameter / 2 * self.needle_scale_factor),
            QPoint(0, - self.widget_diameter / 2 * self.needle_scale_factor - 6),
            QPoint(2, - self.widget_diameter / 2 * self.needle_scale_factor)
        ])])


        self.scale_fontsize = self.initial_scale_fontsize * self.widget_diameter / 400
        self.value_fontsize = self.initial_value_fontsize * self.widget_diameter / 400

        # print("slotMethod end")
        pass

    def change_value_needle_style(self, design):
        # prepared for multiple needle instrument
        self.value_needle = []
        for i in design:
            self.value_needle.append(i)
        if not self.use_timer_event:
            self.update()

    def update_value(self, value, mouse_controlled = False):
        if not mouse_controlled:
             self.value = value
        
        if mouse_controlled:
             self.valueChanged.emit(int(value))

        if value <= self.value_min:
            self.value = self.value_min
        elif value >= self.value_max:
            self.value = self.value_max
        else:
            self.value = value
        # self.paintEvent("")
        self.valueChanged.emit(float(value))
        # print(self.value)

        # ohne timer: aktiviere self.update()
        if not self.use_timer_event:
            self.update()

    def update_angle_offset(self, offset):
        self.angle_offset = offset
        if not self.use_timer_event:
            self.update()

    def center_horizontal(self, value):
        self.center_horizontal_value = value
        # print("horizontal: " + str(self.center_horizontal_value))

    def center_vertical(self, value):
        self.center_vertical_value = value
        # print("vertical: " + str(self.center_vertical_value))

 ###############################################################################################
    def set_NeedleColor(self, R=50, G=50, B=50, Transparency=255):

        self.NeedleColor = QColor(R, G, B, Transparency)
        self.NeedleColorReleased = self.NeedleColor

        if not self.use_timer_event:
            self.update()

    def set_NeedleColorDrag(self, R=50, G=50, B=50, Transparency=255):

        self.NeedleColorDrag = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    def set_ScaleValueColor(self, R=50, G=50, B=50, Transparency=255):

        self.ScaleValueColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    def set_DisplayValueColor(self, R=50, G=50, B=50, Transparency=255):

        self.DisplayValueColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    def set_CenterPointColor(self, R=50, G=50, B=50, Transparency=255):
        self.CenterPointColor = QColor(R, G, B, Transparency)

        if not self.use_timer_event:
            self.update()

    def set_enable_Needle_Polygon(self, enable = True):
        self.enable_Needle_Polygon = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_ScaleText(self, enable = True):
        self.enable_scale_text = enable

        if not self.use_timer_event:
            self.update()


    def set_enable_barGraph(self, enable = True):
        self.enable_barGraph = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_value_text(self, enable = True):
        self.enable_value_text = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_CenterPoint(self, enable = True):
        self.enable_CenterPoint = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_filled_Polygon(self, enable = True):
        self.enable_filled_Polygon = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_big_scaled_grid(self, enable = True):
        self.enable_big_scaled_marker = enable

        if not self.use_timer_event:
            self.update()

    def set_enable_fine_scaled_marker(self, enable = True):
        self.enable_fine_scaled_marker = enable

        if not self.use_timer_event:
            self.update()

    def set_scala_main_count(self, count):
        if count < 1:
            count = 1
        self.scala_main_count = count

        if not self.use_timer_event:
            self.update()

    def set_MinValue(self, min):
        if self.value < min:
            self.value = min
        if min >= self.value_max:
            self.value_min = self.value_max - 1
        else:
            self.value_min = min

        if not self.use_timer_event:
            self.update()

    def set_MaxValue(self, max):
        if self.value > max:
            self.value = max
        if max <= self.value_min:
            self.value_max = self.value_min + 1
        else:
            self.value_max = max

        if not self.use_timer_event:
            self.update()

    def set_start_scale_angle(self, value):
        # Value range in DEG: 0 - 360
        self.scale_angle_start_value = value
        # print("startFill: " + str(self.scale_angle_start_value))

        if not self.use_timer_event:
            self.update()

    def set_total_scale_angle_size(self, value):
        self.scale_angle_size = value
        # print("stopFill: " + str(self.scale_angle_size))

        if not self.use_timer_event:
            self.update()

    def set_gauge_color_outer_radius_factor(self, value):
        self.gauge_color_outer_radius_factor = float(value) / 1000
        # print(self.gauge_color_outer_radius_factor)

        if not self.use_timer_event:
            self.update()

    def set_gauge_color_inner_radius_factor(self, value):
        self.gauge_color_inner_radius_factor = float(value) / 1000
        # print(self.gauge_color_inner_radius_factor)

        if not self.use_timer_event:
            self.update()

    def set_scale_polygon_colors(self, color_array):
        # print(type(color_array))
        if 'list' in str(type(color_array)):
            self.scale_polygon_colors = color_array
        elif color_array == None:
            self.scale_polygon_colors = [[.0, Qt.transparent]]
        else:
            self.scale_polygon_colors = [[.0, Qt.transparent]]

        if not self.use_timer_event:
            self.update()


    def get_value_max(self):
        return self.value_max


    def create_polygon_pie(self, outer_radius, inner_raduis, start, lenght):
        polygon_pie = QPolygonF()
        # start = self.scale_angle_start_value
        # start = 0
        # lenght = self.scale_angle_size
        # lenght = 180
        # inner_raduis = self.width()/4
        # print(start)
        n = 360     # angle steps size for full circle
        # changing n value will causes drawing issues
        w = 360 / n   # angle per step
        # create outer circle line from "start"-angle to "start + lenght"-angle
        x = 0
        y = 0

        # todo enable/disable bar graf here
        if not self.enable_barGraph:
            # float_value = ((lenght / (self.value_max - self.value_min)) * (self.value - self.value_min))
            lenght = int(round((lenght / (self.value_max - self.value_min)) * (self.value - self.value_min)))
            # print("f: %s, l: %s" %(float_value, lenght))
            pass

        # mymax = 0

        for i in range(lenght+1):                                              # add the points of polygon
            t = w * i + start - self.angle_offset
            x = outer_radius * math.cos(math.radians(t))
            y = outer_radius * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))
        # create inner circle line from "start + lenght"-angle to "start"-angle
        for i in range(lenght+1):                                              # add the points of polygon
            # print("2 " + str(i))
            t = w * (lenght - i) + start - self.angle_offset
            x = inner_raduis * math.cos(math.radians(t))
            y = inner_raduis * math.sin(math.radians(t))
            polygon_pie.append(QPointF(x, y))

        # close outer line
        polygon_pie.append(QPointF(x, y))
        return polygon_pie

    def draw_filled_polygon(self, outline_pen_with=0):
        if not self.scale_polygon_colors == None:
            painter_filled_polygon = QPainter(self)
            painter_filled_polygon.setRenderHint(QPainter.Antialiasing)
            # Koordinatenursprung in die Mitte der Flaeche legen
            painter_filled_polygon.translate(self.width() / 2, self.height() / 2)

            painter_filled_polygon.setPen(Qt.NoPen)

            self.pen.setWidth(outline_pen_with)
            if outline_pen_with > 0:
                painter_filled_polygon.setPen(self.pen)

            colored_scale_polygon = self.create_polygon_pie(
                ((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_outer_radius_factor,
                (((self.widget_diameter / 2) - (self.pen.width() / 2)) * self.gauge_color_inner_radius_factor),
                self.scale_angle_start_value, self.scale_angle_size)

            gauge_rect = QRect(QPoint(0, 0), QSize(self.widget_diameter / 2 - 1, self.widget_diameter - 1))
            grad = QConicalGradient(QPointF(0, 0), - self.scale_angle_size - self.scale_angle_start_value +
                                    self.angle_offset - 1)

            # todo definition scale color as array here
            for eachcolor in self.scale_polygon_colors:
                grad.setColorAt(eachcolor[0], eachcolor[1])
            # grad.setColorAt(.00, Qt.red)
            # grad.setColorAt(.1, Qt.yellow)
            # grad.setColorAt(.15, Qt.green)
            # grad.setColorAt(1, Qt.transparent)
            painter_filled_polygon.setBrush(grad)
            # self.brush = QBrush(QColor(255, 0, 255, 255))
            # painter_filled_polygon.setBrush(self.brush)
            painter_filled_polygon.drawPolygon(colored_scale_polygon)
            # return painter_filled_polygon


    def draw_big_scaled_markter(self):
        my_painter = QPainter(self)
        my_painter.setRenderHint(QPainter.Antialiasing)
        # Koordinatenursprung in die Mitte der Flaeche legen
        my_painter.translate(self.width() / 2, self.height() / 2)

        # my_painter.setPen(Qt.NoPen)
        self.pen = QPen(QColor(0, 0, 0, 255))
        self.pen.setWidth(2)
        # # if outline_pen_with > 0:
        my_painter.setPen(self.pen)

        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) / float(self.scala_main_count))
        scale_line_outer_start = self.widget_diameter/2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 20)
        # print(stepszize)
        for i in range(self.scala_main_count+1):
            my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_scale_marker_values_text(self):
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)

        # Koordinatenursprung in die Mitte der Flaeche legen
        painter.translate(self.width() / 2, self.height() / 2)
        # painter.save()
        font = QFont(self.scale_fontname, self.scale_fontsize)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.ScaleValueColor)
        painter.setPen(pen_shadow)

        text_radius_factor = 0.8
        text_radius = self.widget_diameter/2 * text_radius_factor

        scale_per_div = int((self.value_max - self.value_min) / self.scala_main_count)

        angle_distance = (float(self.scale_angle_size) / float(self.scala_main_count))
        for i in range(self.scala_main_count + 1):
            # text = str(int((self.value_max - self.value_min) / self.scala_main_count * i))
            text = str(int(self.value_min + scale_per_div * i))
            w = fm.width(text) + 1
            h = fm.height()
            painter.setFont(QFont(self.scale_fontname, self.scale_fontsize))
            angle = angle_distance * i + float(self.scale_angle_start_value - self.angle_offset)
            x = text_radius * math.cos(math.radians(angle))
            y = text_radius * math.sin(math.radians(angle))
            # print(w, h, x, y, text)
            text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
            painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
        # painter.restore()

    def create_fine_scaled_marker(self):
        #  Description_dict = 0
        my_painter = QPainter(self)

        my_painter.setRenderHint(QPainter.Antialiasing)
        # Koordinatenursprung in die Mitte der Flaeche legen
        my_painter.translate(self.width() / 2, self.height() / 2)

        my_painter.setPen(Qt.black)
        my_painter.rotate(self.scale_angle_start_value - self.angle_offset)
        steps_size = (float(self.scale_angle_size) / float(self.scala_main_count * self.scala_subdiv_count))
        scale_line_outer_start = self.widget_diameter/2
        scale_line_lenght = (self.widget_diameter / 2) - (self.widget_diameter / 40)
        for i in range((self.scala_main_count * self.scala_subdiv_count)+1):
            my_painter.drawLine(scale_line_lenght, 0, scale_line_outer_start, 0)
            my_painter.rotate(steps_size)

    def create_values_text(self):
        painter = QPainter(self)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)

        # Koordinatenursprung in die Mitte der Flaeche legen
        painter.translate(self.width() / 2, self.height() / 2)
        # painter.save()
        # xShadow = 3.0
        # yShadow = 3.0
        font = QFont(self.value_fontname, self.value_fontsize)
        fm = QFontMetrics(font)

        pen_shadow = QPen()

        pen_shadow.setBrush(self.DisplayValueColor)
        painter.setPen(pen_shadow)

        text_radius = self.widget_diameter / 2 * self.text_radius_factor

        # angle_distance = (float(self.scale_angle_size) / float(self.scala_main_count))
        # for i in range(self.scala_main_count + 1):
        text = str(int(self.value))
        w = fm.width(text) + 1
        h = fm.height()
        painter.setFont(QFont(self.value_fontname, self.value_fontsize))

        # Mitte zwischen Skalenstart und Skalenende:
        # Skalenende = Skalenanfang - 360 + Skalenlaenge
        # Skalenmitte = (Skalenende - Skalenanfang) / 2 + Skalenanfang
        angle_end = float(self.scale_angle_start_value + self.scale_angle_size - 360)
        angle = (angle_end - self.scale_angle_start_value) / 2 + self.scale_angle_start_value

        x = text_radius * math.cos(math.radians(angle))
        y = text_radius * math.sin(math.radians(angle))
        # print(w, h, x, y, text)
        text = [x - int(w/2), y - int(h/2), int(w), int(h), Qt.AlignCenter, text]
        painter.drawText(text[0], text[1], text[2], text[3], text[4], text[5])
        # painter.restore()

    def draw_big_needle_center_point(self, diameter=30):
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)

        # Koordinatenursprung in die Mitte der Flaeche legen
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        # painter.setPen(Qt.NoPen)
        painter.setBrush(self.CenterPointColor)
        # diameter = diameter # self.widget_diameter/6
        painter.drawEllipse(int(-diameter / 2), int(-diameter / 2), int(diameter), int(diameter))

    def draw_needle(self):
        painter = QPainter(self)
        # painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.Antialiasing)
        # Koordinatenursprung in die Mitte der Flaeche legen
        painter.translate(self.width() / 2, self.height() / 2)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.NeedleColor)
        painter.rotate(((self.value - self.value_offset - self.value_min) * self.scale_angle_size /
                        (self.value_max - self.value_min)) + 90 + self.scale_angle_start_value)

        painter.drawConvexPolygon(self.value_needle[0])


    def resizeEvent(self, event):
        # self.resized.emit()
        # return super(self.parent, self).resizeEvent(event)
        # print("resized")
        # print(self.width())
        self.rescale_method()
        # self.emit(SIGNAL("resize()"))
        # print("resizeEvent")
        #pass

    def paintEvent(self, event):
        # Main Drawing Event:
        # Will be executed on every change
        # vgl http://doc.qt.io/qt-4.8/qt-demos-affine-xform-cpp.html
        # print("event", event)

        # colored pie area
        if self.enable_filled_Polygon:
            self.draw_filled_polygon()

        # draw scale marker lines
        if self.enable_fine_scaled_marker:
            self.create_fine_scaled_marker()
        if self.enable_big_scaled_marker:
            self.draw_big_scaled_markter()

        # draw scale marker value text
        if self.enable_scale_text:
            self.create_scale_marker_values_text()

        # Display Value
        if self.enable_value_text:
            self.create_values_text()

        # draw needle 1
        if self.enable_Needle_Polygon:
            self.draw_needle()

        # Draw Center Point
        if self.enable_CenterPoint:
            self.draw_big_needle_center_point(diameter=(self.widget_diameter / 6))

    def setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)

        QWidget.setMouseTracking(self, flag)
        recursive_set(self)

    def mouseReleaseEvent(self, QMouseEvent):
        # print("released")
        self.NeedleColor = self.NeedleColorReleased

        if not self.use_timer_event:
            self.update()
        pass

    def mouseMoveEvent(self, event):
        x, y = event.x() - (self.width() / 2), event.y() - (self.height() / 2)
        if not x == 0:
            angle = math.atan2(y, x) / math.pi * 180
            # winkellaenge der anzeige immer positiv 0 - 360deg
            # min wert + umskalierter wert
            value = (float(math.fmod(angle - self.scale_angle_start_value + 720, 360)) / \
                     (float(self.scale_angle_size) / float(self.value_max - self.value_min))) + self.value_min
            temp = value
            fmod = float(math.fmod(angle - self.scale_angle_start_value + 720, 360))
            state = 0
            if (self.value - (self.value_max - self.value_min) * self.value_needle_snapzone) <= \
                    value <= \
                    (self.value + (self.value_max - self.value_min) * self.value_needle_snapzone):
                self.NeedleColor = self.NeedleColorDrag
                # todo: evtl ueberpruefen
                #
                state = 9
                # if value >= self.value_max and self.last_value < (self.value_max - self.value_min) / 2:
                if value >= self.value_max and self.last_value < (self.value_max - self.value_min) / 2:
                    state = 1
                    value = self.value_max
                    self.last_value = self.value_min
                    self.valueChanged.emit(int(value))
                elif value >= self.value_max >= self.last_value:
                    state = 2
                    value = self.value_max
                    self.last_value = self.value_max
                    self.valueChanged.emit(int(value))
                else:
                    state = 3
                    self.last_value = value
                    self.valueChanged.emit(int(value))
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "App"
##        self.top = 100
##        self.left = 100
##        self.width = 680
##        self.height = 500
##        self.InitUI()
        self.setStyleSheet('background-color:#f7f7ff;')
        #self.gauge=AnalogGaugeWidget()
        #self.gauge.use_timer_event=True
        #self.gauge.setGeometry(670,265,320, 340)
        #self.gauge.show()
        #self.gauge.show()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 1024, 768)
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('header.png'))
        self.label.setGeometry(0,0,1024,100)
        #self.layout = QGridLayout(self)
        #self.layout.addWidget(self.label, 0, 0)
        #self.layout.addWidget(self.gauge, 0, 1)
        self.mySubwindow=subwindow()
        #self.mySubwindow.createWindow(1024,668)
        self.mySubwindow.show()
        #self.gauge=AnalogGaugeWidget(self)
        #self.gauge.setGeometry(0,0,320, 340)
        #self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.gauge.show()
        #self.pushButton = QPushButton(self)
        #self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        #self.pushButton.setText('Click me!')
        #self.pushButton.clicked.connect(self.goMainWindow)

           
    def goMainWindow(self):
            self.mySubwindow = subwindow()
            self.mySubwindow.createWindow(1024,668)
            self.mySubwindow.show()

class subwindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(subwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()
       #self.InitUI()
       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,150,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.gauge.show()
        #self.s1 = Switch(self)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('Start Test', self)
        buttonWindow1.setFont(QFont('Arial', 27))
        buttonWindow1.setGeometry(20,60,285,155)
        buttonWindow1.setStyleSheet('background-image: url(start.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,250,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,440,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,60,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,250,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,440,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        self.show()

    def buttonWindow1_onClick(self):
        self.close()
        self.rgwindow = secondwindow()
        self.rgwindow.show()
    def settingswindow(self):
        self.close()
        self.swindow = settingswindow()
        self.swindow.show()
    def userswindow(self):
        self.close()
        self.uwindow = userswindow()
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rswindow = resultswindow()
        self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.abwindow = aboutwindow()
        self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.dwindow = damperwindow()
        self.dwindow.show()
 

class secondwindow(QWidget):
    def __init__(self,parent=None):
       super(secondwindow,self).__init__(parent) 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App2"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI1()
       
       
    def InitUI1(self):
        self.setWindowTitle(self.title)
        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('screens3.png'))
        self.label.setGeometry(0,0,1024,668)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(740,510,180,80)
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.starttest = QPushButton('Start Test', self)
        self.starttest.setGeometry(700,20,250,90)
        #self.buttonWindow12.move(100, 100)
        self.starttest.clicked.connect(self.call_first2)
        self.show()
    def call_first1(self):
        self.close()
        self.mySubwindow = subwindow()
        #self.mySubwindow.createWindow(500,400)
        self.mySubwindow.show()
    def call_first2(self):
        self.close()
        self.mySubwindow = runninggraphwindow()
        #self.mySubwindow.createWindow(500,400)
        self.mySubwindow.show()
class runninggraphwindow(QWidget):
    def __init__(self,parent=None):
       super(runninggraphwindow,self).__init__(parent) 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI1()
       
       
    def InitUI1(self):
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,0,1024,668)
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(700,100,250, 300)
        self.gauge.setStyleSheet("background-color:white;")
        #self.gauge.show()
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(70,40,550, 350)
        self.graphWidget.setBackground('w')
        #graphWidget.setStyleSheet("background-color:white;")
       #pg.setConfigOption('background', 'w')
       # pg.setConfigOption('foreground', 'k')
        self.graphWidget.showGrid(x=False,y=True)
##        plt.addLegend()
##
##        # set properties
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
##        plt.setXRange(0,10)
##        plt.setYRange(0,20)
        self.graphWidget.setWindowTitle('Temperature Graph')

        #self.graphWidget.show()
        
        #self.setCentralWidget(self.graphWidget)

        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        #self.graphWidget.plot(hour, temperature)
        self.Home = QPushButton('Home', self)
        self.Home.setGeometry(120,500,250,90)
        #self.buttonWindow12.move(100, 100)
        self.Home.clicked.connect(self.call_home)
        self.stoptest = QPushButton('Stop Test', self)
        self.stoptest.setGeometry(650,500,250,90)
        #self.buttonWindow12.move(100, 100)
        self.stoptest.clicked.connect(self.stop_test)

        self.show()
    def call_home(self):
        self.close()
        self.shomewindow = secondhomewindow()
        #self.mySubwindow.createWindow(500,400)
        self.shomewindow.show()

    def stop_test(self):
        self.close()
        #self.gauge.close()
        #self.graphWidget.close()
        self.graphresultwindow = graphresultwindow()
        #self.mySubwindow.createWindow(500,400)
        self.graphresultwindow.show()
class secondhomewindow(QWidget):
    def __init__(self,parent=None):
       super(secondhomewindow,self).__init__(parent) 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI1()
       
       
    def InitUI1(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,150,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        self.gauge.show()
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('View Running Test', self)
        buttonWindow1.setFont(QFont('Arial', 25))
        buttonWindow1.setGeometry(20,60,285,155)
        buttonWindow1.setStyleSheet('background-image: url(viewrunningtest.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,250,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,440,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,60,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,250,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,440,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        self.show()

    def buttonWindow1_onClick(self):
        self.close()
        self.rgwindow = runninggraphwindow()
        self.rgwindow.show()
    def settingswindow(self):
        self.close()
        self.swindow = settingswindow()
        self.swindow.show()
    def userswindow(self):
        self.close()
        self.uwindow = userswindow()
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rswindow = resultswindow()
        self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.abwindow = aboutwindow()
        self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.dwindow = damperwindow()
        self.dwindow.show()

class graphresultwindow(QWidget):
    def __init__(self,parent=None):
       super(graphresultwindow,self).__init__(parent) 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI1()
       
       
    def InitUI1(self):
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('resultscreen1.png'))
        self.label.setGeometry(0,0,1024,668)
        self.back = QPushButton('Home', self)
        self.back.setGeometry(80,510,180,80)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_first1)
        self.print = QPushButton('Print', self)
        self.print.setGeometry(280,510,180,80)
        self.print.setFont(QFont('Arial', 21))
        self.print.setStyleSheet('background-color:#4299ff; color: white')
        self.print.clicked.connect(self.call_first1)
        self.exportcsv = QPushButton('Export Csv', self)
        self.exportcsv.setGeometry(480,510,180,80)
        self.exportcsv.setFont(QFont('Arial', 21))
        self.exportcsv.setStyleSheet('background-color:#4299ff; color: white')
        self.exportcsv.clicked.connect(self.call_first1)
        self.exportgraph = QPushButton('Export Graph', self)
        self.exportgraph.setGeometry(680,510,180,80)
        self.exportgraph.setFont(QFont('Arial', 21))
        self.exportgraph.setStyleSheet('background-color:#4299ff; color: white')
        self.exportgraph.clicked.connect(self.call_first1)
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(550,70,420, 390)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=False,y=True)
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setWindowTitle('Temperature Graph')
        self.show()

    def call_first1(self):
        self.close()
        self.mySubwindow = subwindow()
        self.mySubwindow.show()
        
class settingswindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(settingswindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()
       #self.InitUI()
       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,0,1024,668)
        self.ins_settings = QPushButton('Instrument', self)
        self.ins_settings.setFont(QFont('Arial', 25))
        self.ins_settings.setGeometry(370,100,285,155)
        self.ins_settings.setStyleSheet('background-image: url(setting.png);')
        self.ins_settings.clicked.connect(self.instrumentsettingswindow)
        self.service = QPushButton('Service   ', self)
        self.service.setFont(QFont('Arial', 25))
        self.service.setGeometry(370,300,285,155)
        self.service.setStyleSheet('background-image: url(setting.png);')
        self.service.clicked.connect(self.servicewindow)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,490,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def instrumentsettingswindow(self):
        self.close()
        self.swindow = instrumentwindow()
        self.swindow.show()

    def servicewindow(self):
        self.close()
        self.svwindow = servicewindow()
        self.svwindow.show()
    def call_first1(self):
        self.close()
        self.mySubwindow = subwindow()
        #self.mySubwindow.createWindow(500,400)
        self.mySubwindow.show()

class servicewindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(servicewindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()

       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Enter Password',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setGeometry(400,30,220,50)
        self.textbox = QLineEdit(self)
        self.textbox.setFont(QFont('Arial', 21))
        self.textbox.setGeometry(370,150,280,60)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        self.e_password = QPushButton('Enter Password', self)
        self.e_password.setGeometry(370,270,280,100)
        self.e_password.setFont(QFont('Arial', 21))
        self.e_password.setStyleSheet('background-color:#4299ff; color: white')
        self.e_password.clicked.connect(self.call_second_service)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,400,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)
        self.show()

    def call_second_service(self):
        self.close()
        self.svwindow = second_servicewindow()
        self.svwindow.show()
    def call_back(self):
        self.close()
        self.swindow = settingswindow()
        self.swindow.show()


class second_servicewindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(second_servicewindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()

       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.background = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.background.setPixmap(QPixmap('graph_screen.png'))
        self.background.setGeometry(0,0,1024,668)
        self.label = QLabel('Service Screen',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,20,220,50)
        self.home = QPushButton('Home', self)
        self.home.setGeometry(650,60,140,70)
        self.home.setFont(QFont('Arial', 19))
        self.home.setStyleSheet('background-color:#4299ff; color: white')
        self.home.clicked.connect(self.call_home)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(820,60,140,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)
        self.language = QPushButton('Language', self)
        self.language.setGeometry(120,130,250,90)
        self.language.setFont(QFont('Arial', 21))
        self.language.setStyleSheet('background-color:#4299ff; color: white')
        self.language.clicked.connect(self.call_language)
        self.timezone = QPushButton('TimeZone', self)
        self.timezone.setGeometry(120,250,250,90)
        self.timezone.setFont(QFont('Arial', 21))
        self.timezone.setStyleSheet('background-color:#4299ff; color: white')
        self.timezone.clicked.connect(self.call_timezone)
        self.temp_limit = QPushButton('Temperature Limit', self)
        self.temp_limit.setGeometry(120,370,250,90)
        self.temp_limit.setFont(QFont('Arial', 21))
        self.temp_limit.setStyleSheet('background-color:#4299ff; color: white')
        self.temp_limit.clicked.connect(self.call_templimit)
        self.performance = QPushButton('Performance', self)
        self.performance.setGeometry(120,490,250,90)
        self.performance.setFont(QFont('Arial', 21))
        self.performance.setStyleSheet('background-color:#4299ff; color: white')
        self.performance.clicked.connect(self.call_performance)
        self.calibration = QPushButton('Calibration', self)
        self.calibration.setGeometry(410,250,250,90)
        self.calibration.setFont(QFont('Arial', 21))
        self.calibration.setStyleSheet('background-color:#4299ff; color: white')
        self.calibration.clicked.connect(self.call_calibration)
        self.password = QPushButton('Password', self)
        self.password.setGeometry(410,370,250,90)
        self.password.setFont(QFont('Arial', 21))
        self.password.setStyleSheet('background-color:#4299ff; color: white')
        self.password.clicked.connect(self.call_password)
        self.s_update = QPushButton('Software Update', self)
        self.s_update.setGeometry(410,490,250,90)
        self.s_update.setFont(QFont('Arial', 21))
        self.s_update.setStyleSheet('background-color:#4299ff; color: white')
        self.s_update.clicked.connect(self.call_update)
        self.f_reset = QPushButton('Factory Reset', self)
        self.f_reset.setGeometry(710,250,250,90)
        self.f_reset.setFont(QFont('Arial', 21))
        self.f_reset.setStyleSheet('background-color:#4299ff; color: white')
        self.f_reset.clicked.connect(self.call_factoryreset)
        self.test = QPushButton('Test Devices', self)
        self.test.setGeometry(710,370,250,90)
        self.test.setFont(QFont('Arial', 21))
        self.test.setStyleSheet('background-color:#4299ff; color: white')
        self.test.clicked.connect(self.call_testdevices)
        self.ethernet = QPushButton('Ethernet', self)
        self.ethernet.setGeometry(710,490,250,90)
        self.ethernet.setFont(QFont('Arial', 21))
        self.ethernet.setStyleSheet('background-color:#4299ff; color: white')
        self.ethernet.clicked.connect(self.call_ethernet)
        self.show()

    def call_home(self):
        self.close()
        self.svwindow = subwindow()
        self.svwindow.show()
    def call_back(self):
        self.close()
        self.swindow = servicewindow()
        self.swindow.show()
    def call_ethernet(self):
        pass
    def call_language(self):
        pass
    def call_timezone(self):
        pass
    def call_templimit(self):
        pass
    def call_performance(self):
        pass
    def call_calibration(self):
        pass
    def call_password(self):
        pass
    def call_update(self):
        pass  
    def call_factoryreset(self):
        pass
    def call_testdevices(self):
        pass

class instrumentwindow(QWidget):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,parent=None):
       #parent=None
       super(instrumentwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 668
       self.InitUI()

       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.background = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.background.setPixmap(QPixmap('graph_screen.png'))
        self.background.setGeometry(0,0,1024,668)
        self.label = QLabel('Instrument Settings',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,20,220,50)
        self.home = QPushButton('Home', self)
        self.home.setGeometry(650,80,140,70)
        self.home.setFont(QFont('Arial', 19))
        self.home.setStyleSheet('background-color:#4299ff; color: white')
        self.home.clicked.connect(self.call_home)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(820,80,140,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('background-color:#4299ff; color: white')
        self.back.clicked.connect(self.call_back)
        self.save = QPushButton('Save', self)
        self.save.setGeometry(480,80,140,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet('background-color:#4299ff; color: white')
        self.save.clicked.connect(self.call_back)
        self.c_name = QLabel('Company Name',self)
        self.c_name.setFont(QFont('Arial', 16))
        self.c_name.setStyleSheet('background-color:white; color: black')
        self.c_name.move(90,130)
        self.c_name_entry = QLineEdit(self)
        self.c_name_entry.setFont(QFont('Arial', 16))
        self.c_name_entry.setGeometry(90,170,240,40)
        self.c_name_entry.setStyleSheet('background-color:white; color: black')
        self.tele_no = QLabel('Telephone Number',self)
        self.tele_no.setFont(QFont('Arial', 16))
        self.tele_no.setStyleSheet('background-color:white; color: black')
        self.tele_no.move(90,230)
        self.tele_no_entry = QLineEdit(self)
        self.tele_no_entry.setFont(QFont('Arial', 16))
        self.tele_no_entry.setGeometry(90,270,240,40)
        self.tele_no_entry.setStyleSheet('background-color:white; color: black')
        self.time = QLabel('Time',self)
        self.time.setFont(QFont('Arial', 16))
        self.time.setStyleSheet('background-color:white; color: black')
        self.time.move(90,330)
        self.s1 = Switch(self,thumb_radius=24, track_radius=25,text='Time')
        self.s1.move(90,370)
        self.temperature = QLabel('Temperature',self)
        self.temperature.setFont(QFont('Arial', 16))
        self.temperature.setStyleSheet('background-color:white; color: black')
        self.temperature.move(90,440)
        self.s2 = Switch(self,thumb_radius=24, track_radius=25,text='Temperature')
        self.s2.move(90,480)
        self.screentimeout = QLabel('Screen Timeout',self)
        self.screentimeout.setFont(QFont('Arial', 16))
        self.screentimeout.setStyleSheet('background-color:white; color: black')
        self.screentimeout.move(500,230)
        self.b_timeout = QPushButton('Screen Timeout', self)
        self.b_timeout.setGeometry(500,280,240,90)
        self.b_timeout.setFont(QFont('Arial', 19))
        self.b_timeout.setStyleSheet('background-color:#4299ff; color: white')
        self.b_timeout.clicked.connect(self.call_home)
        self.printer = QLabel('Printer',self)
        self.printer.setFont(QFont('Arial', 16))
        self.printer.setStyleSheet('background-color:white; color: black')
        self.printer.move(500,390)
        self.b_printer = QPushButton('Select Printer', self)
        self.b_printer.setGeometry(500,440,240,90)
        self.b_printer.setFont(QFont('Arial', 19))
        self.b_printer.setStyleSheet('background-color:#4299ff; color: white')
        self.b_printer.clicked.connect(self.call_home)
        self.show()

    def call_home(self):
        self.close()
        self.svwindow = subwindow()
        self.svwindow.show()
    def call_back(self):
        self.close()
        self.swindow = settingswindow()
        self.swindow.show()
    def call_ethernet(self):
        pass
    def call_language(self):
        pass
    def call_timezone(self):
        pass
    def call_templimit(self):
        pass
    def call_performance(self):
        pass
    def call_calibration(self):
        pass
    def call_password(self):
        pass
    def call_update(self):
        pass  
    def call_factoryreset(self):
        pass
    def call_testdevices(self):
        pass
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    #my_gauge=AnalogGaugeWidget()
    #gauge.setGeometry(0,0,320, 340)
    #gauge.setStyleSheet("background-color:#f7f7ff;")
    #my_gauge.show()
    w = Window()
    w.show()
    sys.exit(app.exec_())
