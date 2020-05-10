from PyQt5.QtGui import QPixmap,QPainter,QFont,QCursor,QMovie,QTextCursor,QColor,QPen
from PyQt5.QtCore import QThread, pyqtSignal,QTimer,QTime,Qt,QRect
from PyQt5.QtWidgets import (QPlainTextEdit,QHeaderView,QScroller,QAbstractItemView,QComboBox,QGraphicsDropShadowEffect,QWidget,QMainWindow,QFrame,
  QApplication, QDialog,QProgressBar, QPushButton,QMdiSubWindow,QTreeWidget,QLabel,QLineEdit,QTreeWidgetItem,QMdiArea,QGraphicsView,QTextEdit)
from functools import partial
class arabickeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_1=""
        #self.mainwindowshow=mainwindowshow
        #self.previouswindow=previouswindow
        #self.startUI()
        self.InitUI()
    def startUI(self):

        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.label_show="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.label_show="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.label_show="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.label_show="Enter Contact"
            self.length=14
        elif(self.previouswindow=='c_name'):
            self.label_show="Enter Company Name"
            self.length=14
        elif(self.previouswindow=='pass'):
            self.label_show="Enter Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword"):
            self.label_show="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword"):
            self.label_show="Confirm Password"
            self.length=14
        elif(self.previouswindow=="currentservicepassword1"):
            self.label_show="Current Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword1"):
            self.label_show="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword1"):
            self.label_show="Confirm Password"
            self.length=14
        elif(self.previouswindow=="result"):
            self.label_show="Enter Keywords"
            self.length=14
            



    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        #self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setStyleSheet("background-color:#f8f8f8")
        self.bg.setGeometry(0,100,1024,668)

        self.label = QLabel("",self)
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 1px;')
        self.label.setGeometry(20,116,200,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setPlaceholderText("")
        #self.entry.setMaxLength(self.length)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entry_1)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton("q", self)
        q.setGeometry(59,249,82,100)
        q.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(q)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        q.setGraphicsEffect(effect)
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton("w", self)
        self.w.setGeometry(141,249,82,100)
        self.w.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.w)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.w.setGraphicsEffect(effect)
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton("e", self)
        self.e.setGeometry(223,249,82,100)
        self.e.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.e)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.e.setGraphicsEffect(effect)
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton("r", self)
        self.r.setGeometry(305,249,82,100)
        self.r.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.r)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.r.setGraphicsEffect(effect)
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('t', self)
        self.t.setGeometry(387,249,82,100)
        self.t.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.t)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.t.setGraphicsEffect(effect)
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('y', self)
        self.y.setGeometry(469,249,82,100)
        self.y.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.y)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.y.setGraphicsEffect(effect)
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('u', self)
        self.u.setGeometry(551,249,82,100)
        self.u.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.u)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.u.setGraphicsEffect(effect)
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('i', self)
        self.i.setGeometry(633,249,82,100)
        self.i.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.i)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.i.setGraphicsEffect(effect)
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton(str("o"), self)
        self.o.setGeometry(715,249,82,100)
        self.o.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.o)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.o.setGraphicsEffect(effect)
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton(str("p"), self)
        self.p.setGeometry(797,249,82,100)
        self.p.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.p)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.p.setGraphicsEffect(effect)
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)

        self.p1 = QPushButton(str("|"), self)
        self.p1.setGeometry(879,249,82,100)
        self.p1.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.p1)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.p1.setGraphicsEffect(effect)
        self.p1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.p1.clicked.connect(self.insert_text)
        
        self.a = QPushButton("a", self)
        self.a.setGeometry(59,350,82,100)
        self.a.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.a)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.a.setGraphicsEffect(effect)
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton("s", self)
        self.s.setGeometry(141,350,82,100)
        self.s.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.s)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.s.setGraphicsEffect(effect)
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton("d", self)
        self.d.setGeometry(223,350,82,100)
        self.d.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.d)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.d.setGraphicsEffect(effect)
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton("f", self)
        self.f.setGeometry(305,350,82,100)
        self.f.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.f)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.f.setGraphicsEffect(effect)
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton(("g"), self)
        self.g.setGeometry(387,350,82,100)
        self.g.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.g)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.g.setGraphicsEffect(effect)
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('h', self)
        self.h.setGeometry(469,350,82,100)
        self.h.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.h)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.h.setGraphicsEffect(effect)
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton("j", self)
        self.j.setGeometry(551,350,82,100)
        self.j.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.j)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.j.setGraphicsEffect(effect)
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('k', self)
        self.k.setGeometry(633,350,82,100)
        self.k.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.k)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.k.setGraphicsEffect(effect)
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton("l", self)
        self.l.setGeometry(715,350,82,100)
        self.l.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.l)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.l.setGraphicsEffect(effect)
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(":", self)
        self.col.setGeometry(797,350,82,100)
        self.col.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.col)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.col.setGraphicsEffect(effect)
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)

        self.col1 = QPushButton("'", self)
        self.col1.setGeometry(879,350,82,100)
        self.col1.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.col1)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.col1.setGraphicsEffect(effect)
        self.col1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.col1.clicked.connect(self.insert_text)

        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,451,82,100)
        self.shift.setFont(QFont('Arial', 38))
        effect = QGraphicsDropShadowEffect(self.shift)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.shift.setGraphicsEffect(effect)
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('z', self)
        self.z.setGeometry(140,451,82,100)
        self.z.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.z)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.z.setGraphicsEffect(effect)
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('x', self)
        self.x.setGeometry(222,451,82,100)
        self.x.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.x)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.x.setGraphicsEffect(effect)
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('c', self)
        self.c.setGeometry(304,451,82,100)
        self.c.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.c)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.c.setGraphicsEffect(effect)
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('v', self)
        self.v.setGeometry(386,451,82,100)
        self.v.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.v)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.v.setGraphicsEffect(effect)
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('b', self)
        self.b.setGeometry(468,451,82,100)
        self.b.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.b)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.b.setGraphicsEffect(effect)
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('n', self)
        self.n.setGeometry(550,451,82,100)
        self.n.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.n)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.n.setGraphicsEffect(effect)
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('m', self)
        self.m.setGeometry(632,451,82,100)
        self.m.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.m)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.m.setGraphicsEffect(effect)
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(714,451,82,100)
        self.po.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.po)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.po.setGraphicsEffect(effect)
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        
        self.clear = QPushButton('?', self)
        self.clear.setGeometry(796,451,82,100)
        self.clear.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.clear)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.clear.setGraphicsEffect(effect)
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.insert_text)
        clr=u'\u232b'
        self.clear2 = QPushButton(clr, self)
        self.clear2.setGeometry(878,451,82,100)
        self.clear2.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.clear2)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.clear2.setGraphicsEffect(effect)
        self.clear2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.clear2.clicked.connect(self.clear1)

##
        self.shift = QPushButton("!", self)
        self.shift.setGeometry(58,552,82,100)
        self.shift.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.shift)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.shift.setGraphicsEffect(effect)
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.insert_text)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('@', self)
        self.z.setGeometry(140,552,82,100)
        self.z.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.z)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.z.setGraphicsEffect(effect)
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('#', self)
        self.x.setGeometry(222,552,82,100)
        self.x.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.x)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.x.setGraphicsEffect(effect)
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('$', self)
        self.c.setGeometry(304,552,82,100)
        self.c.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.c)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.c.setGraphicsEffect(effect)
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('%', self)
        self.v.setGeometry(386,552,82,100)
        self.v.setFont(QFont('Arial', 30))
        effect = QGraphicsDropShadowEffect(self.v)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.v.setGraphicsEffect(effect)
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('^', self)
        self.b.setGeometry(468,552,82,100)
        self.b.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.b)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.b.setGraphicsEffect(effect)
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('_', self)
        self.n.setGeometry(550,552,82,100)
        self.n.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.n)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.n.setGraphicsEffect(effect)
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('*', self)
        self.m.setGeometry(632,552,82,100)
        self.m.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.m)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.m.setGraphicsEffect(effect)
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('(', self)
        self.po.setGeometry(714,552,82,100)
        self.po.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.po)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.po.setGraphicsEffect(effect)
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(')', self)
        self.clear.setGeometry(796,552,82,100)
        self.clear.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.clear)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.clear.setGraphicsEffect(effect)
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.insert_text)

        self.clear2 = QPushButton("~", self)
        self.clear2.setGeometry(878,552,82,100)
        self.clear2.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.clear2)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.clear2.setGraphicsEffect(effect)
        self.clear2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.clear2.clicked.connect(self.insert_text)
##
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,653,100,100)
        self.change.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.change)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.change.setGraphicsEffect(effect)
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(158,653,100,100)
        self.dash.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.dash)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.dash.setGraphicsEffect(effect)
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)

        self.dash = QPushButton('ARB', self)
        self.dash.setGeometry(258,653,100,100)
        self.dash.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.dash)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.dash.setGraphicsEffect(effect)
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.arbitoenglish)        
        self.space = QPushButton('space', self)
        self.space.setGeometry(358,653,340,100)
        self.space.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.space)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.space.setGraphicsEffect(effect)
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(698,653,260,100)
        self.enter.setFont(QFont('Arial', 24))
        effect = QGraphicsDropShadowEffect(self.enter)
        effect.setOffset(0, 0)
        effect.setBlurRadius(1)
        self.enter.setGraphicsEffect(effect)
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 1px;
border-radius: 10px;
border-color: gray;
padding: 4px; color: black''')
        self.enter.clicked.connect(self.enter1)
    def insert_text(self,data):
            sender = self.sender()
##            print(sender.text())
##            cursor = self.entry.cursorPosition()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
##            print('cursor',cursor)
##            self.entry.cursorWordForward(True)
##            self.entry.setCursorPosition(2)
            #self.entry.setText(str(data))
    def arbitoenglish(self):
        pass        
    def clear1(self):
        #self.entry.text=self.entry.text()[0:-2]
        print(self.entry.text()[0:-1])
        l=self.entry.text()[0:-1]
        self.entry.setText(l)
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    def enter1(self):
        if(self.previouswindow=='e_user' ):
            keydata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='e_employer'):
            keydata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='e_contact'):
            keydata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='e_designation'):
            keydata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=edituser(self.mainwindowshow,editdata='')
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='a_user' ):
            adduserdata.username = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='a_employer'):
            adduserdata.employerid = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='a_contact'):
            adduserdata.contact = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='a_designation'):
            adduserdata.designation = self.entry.text()
            #print(y.username,'ee')
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=adduser(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='c_name'):
            ins_screen.companyname=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=instrumentwindow(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
            #"faisal"="Enter Company\nName"
            #self.length=14
        elif(self.previouswindow=='pass'):
            password_screen.password=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=servicepasswordwindow(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='newservicepassword'):
            masterpassword_screen.newservicepassword=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=masterpasswordscreen(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=='confirmservicepassword'):
            masterpassword_screen.confirmservicepassword=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=masterpasswordscreen(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=="currentservicepassword1"):
            servicepassword_screen.currentservicepassword=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=servicepasswordscreen(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=="newservicepassword1"):
            servicepassword_screen.newservicepassword=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=servicepasswordscreen(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=="confirmservicepassword1"):
            servicepassword_screen.confirmservicepassword=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=servicepasswordscreen(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()
        elif(self.previouswindow=="result"):
            result_screen.result=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=result_window(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()

    def shift1(self):
        self.close()
        #self.destroy()
        #gc.collect()

        self.capital_keyboard1=capital_keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        windoww.win.addSubWindow(self.capital_keyboard1)
        self.capital_keyboard1.show()
    def change_numeric(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        windoww.win.addSubWindow(self.numerickeyboard1)
        self.numerickeyboard1.show()

import sys
import gc        
app = QApplication(sys.argv)
gc.enable()
w = arabickeyboard()
w.show()
sys.exit(app.exec_())
