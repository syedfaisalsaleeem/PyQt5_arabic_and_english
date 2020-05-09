#import RPi.GPIO as IO
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

from PyQt5.QtGui import QPixmap,QPainter,QFont,QCursor,QMovie,QTextCursor,QColor,QPen
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
class External3(QThread):
  def run(self):
    conn = sqlite3.connect("faisal.db")
    c = conn.cursor()   
    def temp():
          x_t1=temperature_read()
          time.sleep(1)
          return x_t1
    while True:
      current_temp=temp()
      now = time.time()   
      c.execute("INSERT INTO live(Date,Temperature) VALUES(?,?)",(now,float(current_temp)))
      conn.commit()
    
class External2(QThread):
    def run(self):
        try:
            def temp():
                x_t1=temp_call()
                time.sleep(1)
                return x_t1
            list_temperature=[]
            previous_error=0
            integral=0
            setpoint=starttestdata.temperature
            KP=1.5
            KI=0.01
            KD=2 #0.2
            previous_error_off=0
            integral_off=0
            k_1=0
            KP_off=10
            KI_off=0.05 #0.1
            KD_off=15
            new_1=0
            Dt=40
            IO.setmode (IO.BOARD)
            list_temperature=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            list_time=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            l_1=[]
            i=0
            m_1=0
            n=0
            previous_error_1=0
            integral_1=0
            KP_1=6.3
            KI_1=0.08
            KD_1=2 #0.2
            l_output_1=[0]
            previous_error_off_1=0
            integral_off_1=0
            my_time=0
            my_time_1=0
            IO.setwarnings(False)
            while True:     
              setpoint=set_point_original
              x=temp()
              currentTemp=x

              temp_oven=float(x)

              if temp_oven!=None and temp_oven <320 and halt_pid=='True' :

                      list_temperature.append(temp_oven)

##                      if len(list_temperature)>100:
##                        del list_temperature[0:20]

                      presentvalue=temp_oven

                      error=setpoint-presentvalue
                      integral=integral+error
                      derivative=(error-previous_error)
                      output=(KP*error)+(KI*integral)+(KD*derivative)
                      previous_error=error
                      output=int(output)
                      if(output>45 or output==45):
                          output=10
                          integral=0
                      
                          
##                      print(output, derivative,integral,KI,"output","derivative","integral")
                      #print(error,"error")
                      error_off=setpoint-presentvalue
                      integral_off=integral_off+error_off
                      derivative_off=(error_off-previous_error_off)
                      output_off=(KP_off*error_off)+(KI_off*integral_off)+(KD_off*derivative_off)
                      previous_error_off=error_off
                      output_off=int(output_off)
##                      print(output_off, derivative_off,integral_off,"output off","derivative_off","integral_off")
                      if(output_off>60 or output_off==60 ):
                          output_off=0
                          integral_off=0
                      if( output_off<0):
                          output_off=0



                      if (temp_oven<setpoint-20):
                        
                        for t_1 in range(0,5):
                            if(list_temperature[-1]>list_temperature[-3] or list_temperature[-1]==list_temperature[-3]): 
                              #print(' Not Heating')
                  

                              y=temp()
                              #print(y)
                              n=float(y)
                              n_1=round(n,1)
                              n_x=int(n)

                              list_temperature.append(n_1)


                              IO.setmode (IO.BOARD)
                              IO.setup(12,IO.OUT)
                              IO.output(12,0)
                              # if(list_stop[-1]=='close'):
                              #     halt_pid='False'
                              #     set_point_original=0
                              #     del list_temperature
                              #     list_temperature=[]
                              #     status1='halted'
                              #     IO.setmode (IO.BOARD)
                              #     IO.setup(12,IO.OUT)
                              #     IO.output(12,0)
                              #     break
         
                        for t_1 in range(0,25):
                          
                                  #print('Heating')

                                  
                                  #print(t_1)
                                  y=temp()
                                  #print(y)
                                  n=float(y)
                                  n_1=round(n,1)
                                  n_x=int(n)

                                  list_temperature.append(n_1)



                                  IO.setmode (IO.BOARD)
                                  IO.setup(12,IO.OUT)
                                  IO.output(12,1)
                                  # if(list_stop[-1]=='close'):
                                  #     halt_pid='False'
                                  #     set_point_original=0
                                  #     del list_temperature
                                  #     list_temperature=[]
                                  #     status1='halted'
                                  #     IO.setmode (IO.BOARD)
                                  #     IO.setup(12,IO.OUT)
                                  #     IO.output(12,0)
                                  #     break

                      else:
                              for t_1 in range(80,output_off,-1):
                                              if(list_temperature[-1]>list_temperature[-25] ): 
                                                    
                                                    #print(t_1)
                                                    y=temp()

                                                    #print(y)
                                                    m=float(y)
                                                    m_1=round(m,1)
                                                    m_x=int(m)
      
                                                    list_temperature.append(m_1)

                                                    IO.setmode (IO.BOARD)
                                                    IO.setup(12,IO.OUT)
                                                    IO.output(12,0)
                                                    # if(list_stop[-1]=='close'):
                                                    #     halt_pid='False'
                                                    #     IO.setmode (IO.BOARD)
                                                    #     IO.setup(12,IO.OUT)
                                                    #     IO.output(12,0)
                                                    #     break

                                                    
                                                    if (m>setpoint or m==setpoint):
                                                      integral=0
                                                      integral_off=0
                                                      my_time_2=0
                                                      #call_buzzer()

                                                      while True:
                                                        setpoint=set_point_original
                                                        #print(set_point_original,'set_point_original')
                                                        y=temp()
                                                        currentTemp=y

                                                        #print('Not Heating')


                                                        

                                                        #print(y)
                                                        #print(t_1)
                                                        q_temp=float(y)
                                                        q_temp_x=int(q_temp)

                                                        list_temperature.append(q_temp)

##                                                        if len(list_temperature)>100:
##                                                          del list_temperature[0:20]
                                                        IO.setmode (IO.BOARD)
                                                        IO.setup(12,IO.OUT)
                                                        IO.output(12,0)
                                                        presentvalue=q_temp
                                                        error_1=setpoint-presentvalue
                                                        integral_1=integral_1+error_1
                                                        derivative_1=(error_1-previous_error_1)
                                                        output_1=(KP_1*error_1)+(KI_1*integral_1)+(KD_1*derivative_1)
                                                        previous_error_1=error_1
                                                        output_1=(output_1)
                                                        l_output_1.append(output_1)
                                                        my_time_2=my_time_2+1

                                                        if(output_1>45 or output_1==45):
                                                              output_1=10
                                                              integral_1=0
                                                        if(integral_1<0):
                                                                integral_1=0
                                                        if(output_1<0):
                                                                output_1=0

                                                        # if(list_stop[-1]=='close'):
                                                        #      halt_pid='False'
                                                        #      IO.setmode (IO.BOARD)
                                                        #      IO.setup(12,IO.OUT)
                                                        #      IO.output(12,0)
                                                        #      del list_temperature
                                                        #      list_temperature=[]
                                                        #      status1='halted'
                                                        #      break

                                                          
                                                              
                                                        #print(output_1, derivative_1,integral_1,KI_1,"output","derivative","integral")
                                                        #print(l_output_1[-1],"output_1")
                                                          

                                                        if(q_temp<setpoint):
                                                                     #print('Heating')

                                                                     y=temp()
                                                                     #print(y)
                                                                     #print(new_1)
                                                                     n=float(y)
                                                                     n_x=int(n)

                                                                     list_temperature.append(n)
                                                                     IO.setmode (IO.BOARD)
                                                                     IO.setup(12,IO.OUT)
                                                                     IO.output(12,1)
                                                                     time.sleep(output_1)
                                                                     IO.setup(12,IO.OUT)
                                                                     IO.output(12,0)
                                                                     
                                                                     if (n>setpoint or n==setpoint):
                                                                      #print(setpoint,'break')
                                                                      if (n>setpoint+0.4):
                                                                        integral_1=0

                                                                     if (integral_1<0):
                                                                      integral_1=0
                                                        for new_1 in range(0,25):
                                                              if(list_temperature[-1]>list_temperature[-17] ):            

          
                                                                   #print(' Not Heating inside loop')

                                                                   
                                                                   #print(new_1)
                                                                   y=temp()
                                                                   #print(y)
                                                                   n=float(y)
                                                                   
                                                                   n_x=int(n)

                                                                   list_temperature.append(n)

                                                                   IO.setmode (IO.BOARD)
                                                                   IO.setup(12,IO.OUT)
                                                                   IO.output(12,0)
                                                                   my_time_2=my_time_2+1
                                                                   if (n>setpoint or n==setpoint):
                                                                    #print(setpoint,'break')
                                                                    #call_buzzer()
                                                                    if (n>setpoint+1.5):
                                                                      integral_1=0
                                                                    
                                                                    break
                                                                   if (integral_1<0):
                                                                    integral_1=0

                                                                   # if(list_stop[-1]=='close'):
                                                                   #       halt_pid='False'
                                                                   #       IO.setmode (IO.BOARD)
                                                                   #       IO.setup(12,IO.OUT)
                                                                   #       IO.output(12,0)
                                                                   #       del list_temperature
                                                                   #       list_temperature=[]
                                                                   #       status1='halted'
                                                                   #       break


                                                        if(q_temp<setpoint-5):
                                                            #print("totally break")
                                                            break
                              










                              for new_1 in range(0,output):
                                     #print('Heating')
                                     setpoint=set_point_original
                                     #print(set_point_original,'set_point_original')
                                     #print(new_1)
                                     y=temp()
                                     #print(y)
                                     m=float(y)
                                     
                                     m_x=int(m)

                                     list_temperature.append(m_1)

                                     IO.setmode (IO.BOARD)
                                     IO.setup(12,IO.OUT)
                                     IO.output(12,1)
                                     if(list_stop[-1]=='close'):
                                                halt_pid='False'
                                                IO.setmode (IO.BOARD)
                                                IO.setup(12,IO.OUT)
                                                IO.output(12,0)
                                                del list_temperature
                                                list_temperature=[]
                                                status1='halted'
                                                break


                                     if (m>setpoint or m==setpoint):
                                      integral=0
                                      integral_off=0
                                      my_time_2=0
                                      #call_buzzer()
                                      while True:
                                              y=temp()
                                              currentTemp=y

                                              setpoint=set_point_original
                                              q_temp=float(y)
                                              q_temp_x=int(q_temp)

                                              list_temperature.append(q_temp)

##                                              if len(list_temperature)>60:
##                                                del list_temperature[0:20]
                                              IO.setmode (IO.BOARD)
                                              IO.setup(12,IO.OUT)
                                              IO.output(12,0)
                                              presentvalue=q_temp
                                              error_1=setpoint-presentvalue
                                              integral_1=integral_1+error_1
                                              derivative_1=(error_1-previous_error_1)
                                              output_1=(KP_1*error_1)+(KI_1*integral_1)+(KD_1*derivative_1)
                                              previous_error_1=error_1
                                              output_1=(output_1)
                                              l_output_1.append(output_1)
                                              #l_output_1.append(output_1)
                                              if(output_1>45 or output_1==45):
                                                    output_1=10
                                                    integral_1=0
                                              if(integral_1<0):
                                                      integral_1=0
                                              if(output_1<0):
                                                      output_1=0
                                              # if(list_stop[-1]=='close'):
                                              #   halt_pid='False'
                                              #   IO.setmode (IO.BOARD)
                                              #   IO.setup(12,IO.OUT)
                                              #   IO.output(12,0)
                                              #   del list_temperature
                                              #   list_temperature=[]
                                              #   status1='halted'
                                              #   break
                                              if(q_temp<setpoint):  
                                                         #print('Heating')

                                                         y=temp()
                                                         #print(y)
                                                         #print(new_1)
                                                         n=float(y)
                                                         n_x=int(n)

                                                         list_temperature.append(n)

                                                         IO.setmode (IO.BOARD)
                                                         IO.setup(12,IO.OUT)
                                                         IO.output(12,1)
                                                         time.sleep(output_1)
                                                         IO.setup(12,IO.OUT)
                                                         IO.output(12,0)

                                                         if (n>setpoint or n==setpoint):
                                                          #print(setpoint,'break')
                                                          #call_buzzer()
                                                          if (n>setpoint+0.4):
                                                            integral_1=0

                                                         if (integral_1<0):
                                                          integral_1=0
                                              for new_1 in range(0,25):

                                                                if(list_temperature[-1]>list_temperature[-17] ):
                                                                
                                                                   #print(' Not Heating inside loop')


                                                                   y=temp()
                                                                   #print(y)
                                                                   #print(new_1)
                                                                   n=float(y)
                                                                   
                                                                   n_x=int(n)

                                                                   list_temperature.append(n)

                                                                   IO.setmode (IO.BOARD)
                                                                   IO.setup(12,IO.OUT)
                                                                   IO.output(12,0)
                                                                   my_time_2=my_time_2+1
                                                                   if (n>setpoint or n==setpoint):
                                                                    #print(setpoint,'break')
                                                                    #call_buzzer()
                                                                    if (n>setpoint+1.5):
                                                                      integral_1=0
                                                                    #integral_1=0
                                                                    break
                                                                   if (integral_1<0):
                                                                    integral_1=0
                                                                   # if(list_stop[-1]=='close'):
                                                                   #      halt_pid='False'
                                                                   #      IO.setmode (IO.BOARD)
                                                                   #      IO.setup(12,IO.OUT)
                                                                   #      IO.output(12,0)
                                                                   #      del list_temperature
                                                                   #      list_temperature=[]
                                                                   #      status1='halted'
                                                                   #      break


                                              if(q_temp<setpoint-5):
                                                        break
        except:
            print("error")        
        
        

class External1(QThread):
        countChanged = pyqtSignal(str)
        def run(self):
            if(starttestdata.hours!='infinity' or starttestdata.minutes !='infinity'):
                hours=int(starttestdata.hours)
                minutes=int(starttestdata.minutes)
                try:  

                                if (hours==0 and minutes!='Infinity'):
                                        for m in range(minutes):
                                                for z in range(61):

                                                    uuu=str(str(0)+'hours'+str(minutes-1)+'minutes'+str(60-z)+'seconds')
                                                    mainwindow1.lowertext=uuu
                                                    print(uuu)
                                                    #l_cool.append(uuu)
                                                    time.sleep(1)

                                                    
                                                minutes=minutes-1
                                        setstatus.status='completed'
                                        self.countChanged.emit('stop')



                                            

                                elif hours!='Infinity' and minutes!='Infinity':
                                    #gfg1=1

                                            
                                        #gfg1=1
                                
                                    for h in range( hours):
                                        for m in range(minutes):
                                            for z in range(61):

                                                uuu=str(str(hours)+'hours'+str(minutes-1)+'minutes'+str(60-z)+'seconds')
                                                mainwindow1.lowertext=uuu
                                                #print(uuu)
                                                #l_cool.append(uuu)
                                                time.sleep(1)


                                            minutes=minutes-1


                                    if(hours==1):
                                        for m in range(59):
                                                for z in range(61):
                                                    #if(len(l_cool)>2):
                                                        #del l_cool[0]
                                                    #print(str(0)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                    uuu=str(str(0)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                    mainwindow1.lowertext=uuu
                                                    print(uuu)
                                                    #l_cool.append(uuu)
                                                    time.sleep(1)

                                                minutes=minutes-1
                                        setstatus.status='completed'
                                        self.countChanged.emit('stop')

                                    else:
                                            hours=hours-1
                                            for h in range(hours):  
                                                for m in range(59):
                                                        for z in range(61):
                                                            #if(len(l_cool)>2):
                                                                #del l_cool[0]
                                                            #print(str(hours)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                            uuu=str(str(hours)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                            mainwindow1.lowertext=uuu
                                                            print(uuu)
                                                            #l_cool.append(uuu)
                                                            time.sleep(1)



                                                        minutes=minutes-1

                                                        
                                                hours=hours-1

                                            for m in range(59):
                                                    for z in range(61):
                                                        #if(len(l_cool)>2):
                                                            #del l_cool[0]
                                                        #print(str(0)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                        uuu=str(str(0)+'hours'+str(59-m)+'minutes'+str(60-z)+'seconds')
                                                        mainwindow1.lowertext=uuu
                                                        print(uuu)
                                                        #l_cool.append(uuu)
                                                        time.sleep(1)

                                                    minutes=minutes-1
                                            setstatus.status='completed'
                                            self.countChanged.emit('stop')

                                
                                elif(hours=='Infinity' and minutes=='Infinity'):
                                    print('Infinity')


                except:
                        print("error")
class exportallresults(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       #self.sUI()
       self.InitUI()

       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.label = QLabel('Export/Print Results',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)


        self.etd = QPushButton('Export All Tabular Data', self)
        self.etd.setGeometry(120,270,300,80)
        self.etd.setFont(QFont('Arial', 21))
        self.etd.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.etd.clicked.connect(self.save1)


        self.eag = QPushButton('Export All Graphs', self)
        self.eag.setGeometry(120,420,300,80)
        self.eag.setFont(QFont('Arial', 21))
        self.eag.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.eag.clicked.connect(self.save1)


        self.etp = QPushButton('Export All Test Performed', self)
        self.etp.setGeometry(120,570,300,80)
        self.etp.setFont(QFont('Arial', 21))
        self.etp.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.etp.clicked.connect(self.save1)


        self.save = QPushButton('Print All Tabular Data', self)
        self.save.setGeometry(540,270,300,80)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)
        
        self.save = QPushButton('Print All Graphs', self)
        self.save.setGeometry(540,420,300,80)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)

        self.save = QPushButton('Print All Test Performed', self)
        self.save.setGeometry(540,570,300,80)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(700,170,200,60)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def save1(self):
        pass



    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=result_window(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class point3calibration(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()
      
    def call_b(self,data):
        print("asdss",data)
        if(data=="e_p1"):
             user_data=self.e_p1.text()
             self.close()
            # self.destroy()
            # gc.collect()
            # self.nk=temperature_keyboard(self.mainwindow,data,user_data)
            # self.nk.show()
        elif(data=="e_p2"):
             user_data=self.e_p2.text()
             self.close()
            # self.destroy()
            # gc.collect()
            # self.nk=temperature_keyboard(self.mainwindow,data,user_data)
            # self.nk.show()
        elif(data=="e_p3"):
             user_data=self.e_p3.text()
             self.close()
            # self.destroy()
            # gc.collect()
            # self.nk=temperature_keyboard(self.mainwindow,data,user_data)
            # self.nk.show()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:white;')
        self.label = QLabel('3 Point Calibration',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)

        degree_sign=u'\u00B0'
        cap_degree=degree_sign+"C"
        self.label_deg_c=QLabel(self)
        self.label_deg_c.setFont(QFont('Arial', 21))
        self.label_deg_c.setStyleSheet('background-color:white; color: black')
        self.label_deg_c.setGeometry(710, 220,60,30)
        self.label_deg_c.setText(cap_degree)   

        self.p1 = QLabel('Point 1 Calibration',self)
        self.p1.setFont(QFont('Arial', 18))
        self.p1.setStyleSheet('background-color:white; color: black')
        self.p1.setGeometry(150,205,270,50)


        self.e_p1 = extQLineEdit1(self)
        self.e_p1 .setFont(QFont('Arial', 18))
        self.e_p1 .setGeometry(397,205,300,63)
        self.e_p1 .setStyleSheet('background-color:white; color: black')
        self.e_p1 .setPlaceholderText('Enter 1st point calibration')
        self.e_p1.setText("100")
        self.e_p1.setReadOnly(True)
        #self.e_p1.speak.connect(partial(self.call_b,data='e_p1'))

        self.label_deg_c2=QLabel(self)
        self.label_deg_c2.setFont(QFont('Arial', 21))
        self.label_deg_c2.setStyleSheet('background-color:white; color: black')
        self.label_deg_c2.setGeometry(710, 320,60,30)
        self.label_deg_c2.setText(cap_degree)   

        self.p2 = QLabel('Point 2 Calibration',self)
        self.p2.setFont(QFont('Arial', 18))
        self.p2.setStyleSheet('background-color:white; color: black')
        self.p2.setGeometry(150,305,270,50)


        self.e_p2 = extQLineEdit1(self)
        self.e_p2 .setFont(QFont('Arial', 18))
        self.e_p2 .setGeometry(397,305,300,63)
        self.e_p2 .setStyleSheet('background-color:white; color: black')
        self.e_p2 .setPlaceholderText('Enter 2nd point calibration')
        self.e_p2.setText("180")
        self.e_p2.setReadOnly(True)
        #self.e_p2.speak.connect(partial(self.call_b,data='e_p2'))


        self.label_deg_c3=QLabel(self)
        self.label_deg_c3.setFont(QFont('Arial', 21))
        self.label_deg_c3.setStyleSheet('background-color:white; color: black')
        self.label_deg_c3.setGeometry(710, 420,60,30)
        self.label_deg_c3.setText(cap_degree)   

        self.p3 = QLabel('Point 3 Calibration',self)
        self.p3.setFont(QFont('Arial', 18))
        self.p3.setStyleSheet('background-color:white; color: black')
        self.p3.setGeometry(150,405,270,50)


        self.e_p3 = extQLineEdit1(self)
        self.e_p3 .setFont(QFont('Arial', 18))
        self.e_p3 .setGeometry(397,405,300,63)
        self.e_p3 .setStyleSheet('background-color:white; color: black')
        self.e_p3 .setPlaceholderText('Enter 3rd point calibration')
        self.e_p3.setText("250")
        self.e_p3.setReadOnly(True)
        #self.e_p3.speak.connect(partial(self.call_b,data='e_p3'))




        self.save = QPushButton('Start Calibration', self)
        self.save.setGeometry(395,505,300,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(395,605,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)


        self.show()
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end() 
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(QPen(Qt.black, 2))
        #qp.setwidth(2)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 205, 75, 63)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 305, 75, 63)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 405, 75, 63)
  

    def save1(self):
        pass




    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=calibrationscreen(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class point2calibration(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()
      


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:white;')
        self.label = QLabel('2 Point Calibration',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)

        degree_sign=u'\u00B0'
        cap_degree=degree_sign+"C"
        self.label_deg_c=QLabel(self)
        self.label_deg_c.setFont(QFont('Arial', 21))
        self.label_deg_c.setStyleSheet('background-color:white; color: black')
        self.label_deg_c.setGeometry(710, 220,60,30)
        self.label_deg_c.setText(cap_degree)   

        self.p1 = QLabel('Point 1 Calibration',self)
        self.p1.setFont(QFont('Arial', 18))
        self.p1.setStyleSheet('background-color:white; color: black')
        self.p1.setGeometry(150,205,270,50)


        self.e_p1 = QLineEdit(self)
        self.e_p1 .setFont(QFont('Arial', 18))
        self.e_p1 .setGeometry(397,205,300,63)
        self.e_p1 .setStyleSheet('background-color:white; color: black')
        self.e_p1 .setPlaceholderText('Enter 1 point calibration')

        self.label_deg_c2=QLabel(self)
        self.label_deg_c2.setFont(QFont('Arial', 21))
        self.label_deg_c2.setStyleSheet('background-color:white; color: black')
        self.label_deg_c2.setGeometry(710, 320,60,30)
        self.label_deg_c2.setText(cap_degree)   

        self.p2 = QLabel('Point 2 Calibration',self)
        self.p2.setFont(QFont('Arial', 18))
        self.p2.setStyleSheet('background-color:white; color: black')
        self.p2.setGeometry(150,305,270,50)


        self.e_p2 = QLineEdit(self)
        self.e_p2 .setFont(QFont('Arial', 18))
        self.e_p2 .setGeometry(397,305,300,63)
        self.e_p2 .setStyleSheet('background-color:white; color: black')
        self.e_p2 .setPlaceholderText('Enter 2 point calibration')




        self.save = QPushButton('Start Calibration', self)
        self.save.setGeometry(395,405,300,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(395,505,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)


        self.show()
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end() 
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(QPen(Qt.black, 2))
        #qp.setwidth(2)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 205, 75, 63)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 305, 75, 63)
  

    def save1(self):
        pass




    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=calibrationscreen(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class point1calibration(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()
      


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:white;')
        self.label = QLabel('1 Point Calibration',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)
        degree_sign=u'\u00B0'
        cap_degree=degree_sign+"C"
        self.label_deg_c=QLabel(self)
        self.label_deg_c.setFont(QFont('Arial', 21))
        self.label_deg_c.setStyleSheet('background-color:white; color: black')
        self.label_deg_c.setGeometry(710, 220,60,30)
        self.label_deg_c.setText(cap_degree)   

        self.p1 = QLabel('Point 1 Calibration',self)
        self.p1.setFont(QFont('Arial', 18))
        self.p1.setStyleSheet('background-color:white; color: black')
        self.p1.setGeometry(150,205,270,50)



        self.e_p1 = QLineEdit(self)
        self.e_p1 .setFont(QFont('Arial', 18))
        self.e_p1 .setGeometry(397,205,300,63)
        self.e_p1 .setStyleSheet('background-color:white; color: black')
        self.e_p1 .setPlaceholderText('Enter 1 point calibration')




        self.sc = QPushButton('Start Calibration', self)
        self.sc.setGeometry(395,305,300,70)
        self.sc.setFont(QFont('Arial', 21))
        self.sc.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.sc.clicked.connect(self.save1)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(395,405,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)


        self.show()
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end() 
    def drawRectangles(self, qp):
      
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(QPen(Qt.black, 2))
        #qp.setwidth(2)

        qp.setBrush(QColor(255, 255, 255))
        qp.drawRect(697, 205, 75, 63)
  

    def save1(self):
        pass




    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=calibrationscreen(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class masterpassword_screen():
    newservicepassword=''
    confirmservicepassword=''

class masterpasswordscreen(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()
       
    def call_b(self,data):
        #print("asdss",data)
        if(data=="newservicepassword"):
            user_data=self.e_nsp.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="confirmservicepassword"):
            user_data=self.e_cp.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.label = QLabel('Master Password',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)    

        self.nsp = QLabel('New Service Password',self)
        self.nsp.setFont(QFont('Arial', 18))
        self.nsp.setStyleSheet('background-color:white; color: black')
        self.nsp.setGeometry(90,220,270,50)


        self.cp = QLabel('Confirm Password',self)
        self.cp.setFont(QFont('Arial', 18))
        self.cp.setStyleSheet('background-color:white; color: black')
        self.cp.setGeometry(90,340,270,50)


        self.e_nsp = extQLineEdit1(self)
        self.e_nsp .setFont(QFont('Arial', 18))
        self.e_nsp .setGeometry(390,220,500,53)
        self.e_nsp .setStyleSheet('background-color:white; color: black')
        self.e_nsp .setPlaceholderText('Enter New Service Password')
        self.e_nsp.setReadOnly(True)
        self.e_nsp.setEchoMode(QLineEdit.Password)
        self.e_nsp.setText(masterpassword_screen.newservicepassword)
        self.e_nsp.speak.connect(partial(self.call_b,data='newservicepassword'))

        self.e_cp = extQLineEdit1(self)
        self.e_cp.setFont(QFont('Arial', 18))
        self.e_cp.setGeometry(390,340,500,53)
        self.e_cp.setStyleSheet('background-color:white; color: black')
        self.e_cp.setPlaceholderText('Enter Confirm Password')
        self.e_cp.setReadOnly(True)
        self.e_cp.setEchoMode(QLineEdit.Password)
        self.e_cp.setText(masterpassword_screen.confirmservicepassword)
        self.e_cp.speak.connect(partial(self.call_b,data='confirmservicepassword'))


        self.save = QPushButton('Save', self)
        self.save.setGeometry(450,435,300,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(450,535,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def save1(self):


        if(len(self.e_nsp.text())==0 or len(self.e_cp.text())==0 ):

            self.popup1=popup1(name='              Please Enter All Values',name2='Close')
            self.popup1.show()

        elif(self.e_nsp.text()!=self.e_cp.text()):

            self.popup1=popup1(name="      New password does not matched\n      confirmed password!",name2='Close')
            self.popup1.show()


        else:

            conn = sqlite3.connect('faisal.db')
            c = conn.cursor() 
            c.execute(f"Update password set normal='{self.e_cp.text()}' where key=1")
            conn.commit()
            c.close()               
            conn.close()
            self.popup1=popup2(name="              Password has been updated!",name2='Close')
            self.popup1.show()
            self.close()
            #self.destroy()
            #gc.collect()
            masterpassword_screen.newservicepassword=''
            masterpassword_screen.confirmservicepassword=''
            self.userswindow=servicepasswordwindow(self.mainwindow)
            windoww.win.addSubWindow(self.userswindow)
            self.userswindow.show()



    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         masterpassword_screen.newservicepassword=''
         masterpassword_screen.confirmservicepassword=''
         self.userswindow=servicepasswordwindow(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class servicepassword_screen():
    currentservicepassword=''
    newservicepassword=''
    confirmservicepassword=''
class servicepasswordscreen(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.sUI()
       self.InitUI()
    def call_b(self,data):
        if(data=="currentservicepassword1"):
            user_data=self.e_cp.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="newservicepassword1"):
            user_data=self.e_np.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="confirmservicepassword1"):
            user_data=self.e_cnp.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        m=c.execute("Select normal from password where  key=1")
        
        for z in m:
            #print(z[0],'bool1')
            self.passwordoriginal=z[0]
            print(self.passwordoriginal)

        conn.commit()
        c.close()
        conn.close()

       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.label = QLabel('New Service Password',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(410,120,300,50)

        self.lcp = QLabel('Enter Current Password',self)
        self.lcp.setFont(QFont('Arial', 18))
        self.lcp.setStyleSheet('background-color:white; color: black')
        self.lcp.setGeometry(90,220,270,50)


        self.lnp = QLabel('Enter New Password',self)
        self.lnp.setFont(QFont('Arial', 18))
        self.lnp.setStyleSheet('background-color:white; color: black')
        self.lnp.setGeometry(90,340,270,50)


        self.lcnp = QLabel('Confirm new Password',self)
        self.lcnp.setFont(QFont('Arial', 18))
        self.lcnp.setStyleSheet('background-color:white; color: black')
        self.lcnp.setGeometry(90,460,270,50)

        self.e_cp = extQLineEdit1(self)
        self.e_cp .setFont(QFont('Arial', 18))
        self.e_cp .setGeometry(390,220,500,53)
        self.e_cp .setStyleSheet('background-color:white; color: black')
        self.e_cp .setPlaceholderText('Enter Current Service Password')
        self.e_cp.setReadOnly(True)
        self.e_cp.setEchoMode(QLineEdit.Password)
        self.e_cp.setText(servicepassword_screen.currentservicepassword)
        self.e_cp.speak.connect(partial(self.call_b,data='currentservicepassword1'))

        self.e_np = extQLineEdit1(self)
        self.e_np.setFont(QFont('Arial', 18))
        self.e_np.setGeometry(390,340,500,53)
        self.e_np.setStyleSheet('background-color:white; color: black')
        self.e_np.setPlaceholderText('Enter New Password')
        self.e_np.setReadOnly(True)
        self.e_np.setEchoMode(QLineEdit.Password)
        self.e_np.setText(servicepassword_screen.newservicepassword)
        self.e_np.speak.connect(partial(self.call_b,data='newservicepassword1'))

        self.e_cnp = extQLineEdit1(self)
        self.e_cnp.setFont(QFont('Arial', 18))
        self.e_cnp.setGeometry(390,460,500,53)
        self.e_cnp.setStyleSheet('background-color:white; color: black')
        self.e_cnp.setPlaceholderText('Confirm New Password')
        self.e_cnp.setEchoMode(QLineEdit.Password)
        self.e_cnp.setText(servicepassword_screen.confirmservicepassword)
        self.e_cnp.speak.connect(partial(self.call_b,data='confirmservicepassword1'))

        self.save = QPushButton('Save', self)
        self.save.setGeometry(450,535,300,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.save.clicked.connect(self.save1)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(450,635,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def save1(self):
        if(self.e_cp.text()!=self.passwordoriginal):

            self.popup1=popup1(name='Please Enter Correct Previous Password! ',name2='Close')
            self.popup1.show()


        elif(len(self.e_cp.text())==0 or len(self.e_np.text())==0 or len(self.e_cnp.text())==0):

            self.popup1=popup1(name='              Please Enter All Values',name2='Close')
            self.popup1.show()

        elif(self.e_np.text()!=self.e_cnp.text()):

            self.popup1=popup1(name="      New password does not matched\n      confirmed password!",name2='Close')
            self.popup1.show()


        elif(self.passwordoriginal==self.e_np.text() or self.passwordoriginal==self.e_cnp.text()):
            self.popup1=popup1(name="        You cannot set the current password! ",name2='Close')
            self.popup1.show()

            
        else:

            conn = sqlite3.connect('faisal.db')
            c = conn.cursor() 
            c.execute(f"Update password set normal='{self.e_cnp.text()}' where key=1")
            conn.commit()
            c.close()               
            conn.close()
            self.popup1=popup2(name="              Password has been updated!",name2='Close')
            self.popup1.show()
            self.close()
            #self.destroy()
            #gc.collect()
            servicepassword_screen.currentservicepassword=''
            servicepassword_screen.newservicepassword=''
            servicepassword_screen.confirmservicepassword=''
            self.userswindow=second_servicewindow(self.mainwindow)
            windoww.win.addSubWindow(self.userswindow)
            self.userswindow.show()



    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         servicepassword_screen.currentservicepassword=''
         servicepassword_screen.newservicepassword=''
         servicepassword_screen.confirmservicepassword=''
         self.userswindow=second_servicewindow(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class performance(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.sUI()
       self.InitUI()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        m=c.execute("SELECT COUNT(*) FROM result WHERE Status='halted'")

        for r in m:
            self.halted=r[0]

        m=c.execute("SELECT COUNT(*) FROM result WHERE Status='completed'")
        for r in m:
            self.completed=r[0]
        conn.commit()
        c.close()
        conn.close()
        self.total=self.completed+self.halted
       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.label = QLabel('Performance',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,120,220,50)

        self.ttp = QLabel('Total Test Performed :',self)
        self.ttp.setFont(QFont('Arial', 19))
        self.ttp.setStyleSheet('background-color:white; color: black')
        self.ttp.move(120,300)
        
        self.ttc = QLabel('Total Test Completed : ',self)
        self.ttc.setFont(QFont('Arial', 19))
        self.ttc.setStyleSheet('background-color:white; color: black')
        self.ttc.move(120,370)
        
        self.tth = QLabel('Total Test Halted : ',self)
        self.tth.setFont(QFont('Arial', 19))
        self.tth.setStyleSheet('background-color:white; color: black')
        self.tth.move(120,440)

        self.ttp1 = QLabel(self)
        self.ttp1.setFont(QFont('Arial', 19))
        self.ttp1.setStyleSheet('background-color:white; color: black')
        self.ttp1.move(400,300)
        self.ttp1.setText(str(self.total))
        
        self.ttc1 = QLabel(self)
        self.ttc1.setFont(QFont('Arial', 19))
        self.ttc1.setStyleSheet('background-color:white; color: black')
        self.ttc1.move(400,370)
        self.ttc1.setText(str(self.completed))
        
        self.tth1 = QLabel(self)
        self.tth1.setFont(QFont('Arial', 19))
        self.tth1.setStyleSheet('background-color:white; color: black')
        self.tth1.move(400,440)
        self.tth1.setText(str(self.halted))

        self.back = QPushButton('Back', self)
        self.back.setGeometry(700,230,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()

    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=second_servicewindow(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class alarmscreen(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Alarm Warning',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
    

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Date','Time','Alarm Status','Duration'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(3, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(4, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(5, QHeaderView.Stretch)
        self.dataView.setColumnCount(5)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
    #@QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
        pass
                #print(i,x)
                #c_timezone=list(set(pytz.common_timezones))
                #c_timezone.sort()  
                #l=[]
                #cplusminus=u'\u00B1'
                #vartemplimit=[cplusminus+' 2 Temperature',cplusminus+' 3 Temperature',cplusminus+' 4 Temperature',cplusminus+' 5 Temperature']
                #for i,x in enumerate(vartemplimit):
                #    QTreeWidgetItem(self.dataView,[str(i),x])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=notification1(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class powerscreen(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Electricity Faliure',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
    

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Date','Time','Power'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(3, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(4, QHeaderView.Stretch)
        self.dataView.setColumnCount(4)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
    #@QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
        pass
                #print(i,x)
                #c_timezone=list(set(pytz.common_timezones))
                #c_timezone.sort()  
                #l=[]
                #cplusminus=u'\u00B1'
                #vartemplimit=[cplusminus+' 2 Temperature',cplusminus+' 3 Temperature',cplusminus+' 4 Temperature',cplusminus+' 5 Temperature']
                #for i,x in enumerate(vartemplimit):
                #    QTreeWidgetItem(self.dataView,[str(i),x])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=notification1(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class calibrationscreen(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()

       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.label = QLabel('Calibration',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(460,120,220,50)
    
        self.c1 = QPushButton('1 Point Calibration', self)
        self.c1 .setGeometry(390,185,300,120)
        self.c1 .setFont(QFont('Arial', 21))
        self.c1 .setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.c1 .clicked.connect(self.p1calib)

        self.c2 = QPushButton('2 Point Calibration', self)
        self.c2 .setGeometry(390,330,300,120)
        self.c2 .setFont(QFont('Arial', 21))
        self.c2 .setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.c2.clicked.connect(self.p2calib)

        self.c3 = QPushButton('3 Point Calibration', self)
        self.c3.setGeometry(390,480,300,120)
        self.c3.setFont(QFont('Arial', 21))
        self.c3.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.c3.clicked.connect(self.p3calib)
        

        self.back = QPushButton('Back', self)
        self.back.setGeometry(400,635,300,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()

    def p1calib(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=point1calibration(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def p2calib(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=point2calibration(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
        
    def p3calib(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=point3calibration(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()

    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=second_servicewindow(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
class testing(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       
       self.InitUI()
       #self.InitUI()
       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.ins_settings = QPushButton(' Printer Testing', self)
        self.ins_settings.setFont(QFont('Arial', 25))
        self.ins_settings.setGeometry(370,200,285,125)
        self.ins_settings.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.ins_settings.clicked.connect(self.instrumentsettingswindow)
        self.service = QPushButton('Buzzer Testing', self)
        self.service.setFont(QFont('Arial', 25))
        self.service.setGeometry(370,400,285,125)
        self.service.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.service.clicked.connect(self.servicewindow)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,590,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def instrumentsettingswindow(self):
        pass
        # self.close()
        # self.destroy()
        # gc.collect()
        # self.swindow = instrumentwindow(self.mainwindow)
        # self.swindow.show()

    def servicewindow(self):
        pass
        
        # self.close()
        # self.destroy()
        # gc.collect()
        # self.svwindow = servicepasswordwindow(self.mainwindow)
        # self.svwindow.show()
    def call_first1(self):
         self.close()
         #self.destroy()
         #gc.collect()
         self.userswindow=second_servicewindow(self.mainwindow)
         windoww.win.addSubWindow(self.userswindow)
         self.userswindow.show()
        # self.mainwindow.show()
class notification1(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       
       self.InitUI()
       #self.InitUI()
       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.b_power = QPushButton('Power Failure', self)
        self.b_power.setFont(QFont('Arial', 25))
        self.b_power.setGeometry(370,200,285,125)
        self.b_power.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.b_power.clicked.connect(self.power)
        
        self.b_alarm = QPushButton('Alarm', self)
        self.b_alarm.setFont(QFont('Arial', 25))
        self.b_alarm.setGeometry(370,400,285,125)
        self.b_alarm.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.b_alarm.clicked.connect(self.alarm1)
        
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,590,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def power(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.swindow = powerscreen(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()

    def alarm1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.swindow = alarmscreen(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()

    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()
class selecttemperaturelimit(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Temperature Limit',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Save', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_save)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Select Temperature Limit'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
   # @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
                #print(i,x)
                #c_timezone=list(set(pytz.common_timezones))
                #c_timezone.sort()  
                #l=[]
                cplusminus=u'\u00B1'
                vartemplimit=[cplusminus+' 2 Temperature',cplusminus+' 3 Temperature',cplusminus+' 4 Temperature',cplusminus+' 5 Temperature']
                for i,x in enumerate(vartemplimit):
                    QTreeWidgetItem(self.dataView,[str(i),x])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=second_servicewindow(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class selecttimezone(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Select TimeZone',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Save', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_save)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Select TimeZone'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
    #@QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
                #print(i,x)
                c_timezone=list(set(pytz.common_timezones))
                c_timezone.sort()  
                #l=[]
                for i,x in enumerate(c_timezone):
                    QTreeWidgetItem(self.dataView,[str(i),x])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=second_servicewindow(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class selectlanguage(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Select Language',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Save', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_save)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Select Language'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
   # @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
                #print(i,x)
                QTreeWidgetItem(self.dataView,['1','English'])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=second_servicewindow(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class selectscreentimeout(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Screen TimeOut',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Save', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_save)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Screen TimeOut'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
   # @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
                #print(i,x)
                QTreeWidgetItem(self.dataView,['1','never'])
                QTreeWidgetItem(self.dataView,['2','5 minutes'])
                QTreeWidgetItem(self.dataView,['3',"10 minutes"])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=instrumentwindow(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()
class selectprinter(QMdiSubWindow):
    def __init__(self,mainwindow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindow=mainwindow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Select Printer',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Save', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_save)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','Select Printer'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
   # @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
         
    def insert_data(self):
                #print(i,x)
                QTreeWidgetItem(self.dataView,['1','HP_LaserJet_Pro_M12a'])
                QTreeWidgetItem(self.dataView,['2','HP_Deskjet_Ink_Advantage_2138_All-in_one_Printer'])
                QTreeWidgetItem(self.dataView,['3',"HP_DeskJet_2130_series"])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=instrumentwindow(self.mainwindow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_save(self):
        pass
        #global getChildNode
        #self.close()
        #starttestdata.username=getChildNode
        #self.userswindow=startwindow(self.mainwindowshow)
       #self.userswindow.show()

class second_servicewindow(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()

       
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.background = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.background.setPixmap(QPixmap('graph_screen.png'))
        self.background.setGeometry(0,100,1024,668)
        self.label = QLabel('Service Screen',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,120,220,50)
        self.home = QPushButton('Home', self)
        self.home.setGeometry(650,160,140,70)
        self.home.setFont(QFont('Arial', 19))
        self.home.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.home.clicked.connect(self.call_home)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(820,160,140,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        self.language = QPushButton('Language', self)
        self.language.setGeometry(120,230,250,90)
        self.language.setFont(QFont('Arial', 21))
        self.language.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.language.clicked.connect(self.call_language)
        self.timezone = QPushButton('TimeZone', self)
        self.timezone.setGeometry(120,350,250,90)
        self.timezone.setFont(QFont('Arial', 21))
        self.timezone.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.timezone.clicked.connect(self.call_timezone)
        self.temp_limit = QPushButton('Temperature Limit', self)
        self.temp_limit.setGeometry(120,470,250,90)
        self.temp_limit.setFont(QFont('Arial', 21))
        self.temp_limit.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.temp_limit.clicked.connect(self.call_templimit)
        self.performance = QPushButton('Performance', self)
        self.performance.setGeometry(120,590,250,90)
        self.performance.setFont(QFont('Arial', 21))
        self.performance.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.performance.clicked.connect(self.call_performance)
        self.calibration = QPushButton('Calibration', self)
        self.calibration.setGeometry(410,350,250,90)
        self.calibration.setFont(QFont('Arial', 21))
        self.calibration.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.calibration.clicked.connect(self.call_calibration)
        self.password = QPushButton('Password', self)
        self.password.setGeometry(410,470,250,90)
        self.password.setFont(QFont('Arial', 21))
        self.password.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.password.clicked.connect(self.call_password)
        self.s_update = QPushButton('Software Update', self)
        self.s_update.setGeometry(410,590,250,90)
        self.s_update.setFont(QFont('Arial', 21))
        self.s_update.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.s_update.clicked.connect(self.call_update)
        self.f_reset = QPushButton('Factory Reset', self)
        self.f_reset.setGeometry(710,350,250,90)
        self.f_reset.setFont(QFont('Arial', 21))
        self.f_reset.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.f_reset.clicked.connect(self.call_factoryreset)
        self.test = QPushButton('Test Devices', self)
        self.test.setGeometry(710,470,250,90)
        self.test.setFont(QFont('Arial', 21))
        self.test.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.test.clicked.connect(self.call_testdevices)
        self.ethernet = QPushButton('Ethernet', self)
        self.ethernet.setGeometry(710,590,250,90)
        self.ethernet.setFont(QFont('Arial', 21))
        self.ethernet.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.ethernet.clicked.connect(self.call_ethernet)
        self.show()

    def call_home(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()
        #self.svwindow = subwindow()
        #self.svwindow.show()
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.swindow = settingswindow(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()
    def call_ethernet(self):
        pass
    def call_language(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_l=selectlanguage(self.mainwindow)
        windoww.win.addSubWindow(self.s_l)
        self.s_l.show()
        
    def call_timezone(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_tz=selecttimezone(self.mainwindow)
        windoww.win.addSubWindow(self.s_tz)
        self.s_tz.show()
    def call_templimit(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_tz=selecttemperaturelimit(self.mainwindow)
        windoww.win.addSubWindow(self.s_tz)
        self.s_tz.show()
    def call_performance(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_tz=performance(self.mainwindow)
        windoww.win.addSubWindow(self.s_tz)
        self.s_tz.show()
        
    def call_calibration(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_tz=calibrationscreen(self.mainwindow)
        windoww.win.addSubWindow(self.s_tz)
        self.s_tz.show()

    def call_password(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_tz=servicepasswordscreen(self.mainwindow)
        windoww.win.addSubWindow(self.s_tz)
        self.s_tz.show()
    def call_update(self):
        pass
    def delete_data(self):
            pass
    def call_stopfinal(self):
                self.delete_data()
                self.popup1=popup1()
                #a.close()
                #a.destroy()
                
                #self.close()
                #self.destroy()
                #gc.collect()

    def popup_factoryreset(self):
            def call_no():
                a.close()
                a.destroy()
                gc.collect()

                #pass
            #print("popup")
            a=QFrame()
            a.setGeometry(237,209,550,350)
            a.setWindowModality(Qt.ApplicationModal)
            a.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
            a.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(a)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Error',a)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel('Are you sure you want to factory reset!',a)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            yes_delete = QPushButton('Yes !', a)
            yes_delete .setGeometry(50,240,240,90)
            yes_delete .setFont(QFont('Arial', 21))
            yes_delete .setStyleSheet('background-color:#d00403; color: white')
            yes_delete .clicked.connect(self.call_stopfinal)
            yes_delete .clicked.connect(call_no)
            no = QPushButton('No', a)
            no.setGeometry(270,240,240,90)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(call_no)
            a.show()  
    def call_factoryreset(self):
        self.popup_factoryreset()
    def call_testdevices(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.t=testing(self.mainwindow)
        windoww.win.addSubWindow(self.t)
        self.t.show()

class servicepasswordwindow(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.startUI()
       self.InitUI()
    def call_b(self,data):
        print("asdss",data)
        if(data=="pass"):
            user_data=self.textbox.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()

    def startUI(self):
        self.master_password=''
        self.normal_password=''
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        y=c.execute("Select * from password where  key=1")
        for x in y:
                self.master_password=x[0]
                self.normal_password=x[1]

        conn.commit()
        c.close()
        conn.close()   
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Enter Password',self)
        self.label.setFont(QFont('Arial', 21))
        self.label.setGeometry(400,130,220,50)
        self.textbox = extQLineEdit1(self)
        self.textbox.setFont(QFont('Arial', 21))
        self.textbox.setGeometry(370,250,280,60)
        self.textbox.setReadOnly(True)
        self.textbox.setEchoMode(QLineEdit.Password)
        self.textbox.setText(password_screen.password)
        self.textbox.speak.connect(partial(self.call_b,data='pass'))
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        self.e_password = QPushButton('Enter Password', self)
        self.e_password.setGeometry(370,370,280,100)
        self.e_password.setFont(QFont('Arial', 21))
        self.e_password.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.e_password.clicked.connect(self.call_second_service)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,500,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        self.show()

    def call_second_service(self):
        p_t=self.textbox.text()
        if(p_t==self.master_password):
            self.close()
            #self.destroy()
            #gc.collect()
            password_screen.password=''
            self.s_sw=masterpasswordscreen(self.mainwindow)
            windoww.win.addSubWindow(self.s_sw)
            self.s_sw.show()
        elif(p_t==self.normal_password):
            self.close()
            #self.destroy()
            #gc.collect()
            password_screen.password=''
            self.s_sw=second_servicewindow(self.mainwindow)
            windoww.win.addSubWindow(self.s_sw)
            self.s_sw.show()
        else:                       
            self.popup1=popup1(name='    You have entered the wrong password',name2='Close')
            self.popup1.show()

        #self.close()
        #self.svwindow = second_servicewindow()
        #self.svwindow.show()
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        password_screen.password=''
        self.swindow = settingswindow(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()

class settingswindow(QMdiSubWindow):

    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       
       self.InitUI()
       #self.InitUI()
       


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        self.ins_settings = QPushButton('Instrument', self)
        self.ins_settings.setFont(QFont('Arial', 25))
        self.ins_settings.setGeometry(370,200,285,155)
        self.ins_settings.setStyleSheet('background-image: url(setting.png);')
        self.ins_settings.clicked.connect(self.instrumentsettingswindow)
        self.service = QPushButton('Service   ', self)
        self.service.setFont(QFont('Arial', 25))
        self.service.setGeometry(370,400,285,155)
        self.service.setStyleSheet('background-image: url(setting.png);')
        self.service.clicked.connect(self.servicewindow)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(370,590,280,100)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.back.clicked.connect(self.call_first1)
        self.show()


    def instrumentsettingswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.swindow = instrumentwindow(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()

    def servicewindow(self):
        
        self.close()
        #self.destroy()
        #gc.collect()
        self.svwindow = servicepasswordwindow(self.mainwindow)
        windoww.win.addSubWindow(self.svwindow)
        self.svwindow.show()
    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()


class instrumentwindow(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self,mainwindow):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.sUI()
       self.InitUI()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        m=c.execute("Select * from temperature where  key=1")
        
        for z in m:
            print(z[0],'bool1')
            self.set1=z[0]
        m1=c.execute("Select * from time where  key=1")
        for z1 in m1:
            self.set2=z1[0]
        conn.commit()
        c.close()
        conn.close()
        # if(self.set1=='1' or self.set2=='1'):
        #     self.set1=1
            
        # elif(self.set1=='0' or self.set2=='0'):
        #     self.set1=0 
        #     self.set2=0
        # elif(self.set2=='1'):
        #     self.set2=1  
    def call_b(self,data):
        print("asdss",data)
        if(data=="c_name"):
            user_data=self.c_name_entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="tele_no"):
            user_data=self.tele_no_entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=contactkeyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()

    #     conn = sqlite3.connect('faisal.db')
    #     c = conn.cursor()
    #     y=c.execute("Select * from instrument where  key=1")

    #     for x in y:
    #             #print(x,x[0])
    #             self.c_name_entry.setText(x[0])
    #             ins_screen.c_name=x[0]
    #             self.tele_no_entry.setText(x[1])

    #     conn.commit()
    #     c.close()
    #     conn.close()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.background = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.background.setPixmap(QPixmap('graph_screen.png'))
        self.background.setGeometry(0,100,1024,668)
        self.label = QLabel('Instrument Settings',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(400,120,220,50)
        self.home = QPushButton('Home', self)
        self.home.setGeometry(650,180,140,70)
        self.home.setFont(QFont('Arial', 19))
        self.home.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.home.clicked.connect(self.call_home)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(820,180,140,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        self.save = QPushButton('Save', self)
        self.save.setGeometry(480,180,140,70)
        self.save.setFont(QFont('Arial', 21))
        self.save.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.save.clicked.connect(self.save1)
        self.c_name = QLabel('Company Name',self)
        self.c_name.setFont(QFont('Arial', 16))
        self.c_name.setStyleSheet('background-color:white; color: black')
        self.c_name.setGeometry(90,230,220,50)
        self.c_name_entry = extQLineEdit1(self)
        self.c_name_entry.setFont(QFont('Arial', 16))
        self.c_name_entry.setGeometry(90,270,240,40)
        self.c_name_entry.setStyleSheet('background-color:white; color: black')
        self.c_name_entry.setReadOnly(True)
        self.c_name_entry.setText(ins_screen.companyname)
        self.c_name_entry.speak.connect(partial(self.call_b,data='c_name'))
        self.tele_no = QLabel('Telephone Number',self)
        self.tele_no.setFont(QFont('Arial', 16))
        self.tele_no.setStyleSheet('background-color:white; color: black')
        self.tele_no.setGeometry(90,330,220,50)
        self.tele_no_entry = extQLineEdit1(self)
        self.tele_no_entry.setFont(QFont('Arial', 16))
        self.tele_no_entry.setGeometry(90,370,240,40)
        self.tele_no_entry.setStyleSheet('background-color:white; color: black')
        self.tele_no_entry.setReadOnly(True)
        self.tele_no_entry.setText(ins_screen.telephoneno)
        self.tele_no_entry.speak.connect(partial(self.call_b,data='tele_no'))
        self.time = QLabel('Time',self)
        self.time.setFont(QFont('Arial', 16))
        self.time.setStyleSheet('background-color:white; color: black')
        self.time.setGeometry(90,430,220,50)
        self.s1 = Switch(self,thumb_radius=24, track_radius=25,text='Time')
        self.s1.setGeometry(90,470,120,50)
        self.s1.setChecked(bool(self.set2)) 
        self.s1.clicked.connect(lambda set2: self.time_change(set2))
        self.temperature = QLabel('Temperature',self)
        self.temperature.setFont(QFont('Arial', 16))
        self.temperature.setStyleSheet('background-color:white; color: black')
        self.temperature.setGeometry(90,540,220,50)
        self.s2 = Switch(self,thumb_radius=24, track_radius=25,text='Temperature')
        self.s2.setGeometry(90,580,120,50)
        print(bool(self.set1),'bool')
        self.s2.setChecked(bool(self.set1)) 
        self.s2.clicked.connect(lambda set1: self.temp_change(set1))
        #self.s2.clicked.connect(self.temp_change)
        
        #mm=self.s2.text()
        #print(mm)
        obj_Disk = psutil.disk_usage('/')
        self.progress_l = QLabel('Disk Storage',self)
        self.progress_l.setFont(QFont('Arial', 16))
        self.progress_l .setStyleSheet('background-color:white; color: black')
        self.progress_l .setGeometry(90,640,220,50)
        self.progress = QProgressBar(self)
        self.progress.setGeometry(90, 680, 300, 25)
        self.progress.setMaximum(100)
        self.progress.setValue(obj_Disk.percent) 
        self.screentimeout = QLabel('Screen Timeout',self)
        self.screentimeout.setFont(QFont('Arial', 16))
        self.screentimeout.setStyleSheet('background-color:white; color: black')
        self.screentimeout.setGeometry(500,330,220,50)
        self.b_timeout = QPushButton('Screen Timeout', self)
        self.b_timeout.setGeometry(500,380,240,90)
        self.b_timeout.setFont(QFont('Arial', 19))
        self.b_timeout.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.b_timeout.clicked.connect(self.call_screentimeout)
        self.printer = QLabel('Printer',self)
        self.printer.setFont(QFont('Arial', 16))
        self.printer.setStyleSheet("background-color:white;color:black;")
# "font: 14pt \"Arial\";\n"
# "border-width: 1px;\n"
# "border-radius: 15px;\n"
# "border-color: black;\n"
# "padding: 4px; color: black")
        self.printer.setGeometry(500,490,220,50)
        self.b_printer = QPushButton('Select Printer', self)
        self.b_printer.setGeometry(500,540,240,90)
        self.b_printer.setFont(QFont('Arial', 19))
        self.b_printer.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.b_printer.clicked.connect(self.call_printer)
        #self.startUI()
        self.show()
    def temp_change(self,set1):
        print(set1)
        if (set1==True):
            self.set1=1
        elif (set1==False):
            self.set1=0
    def time_change(self,set2):
        #print(set1)
        if (set2==True):
            self.set2=1
        elif (set2==False):
            self.set2=0


    def call_printer(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_p=selectprinter(self.mainwindow)
        windoww.win.addSubWindow(self.s_p)
        self.s_p.show()
    def call_screentimeout(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_t=selectscreentimeout(self.mainwindow)
        windoww.win.addSubWindow(self.s_t)
        self.s_t.show()
    def call_home(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.swindow = settingswindow(self.mainwindow)
        windoww.win.addSubWindow(self.swindow)
        self.swindow.show()
    def save1(self):
        mg=self.c_name_entry.text()
        mg1=self.tele_no_entry.text()
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update instrument set Company='{mg}',Telephone='{mg1}' where Key=1")
        c.execute(f"Update temperature set degree='{self.set1}' where Key=1")
        c.execute(f"Update time set t1='{self.set2}' where Key=1")
        #         conn = sqlite3.connect('faisal.db')
        # c = conn.cursor() 
        
        # conn.commit()
        # c.close()               
        # conn.close()

        conn.commit()
        c.close()               
        conn.close()
        self.popup1=popup2(name='      Your Configuration has been saved',name2='Close')
        self.popup1.show()

class damper_screen(QMdiSubWindow):
    def __init__(self,mainwindow):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.mainwindow=mainwindow
        self.sUI()
        self.InitUI1()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        m=c.execute("Select * from damper where  key=1")
        
        for z in m:
            #print(z[0],'bool1')
            self.doff=z[0]
            self.d50=z[1]
            self.d100=z[2]
        conn.commit()
        c.close()
        conn.close()
    def InitUI1(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet("background-color:#f7f7ff;")
        self.label = QLabel('Damper Screen',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black;')
        self.label.setGeometry(450,110,220,50)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,160,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.back.clicked.connect(self.call_first1)
        
        self.d_off = QPushButton('Off 0%', self)
        self.d_off.setCheckable(True)
        self.d_off.setGeometry(105,240,240,120)
        self.d_off.setFont(QFont('Arial', 21))
        self.d_off.setChecked(bool(self.doff))
        self.d_off.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        
        self.d_off.clicked.connect(lambda doff:self.d_off_on(doff))
        
        self.d_50 = QPushButton('Half 50 %', self)
        self.d_50.setCheckable(True)
        self.d_50.setGeometry(105,390,240,120)
        self.d_50.setFont(QFont('Arial', 21))
        self.d_50.setChecked(bool(self.d50))
        #self.d_50.setStyleSheet("QPushButton{background-color:red;}")
        self.d_50.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        #self.d_50.setStyleSheet("QPushButton:pressed { background-color: ; }")
        #self.d_50.setStyleSheet("QPushButton:checked{background-color: white;}")
        self.d_50.clicked.connect(lambda d50:self.d_50_on(d50))
        
        self.d_100 = QPushButton('Full 100 %', self)
        self.d_100.setCheckable(True)
        self.d_100.setChecked(bool(self.d100))
        self.d_100.setGeometry(105,540,240,120)
        self.d_100.setFont(QFont('Arial', 21))
        self.d_100.setStyleSheet(("QPushButton{background-color:#4299ff; color: white;border: none;border-style: outset;border-width:1px;border-radius: 1px;border-color: black;} QPushButton:checked { background-color:red;color:black; }"))
        
        self.d_100.clicked.connect(lambda d100:self.d_100_on(d100))
    def d_50_on(self,d50):
        #self.d_50.setCheckable(False)
        if(d50==True):
            self.d50=1
        elif(d50==False):
            self.d50=0
        print("50")
        self.d_off.setEnabled(True)
        self.d_50.setEnabled(False)
        self.d_100.setEnabled(True)
        
        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update damper set damper50={self.d50},damperoff=0,damper100=0 where key=1")


        conn.commit()
        c.close()               
        conn.close()

        self.popup1=popup2(name='             Damper is turned to 50 %',name2='Close')
        self.popup1.show()

    def d_off_on(self,doff):
        if(doff==True):
            self.doff=1
        elif(doff==False):
            self.doff=0
        print("off")
        self.d_off.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_100.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_100.setCheckable(False)
        self.d_100.setEnabled(False)
        self.d_100.setEnabled(True)
        self.d_100.setCheckable(True)
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update damper set damperoff={self.doff},damper50=0,damper100=0 where key=1")


        conn.commit()
        c.close()               
        conn.close()
        self.popup1=popup2(name='               Damper is turned off',name2='Close')
        self.popup1.show()

    def d_100_on(self,d100):
        if(d100==True):
            self.d100=1
        elif(doff==False):
            self.d100=0
        print("100")
        #self.d_off.setEnabled(False)
        self.d_100.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_off.setEnabled(True)

        self.d_50.setCheckable(False)
        self.d_50.setEnabled(False)
        self.d_50.setEnabled(True)
        self.d_50.setCheckable(True)

        self.d_off.setCheckable(False)
        self.d_off.setEnabled(False)
        self.d_off.setEnabled(True)
        self.d_off.setCheckable(True)
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update damper set damper100={self.d100},damper50=0,damperoff=0 where Key=1")


        conn.commit()
        c.close()               
        conn.close()
        self.popup1=popup2(name='              Damper is turned to 100 %',name2='Close')
        self.popup1.show()
    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()

        
class about_screen(QMdiSubWindow):
    def __init__(self,mainwindow):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.mainwindow=mainwindow
        self.InitUI1()
    def InitUI1(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet("background-color:#f7f7ff;")
        self.label = QLabel('About Us',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(450,110,220,50)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,160,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.back.clicked.connect(self.call_first1)
        self.plainText = QPlainTextEdit(self)
        self.plainText.setStyleSheet('background-color:white; color: black')
        self.plainText.setTextCursor(QTextCursor())
        self.plainText.setFont(QFont('Arial',20))
        self.plainText.setReadOnly(True)
        self.plainText.setGeometry(10,250,1000,500)
        self.quote = """Anamed Systems was established back in 2006 with an aim in mind to provide the best medical and laboratory instruments to all over the world. Company 
has successfully achieved its target over the period of 13 years in the industry and now moving forward with a drastic pace to accomplish the vision of it’s 
founder.
Anamed Systems was installed with an purpose in thoughts to provide the 
excellent Medical and laboratory instruments to everywhere in the international.
Company has successfully performed its target over the length of thirteen 
years inside the industry and now transferring forward with a drastic tempo to 
perform the imaginative and prescient of it’s founder.
Anamed Systems is the specialized supplier of revolutionary heat technology
merchandise of drying, incubating and hot air sterilization carried out in 
studies, improvement, production and satisfactory guarantee.
As a member of Anamed Systems, KSA is specialized inside the income and 
carrier of these super merchandise. This technologically leading product line is based on a knowledge amassed over a few years and meets the needs and 
requirements of an ever changing marketplace.
Competent consulting, an international energetic network of buyers and a 
properly skilled group of provider technicians are the foundation of happy 
customers."""
        
        self.plainText.appendPlainText(self.quote)
        self.plainText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.plainText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.plainText.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        #self.plainText.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        #self.dataView.setMouseEnabled(x=False)
        QScroller.grabGesture(self.plainText.viewport(), QScroller.LeftMouseButtonGesture)
    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()

class graphresultwindowsecond(QMdiSubWindow):
    def __init__(self,mainwindow):
       super().__init__() 
       self.title = "App3"
       self.top = 0
       self.left = 00
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.startui()
       self.InitUI1()
    def getting_table_data(self):
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute(f"Select * from result where  key={starttestdata.key}")
            for x in y:
                print(x,x[0])
                self.set_temperature=x[2]
                self.set_timer=x[3]
                self.set_username=x[4]
                self.set_status=x[7]

            conn.commit()
            c.close()
            conn.close()
            self.df_faisal=pd.read_csv(starttestdata.key+'.csv')  
    def startui(self):
        self.getting_table_data()       
    def InitUI1(self):
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('resultscreen1.png'))
        self.label.setGeometry(0,100,1024,668)
        self.back = QPushButton('Back', self)
        self.back.setGeometry(80,610,180,80)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_first1)
        self.print = QPushButton('Print', self)
        self.print.setGeometry(280,610,180,80)
        self.print.setFont(QFont('Arial', 21))
        self.print.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.print.clicked.connect(self.call_first1)
        self.exportcsv = QPushButton('Export Csv', self)
        self.exportcsv.setGeometry(480,610,180,80)
        self.exportcsv.setFont(QFont('Arial', 21))
        self.exportcsv.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.exportcsv.clicked.connect(self.call_first1)
        self.exportgraph = QPushButton('Export Graph', self)
        self.exportgraph.setGeometry(680,610,180,80)
        self.exportgraph.setFont(QFont('Arial', 21))
        self.exportgraph.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.exportgraph.clicked.connect(self.call_first1)
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(550,170,420, 390)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=False,y=True)
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setWindowTitle('Temperature Graph')
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.df_faisal['Time'], self.df_faisal['Temperature'], pen=pen)
        self.temperature = QLabel("Temperature",self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(100,175,140,75)

        self.timer = QLabel("Timer",self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(100,290,140,75)

                
        self.username = QLabel("User Name",self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(100,395,140,75)
        
        self.status = QLabel("Status",self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(100,505,100,75)
        
        self.temperature = QLabel(self)
        self.temperature.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.temperature.setGeometry(340,175,170,75)
        self.temperature.setText(self.set_temperature)

        self.timer = QLabel(self)
        self.timer.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.timer.setGeometry(340,290,170,75)
        self.timer.setText(self.set_timer)

                
        self.username = QLabel(self)
        self.username.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.username.setGeometry(340,395,170,75)
        self.username.setText(self.set_username)
        
        self.status = QLabel(self)
        self.status.setFont(QFont('Arial', 19))
        #self.set_temp_data.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.status.setGeometry(340,505,170,75)
        self.status.setText(self.set_status)


        self.show()

    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mySubwindow = result_window(self.mainwindow)
        windoww.win.addSubWindow(self.mySubwindow)
        self.mySubwindow.show()
class result_screen():
    result=''
    searchkey=''
class result_window(QMdiSubWindow):
    
    def __init__(self,mainwindow):
       super().__init__()
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.InitUI()
    def call_b(self,data):
        if(data=="result"):
            user_data=self.search.text()
            self.close()
            #self.destroy()
            #gc.collect()
            result_screen.searchkey=self.comboBox.currentText()
            #print(self.comboBox.currentText())
            #self.comboBox.setCurrentText(starttestdata.level)
            #self.comboBox_2.setCurrentText(starttestdata.fanspeed)
            self.nk=keyboard(self.mainwindow,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.setAttribute(Qt.WA_DeleteOnClose)
        #scroll_area=QScrollArea(self)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Results Data',self)


        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(7)
        font.setPointSize (21)
        self.label.setFont(font)
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(450,100,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,160,230,70)
        effect = QGraphicsDropShadowEffect(self.back)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.back.setGraphicsEffect(effect)
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(50)
        font.setPointSize (15)
        self.back.setFont(font)
        #self.back.setStyleSheet(("QPushButton{background-color:#008CBA; color: white;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;} QPushButton:hover { background-color:red;color:white; }"))
        self.back.setStyleSheet(("QPushButton{background-color:#4299ff; color: black;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;}"))
        
        self.back.clicked.connect(self.call_back)

        self.exp_result = QPushButton('Export All Results', self)
        self.exp_result.setGeometry(30,160,230,70)
        effect = QGraphicsDropShadowEffect(self.exp_result)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.exp_result.setGraphicsEffect(effect)
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(50)
        font.setPointSize (15)
        self.exp_result.setFont(font)
        self.exp_result.setStyleSheet(("QPushButton{background-color:#4299ff; color: black;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;}"))
        
        self.exp_result.clicked.connect(self.ex_result)
        self.show_aresult = QPushButton('Show All Results', self)
        self.show_aresult.setGeometry(270,160,230,70)
        effect = QGraphicsDropShadowEffect(self.show_aresult)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.show_aresult.setGraphicsEffect(effect)
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(50)
        font.setPointSize (15)
        self.show_aresult.setFont(font)
        #self.back.setStyleSheet(("QPushButton{background-color:#008CBA; color: white;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;} QPushButton:hover { background-color:red;color:white; }"))
        self.show_aresult.setStyleSheet(("QPushButton{background-color:#4299ff; color: black;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;}"))
        
        self.show_aresult.clicked.connect(self.insert_data)
        
        self.view_result = QPushButton('View Result', self)
        self.view_result.setGeometry(510,160,230,70)
        effect = QGraphicsDropShadowEffect(self.view_result)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.view_result.setGraphicsEffect(effect)
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(50)
        font.setPointSize (15)
        self.view_result.setFont(font)
        #self.back.setStyleSheet(("QPushButton{background-color:#008CBA; color: white;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;} QPushButton:hover { background-color:red;color:white; }"))
        self.view_result.setStyleSheet(("QPushButton{background-color:#4299ff; color: black;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;}"))
        
        self.view_result.clicked.connect(self.view_result1)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(150, 270, 231, 60)
        self.comboBox.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Date")
        self.comboBox.addItem("Temperature")
        self.comboBox.addItem("Timer")
        self.comboBox.addItem("Username")
        self.comboBox.addItem("Fanspeed")
        self.comboBox.addItem("Level")
        self.comboBox.addItem("Status")
        self.comboBox.setCurrentText(result_screen.searchkey)
        self.search = extQLineEdit1(self)
        self.search.setGeometry(410, 270, 251, 60)
        self.search.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.search.setObjectName("lineEdit_3")
        self.search.setFont(QFont('Arial', 21))
        self.search.setPlaceholderText('Enter Key Word')
        self.search.setReadOnly(True)
        self.search.setText(result_screen.result)
        self.search.speak.connect(partial(self.call_b,data='result'))
        self.search_b = QPushButton('Search', self)
        self.search_b.setGeometry(680,270,200,60)
        effect = QGraphicsDropShadowEffect(self.search_b)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        self.search_b.setGraphicsEffect(effect)
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(50)
        font.setPointSize (15)
        self.search_b.setFont(font)
        #self.back.setStyleSheet(("QPushButton{background-color:#008CBA; color: white;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;} QPushButton:hover { background-color:red;color:white; }"))
        self.search_b.setStyleSheet(("QPushButton{background-color:#4299ff; color: black;border-style: ridge;border-width:0px;border-radius: 10px;border-color: #008CBA;}"))
        
        self.search_b.clicked.connect(self.view_search)


        self.dataView = QTreeWidget(self)
        # scroll_area.setWidget(self.dataView)
        # scroll_area.setGeometry(10,350,1000,415)
        # QScroller.grabGesture(scroll_area.viewport(), QScroller.LeftMouseButtonGesture)
        
        #self.dataView.model=QAbstractItemModel()
        self.dataView.setRootIsDecorated(False)

        self.dataView.setHeaderLabels(['No','Date/\nTime','Temperature','Timer','User\nName','Fan\nSpeed','Level','Status'])

        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:14pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')



        self.dataView.setColumnCount(8)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,0)
        self.dataView.setColumnWidth(1,140)
        self.dataView.setColumnWidth(2,120)
        self.dataView.setColumnWidth(3,130)
        self.dataView.setColumnWidth(4,180)
        self.dataView.setColumnWidth(5,100)
        self.dataView.setColumnWidth(6,120)
        self.dataView.setColumnWidth(7,130)
        self.dataView.setAlternatingRowColors(True)
        #self.dataView.setColumnWidth(8,100)
        self.dataView.setColumnWidth(8,0)


        self.dataView.setStyleSheet('background-color:white;color: black;')
        self.dataView.setFont(QFont('Times New Roman', 18))
        self.dataView.setGeometry(10,350,1000,415)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dataView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.dataView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        #self.dataView.setMouseEnabled(x=False)
        #self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.TouchGesture)
        
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()

        #self.show()
    #@QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        #global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        self.getChildNode = baseNode.text(8)
        #print(getChildNode)

    def call_back(self):
        self.close()
        self.mainwindow.show()
        #mm.mm.show()
        #self.destroy()
        #gc.collect()
        result_screen.searchkey=self.comboBox.currentText()
        #self.m=subwindow()
        #windoww.win.addSubWindow(self.m)
        #self.m.show()
    def ex_result(self):
        self.close()
        #self.destroy()
        #gc.collect()
        result_screen.searchkey=self.comboBox.currentText()
        self.xw=exportallresults(self.mainwindow)
        windoww.win.addSubWindow(self.xw)
        self.xw.show()
    def insert_data(self):
        #if(self.insertfirsttime==0):
            self.dataView.clear()
            self.insertfirsttime=1
            l=[]
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select * from result order by Key DESC")
            for row in y:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0]+str('\n')+x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]) 

            conn.commit()
            c.close()
            conn.close()
    def view_result1(self):
        #global getChildNode
        try:
            if len(str(self.getChildNode))==0:
                 raise ValueError 
            self.close()
            #self.destroy()
            #gc.collect() 
            #info.info1=getChildNode
            #self.e.show()
            starttestdata.key=str(self.getChildNode)
            result_screen.searchkey=self.comboBox.currentText()
            self.grw=graphresultwindowsecond(self.mainwindow)
            windoww.win.addSubWindow(self.grw)
            self.grw.show()
            getChildNode=''

        except:
            print("error")
            self.popup1=popup1(name='            Please select any value !',name2='Close')
            self.popup1.show()
    def view_search(self):
        self.popup1=popup2(name='         The results has been updated !',name2='Close')
        self.popup1.show()
        self.dataView.clear()
        mg=self.search.text()
        mg.strip()
        temp_search=self.comboBox.currentText()
        temp_search.strip()
        print(mg,temp_search)
        l=[]
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        y=c.execute(f"SELECT * from result WHERE {temp_search} LIKE '{mg}%' OR {temp_search} LIKE '0{mg}%' order by Key DESC ")
        for row in y:
            #print(row)
            l.append(row)
        for i,x in enumerate(l):
            #print(i,x)
            QTreeWidgetItem(self.dataView,[str(i),x[0]+str('\n')+x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]) 

        conn.commit()
        c.close()
        conn.close() 
class rg():
    rg=False
class running_window(QMdiSubWindow):
    def __init__(self,runninggraph):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.runninggraph=runninggraph
       self.sUI()
       self.InitUI()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        m=c.execute("Select * from sound where  key=1")
        for z in m:
            #print(z[0],'bool1')
            self.sounds=z[0]
        conn.commit()
        c.close()
        conn.close()
       #self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        time = QTime.currentTime().toString()
        x_t=self.temp_call()
        #my_gauge.value=x_t
       #self.label.setText(str(x_t))
        
       
        self.gauge.update_value(x_t)
        # if (c_to_f==0):
        #     my_gauge.value_min = 0
        #     my_gauge.value_max = 300
        # if (c_to_f==1):
        #     my_gauge.value_min = 32
        #     my_gauge.value_max = 572

       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,250,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.Form = QWidget()
        #self.ui = Ui_Form()
        #self.ui.setupUi(self.Form)
        #self.Form.show()
        # self.label = QLabel('uu',self)
        # self.label.setGeometry(165, 5, 61, 16)
        # self.label.setObjectName("label")
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(10)
        #self.gauge.show()
        #self.s1 = Switch(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('View Running Test', self)
        buttonWindow1.setFont(QFont('Arial', 22))
        buttonWindow1.setGeometry(20,160,285,155)
        buttonWindow1.setStyleSheet("background-color:red;border: none;border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #buttonWindow1.setStyleSheet('background-image: url(start.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,350,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,540,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,160,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,350,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,540,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        self.n = QPushButton(self)
        self.n.setFont(QFont('Arial', 27))
        self.n.setGeometry(800,630,50,50)
        self.n.setStyleSheet('background-image: url(notification1.png);border: none;border-style: outset;')
        self.n.clicked.connect(self.notification_1)  
        self.s = QPushButton(self)
        self.s.setCheckable(True)
        self.s.setFont(QFont('Arial', 27))
        self.s.setChecked(self.sounds)        
        self.s.setStyleSheet(("QPushButton{background-image: url(sound_on.png); color: white;border: none;} QPushButton:checked { background-image: url(sound_off.png);color:black; }"))
        self.s.clicked.connect(lambda sounds:self.control(sounds))
        self.s.setGeometry(715,630,80,50)

        
        #objgraph.show_refs(self, filename='sample-graph.png')
        self.show()
    def control(self,sounds):
        print(sounds)
        if(sounds==True):
            self.sounds=1
        elif(sounds==False):
            self.sounds=0
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update sound set volume='{self.sounds}'where Key=1")

        conn.commit()
        c.close()               
        conn.close()
        #pass

    def buttonWindow1_onClick(self):
        self.close()
        self.destroy()
        gc.collect()
        #self.rgwindow = startwindow(self)
        self.runninggraph.show()
    def settingswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_w=settingswindow(self)
        windoww.win.addSubWindow(self.s_w)
        self.s_w.show()
        #self.close()
        #self.swindow = settingswindow()
        #self.swindow.show()
    def userswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.uwindow = userswindow(self)
        windoww.win.addSubWindow(self.uwindow)
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.rw=result_window(self)
        windoww.win.addSubWindow(self.rw)
        self.rw.show()
        #self.close()
        #self.rswindow = resultswindow()
        #self.rswindow.show()
    def aboutwindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.a_s=about_screen(self)
        windoww.win.addSubWindow(self.a_s)
        self.a_s.show()
        #self.close()
        #self.abwindow = aboutwindow()
        #self.abwindow.show()
    def damperwindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.d_s=damper_screen(self)
        windoww.win.addSubWindow(self.d_s)
        self.d_s.show()
    def notification_1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.n1=notification1(self)
        windoww.win.addSubWindow(self.n1)
        self.n1.show()



class temperature_list():
    def temp_call(self):
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    start=False
    temperature_1=[]
    time_1=[]
    while start:
        now = time.time()
        #self.time.append(now)
        temperature_1.append(temp_call)
        time_1.append(now)



class DateAxisItem(AxisItem):
    """
    A tool that provides a date-time aware axis. It is implemented as an
    AxisItem that interpretes positions as unix timestamps (i.e. seconds
    since 1970).
    The labels and the tick positions are dynamically adjusted depending
    on the range.
    It provides a  :meth:`attachToPlotItem` method to add it to a given
    PlotItem
    """
    
    # Max width in pixels reserved for each label in axis
    _pxLabelWidth = 80

    def __init__(self, *args, **kwargs):
        AxisItem.__init__(self, *args, **kwargs)
        self._oldAxis = None

    def tickValues(self, minVal, maxVal, size):
        """
        Reimplemented from PlotItem to adjust to the range and to force
        the ticks at "round" positions in the context of time units instead of
        rounding in a decimal base
        """

        maxMajSteps = int(size/self._pxLabelWidth)

        dt1 = datetime.fromtimestamp(minVal)
        dt2 = datetime.fromtimestamp(maxVal)

        dx = maxVal - minVal
        majticks = []

        if dx > 63072001:  # 3600s*24*(365+366) = 2 years (count leap year)
            d = timedelta(days=366)
            for y in range(dt1.year + 1, dt2.year):
                dt = datetime(year=y, month=1, day=1)
                majticks.append(mktime(dt.timetuple()))

        elif dx > 5270400:  # 3600s*24*61 = 61 days
            d = timedelta(days=31)
            dt = dt1.replace(day=1, hour=0, minute=0,
                             second=0, microsecond=0) + d
            while dt < dt2:
                # make sure that we are on day 1 (even if always sum 31 days)
                dt = dt.replace(day=1)
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 172800:  # 3600s24*2 = 2 days
            d = timedelta(days=1)
            dt = dt1.replace(hour=0, minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 7200:  # 3600s*2 = 2hours
            d = timedelta(hours=1)
            dt = dt1.replace(minute=0, second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 1200:  # 60s*20 = 20 minutes
            d = timedelta(minutes=10)
            dt = dt1.replace(minute=(dt1.minute // 10) * 10,
                             second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 120:  # 60s*2 = 2 minutes
            d = timedelta(minutes=1)
            dt = dt1.replace(second=0, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 20:  # 20s
            d = timedelta(seconds=10)
            dt = dt1.replace(second=(dt1.second // 10) * 10, microsecond=0) + d
            while dt < dt2:
                majticks.append(mktime(dt.timetuple()))
                dt += d

        elif dx > 2:  # 2s
            d = timedelta(seconds=1)
            majticks = range(int(minVal), int(maxVal))

        else:  # <2s , use standard implementation from parent
            return AxisItem.tickValues(self, minVal, maxVal, size)

        L = len(majticks)
        if L > maxMajSteps:
            majticks = majticks[::int(numpy.ceil(float(L) / maxMajSteps))]

        return [(d.total_seconds(), majticks)]

    def tickStrings(self, values, scale, spacing):
        """Reimplemented from PlotItem to adjust to the range"""
        ret = []
        if not values:
            return []

        if spacing >= 31622400:  # 366 days
            fmt = "%Y"

        elif spacing >= 2678400:  # 31 days
            fmt = "%Y %b"

        elif spacing >= 86400:  # = 1 day
            fmt = "%b/%d"

        elif spacing >= 3600:  # 1 h
            fmt = "%b/%d-%Hh"

        elif spacing >= 60:  # 1 m
            fmt = "%H:%M"

        elif spacing >= 1:  # 1s
            fmt = "%H:%M:%S"

        else:
            # less than 2s (show microseconds)
            # fmt = '%S.%f"'
            fmt = '[+%fms]'  # explicitly relative to last second

        for x in values:
            try:
                t = datetime.fromtimestamp(x)
                ret.append(t.strftime(fmt))
            except ValueError:  # Windows can't handle dates before 1970
                ret.append('')

        return ret

    def attachToPlotItem(self, plotItem):
        """Add this axis to the given PlotItem
        :param plotItem: (PlotItem)
        """
        self.setParentItem(plotItem)
        viewBox = plotItem.getViewBox()
        self.linkToView(viewBox)
        self._oldAxis = plotItem.axes[self.orientation]['item']
        self._oldAxis.hide()
        plotItem.axes[self.orientation]['item'] = self
        pos = plotItem.axes[self.orientation]['pos']
        plotItem.layout.addItem(self, *pos)
        self.setZValue(-1000)

    def detachFromPlotItem(self):
        """Remove this axis from its attached PlotItem
        (not yet implemented)
        """
        raise NotImplementedError()  # TODO
class MyStringAxis(pg.AxisItem):
        def __init__(self, xdict, *args, **kwargs):
            pg.AxisItem.__init__(self, *args, **kwargs)
            self.x_values = np.asarray(xdict.keys())
            self.x_strings = xdict.values()

        def tickStrings(self, values, scale, spacing):
            strings = []
            for v in values:
                # vs is the original tick value
                vs = v * scale
                # if we have vs in our values, show the string
                # otherwise show nothing
                if vs in self.x_values:
                    # Find the string with x_values closest to vs
                    vstr = self.x_strings[np.abs(self.x_values-vs).argmin()]
                else:
                    vstr = ""
                strings.append(vstr)
            return strings
class selectuserscreen(QMdiSubWindow):
    def __init__(self,mainwindowshow):
    #def __init__(self,name):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.mainwindowshow=mainwindowshow
        #self.startUI()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Select User',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_back)
        
        self.selectuser = QPushButton('Select User', self)
        self.selectuser.setGeometry(30,200,240,70)
        self.selectuser.setFont(QFont('Arial', 21))
        self.selectuser.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.selectuser.clicked.connect(self.call_select)

        self.dataView = QTreeWidget(self)
        self.dataView.setRootIsDecorated(False)
        self.dataView.setHeaderLabels(['Ref No','User Name'])
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.setColumnCount(2)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,150)
        self.dataView.setColumnWidth(1,230)

        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        self.dataView.setGeometry(10,300,1010,465)
        self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.LeftMouseButtonGesture)
        self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        self.insert_data()
    #@pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        #global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        self.getChildNode = baseNode.text(1)
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
        
    def insert_data(self):
        #if(self.insertfirsttime==0):
            #self.insertfirsttime=1
            l=[]
            test = UsersTable("faisal.db")
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0]])
    def call_back(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.userswindow=startwindow(self.mainwindowshow)
        windoww.win.addSubWindow(self.userswindow)
        self.userswindow.show()
    def call_select(self):
        #global getChildNode
        try:
            starttestdata.username=self.getChildNode
            self.close()
            #self.destroy()
            #gc.collect()
            self.userswindow=startwindow(self.mainwindowshow)
            windoww.win.addSubWindow(self.userswindow)
            self.userswindow.show()
        except:
            self.popup1=popup1(name='    Please select any user to continue',name2='Okay!')
            self.popup1.show()





class timer_keyboard(QMdiSubWindow):
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
    #def __init__(self,name):
        super().__init__()
        #self.name=name
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='hours' ):
            self.labelshow="Enter Hours"
            self.length=2
        elif(self.previouswindow=='minutes' ):
            self.labelshow="Enter Minutes"
            self.length=2




    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,116,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        #self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,233,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,233,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,233,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,337,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,337,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,337,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,441,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,441,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,441,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,545,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,545,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kinf = QPushButton('infinity', self)
        kinf.setGeometry(670,545,297,100)
        kinf.setFont(QFont('Arial', 28))
        kinf.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kinf.clicked.connect(self.enter1)
        
        kl = QPushButton('<', self)
        kl.setGeometry(45,649,296,100)
        kl.setFont(QFont('Arial', 24))
        kl.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kl.clicked.connect(self.moveleft)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(358,649,296,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)
        
        kr = QPushButton('>', self)
        kr.setGeometry(670,649,297,100)
        kr.setFont(QFont('Arial', 24))
        kr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kr.clicked.connect(self.moveright)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.insert(str(sender.text()))
            #self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        self.entry.backspace()
        #self.entry.text=self.entry.text()[0:-2]
        # print(self.entry.text()[0:-1])
        # l=self.entry.text()[0:-1]
        # self.entry.setText(l)
        self.entry.setFocus()
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='hours' ):
            try:
                text=self.entry.text()
                sender = self.sender()
                #print(self.sender())
                if(str(sender.text())=='infinity'):
                    self.close()
                    # starttestdata.hours = self.entry.text()
                    # starttestdata.minutes = self.entry.text()
                    starttestdata.hours = 'infinity'
                    starttestdata.minutes = 'infinity'
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()

                elif(len(text)==0):
                    self.close()
                    starttestdata.hours = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()

                #elif(text.count('.')>=2):
                #    raise NameError
                #elif(float(self.entry.text())>300 or float(self.entry.text())<25):
                #    raise ValueError
                
                #print(y.username,'ee')
                elif(int(self.entry.text())>99):
                    raise ValueError

                else:
                    self.close()
                    starttestdata.hours = self.entry.text()
                    #self.destroy()
                    #gc.collect()
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='           Pleae enter hours less than 100.',name2='Close')
                self.popup1.show()
        elif(self.previouswindow=='minutes' ):
            try:
                text=self.entry.text()
                sender = self.sender()
                #print(self.sender())
                if(str(sender.text())=='infinity'):
                    self.close()
                    # starttestdata.hours = self.entry.text()
                    # starttestdata.minutes = self.entry.text()
                    starttestdata.hours = 'infinity'
                    starttestdata.minutes = 'infinity'
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()

                elif(len(text)==0):
                    self.close()
                    starttestdata.minutes = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()

                #elif(text.count('.')>=2):
                #    raise NameError
                elif(int(self.entry.text())>59):
                    raise ValueError
                
                #print(y.username,'ee')
                elif(text=='infinity'):
                    self.close()
                    starttestdata.hours = self.entry.text()
                    starttestdata.minutes = self.entry.text()
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()

                else:
                    self.close()
                    starttestdata.minutes = self.entry.text()
                    #self.destroy()
                    #gc.collect()
                    self.userswindow=startwindow(self.mainwindowshow)
                    windoww.win.addSubWindow(self.userswindow)
                    self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='           Pleae enter minutes less than 60.',name2='Close')
                self.popup1.show()



    def moveleft(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()-1
        self.entry.setCursorPosition(x)

    def moveright(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()+1
        self.entry.setCursorPosition(x)
class temperature_keyboard(QMdiSubWindow):
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
    #def __init__(self,name):
        super().__init__()
        #self.name=name
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='temperature' or self.previouswindow=='e_p1'or self.previouswindow=='e_p2' or self.previouswindow=='e_p3' ):
            self.labelshow="Enter Temerature"
            self.length=5



    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,116,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        #self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,233,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,233,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,233,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,337,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,337,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,337,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,441,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,441,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,441,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,545,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,545,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,545,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kl = QPushButton('<', self)
        kl.setGeometry(45,649,296,100)
        kl.setFont(QFont('Arial', 24))
        kl.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kl.clicked.connect(self.moveleft)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(358,649,296,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)
        
        kr = QPushButton('>', self)
        kr.setGeometry(670,649,297,100)
        kr.setFont(QFont('Arial', 24))
        kr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kr.clicked.connect(self.moveright)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.insert(str(sender.text()))
            #self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
    def clear1(self):
        self.entry.backspace()
        #self.entry.text=self.entry.text()[0:-2]
        # print(self.entry.text()[0:-1])
        # l=self.entry.text()[0:-1]
        # self.entry.setText(l)
        self.entry.setFocus()
    def space1(self):
        self.entry.setText(self.entry.text() + ' ')
    
    def enter1(self):
        if(self.previouswindow=='temperature'or self.previouswindow=='e_p1' or self.previouswindow=='e_p2'or self.previouswindow=='e_p3'):
            try:
                text=self.entry.text()
                if(len(text)==0):
                    self.close()
                    if(self.previouswindow=='temperature'):
                        starttestdata.temperature = self.entry.text()
                        self.userswindow=startwindow(self.mainwindowshow)
                        windoww.win.addSubWindow(self.userswindow)
                        self.userswindow.show()
                    elif(self.previouswindow=='e_p1' or self.previouswindow=='e_p2'or self.previouswindow=='e_p3' ):
                        #starttestdata.temperature = self.entry.text()
                        self.userswindow=point3calibration(self.mainwindowshow)
                        windoww.win.addSubWindow(self.userswindow)
                        self.userswindow.show()


                elif(text.count('.')>=2):
                    raise NameError
                elif(float(self.entry.text())>300 or float(self.entry.text())<25):
                    raise ValueError
                
                #print(y.username,'ee')
                else:
                    self.close()
                    if(self.previouswindow=='temperature'):
                        starttestdata.temperature = self.entry.text()
                        self.userswindow=startwindow(self.mainwindowshow)
                        windoww.win.addSubWindow(self.userswindow)
                        self.userswindow.show()
                    elif(self.previouswindow=='e_p1' or self.previouswindow=='e_p2'or self.previouswindow=='e_p3' ):
                        point_calibration.e_s1_p1 = self.entry.text()
                        self.userswindow=point3calibration(self.mainwindowshow)
                        windoww.win.addSubWindow(self.userswindow)
                        self.userswindow.show()
                    # starttestdata.temperature = self.entry.text()
                    # #self.destroy()
                    # #gc.collect()
                    # self.userswindow=startwindow(self.mainwindowshow)
                    # self.userswindow.show()
            except NameError:
                self.popup1=popup1(name='           Please enter valid temperature !',name2='Close')
                self.popup1.show()
            except ValueError:
                self.popup1=popup1(name='Pleae enter temperature less than 300\n and greater than 25.',name2='Close')
                self.popup1.show()





    def moveleft(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()-1
        self.entry.setCursorPosition(x)

    def moveright(self):
        self.entry.setFocus()
        #print(self.entry.cursorPosition())
        x=self.entry.cursorPosition()+1
        self.entry.setCursorPosition(x)

        #self.close()
        #self.destroy()
        #gc.collect()        
class graphresultwindow(QMdiSubWindow):
    def __init__(self,mainwindow):
       super().__init__() 
       #parent=None
       #super(secondwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App3"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.mainwindow=mainwindow
       self.startui()
       self.InitUI1()
    def getting_table_data(self):
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute(f"Select * from result where  key={starttestdata.key}")
            for x in y:
                print(x,x[0])
                self.set_temperature=x[2]
                self.set_timer=x[3]
                self.set_username=x[4]
                self.set_status=x[7]

            conn.commit()
            c.close()
            conn.close()
            self.df_faisal=pd.read_csv(starttestdata.key+'.csv')  
    def startui(self):
        self.getting_table_data()       
    def InitUI1(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)

        #self.setStyleSheet("background-image: url(header.png);")
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('resultscreen1.png'))
        self.label.setGeometry(0,100,1024,668)
        self.back = QPushButton('Home', self)
        self.back.setGeometry(80,610,180,80)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.back.clicked.connect(self.call_first1)
        self.print = QPushButton('Print', self)
        self.print.setGeometry(280,610,180,80)
        self.print.setFont(QFont('Arial', 21))
        self.print.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.print.clicked.connect(self.call_first1)
        self.exportcsv = QPushButton('Export Csv', self)
        self.exportcsv.setGeometry(480,610,180,80)
        self.exportcsv.setFont(QFont('Arial', 21))
        self.exportcsv.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.exportcsv.clicked.connect(self.call_first1)
        self.exportgraph = QPushButton('Export Graph', self)
        self.exportgraph.setGeometry(680,610,180,80)
        self.exportgraph.setFont(QFont('Arial', 21))
        self.exportgraph.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.exportgraph.clicked.connect(self.call_first1)
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(550,170,420, 390)
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=False,y=True)
        self.graphWidget.setLabel('left', 'Temperature')
        self.graphWidget.setLabel('bottom', 'Time')
        self.graphWidget.setWindowTitle('Temperature Graph')
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.df_faisal['Time'], self.df_faisal['Temperature'], pen=pen)
        self.temperature = QLabel("Temperature",self)
        self.temperature.setFont(QFont('Arial', 19))
        self.temperature.setStyleSheet('background-color:white; color: black;')
        self.temperature.setGeometry(100,175,140,75)

        self.timer = QLabel("Timer",self)
        self.timer.setFont(QFont('Arial', 19))
        self.timer.setStyleSheet('background-color:white; color: black;')
        self.timer.setGeometry(100,290,140,75)

                
        self.username = QLabel("User Name",self)
        self.username.setFont(QFont('Arial', 19))
        self.username.setStyleSheet('background-color:white; color: black;')
        self.username.setGeometry(100,395,140,75)
        
        self.status = QLabel("Status",self)
        self.status.setFont(QFont('Arial', 19))
        self.status.setStyleSheet('background-color:white; color: black;')
        self.status.setGeometry(100,505,100,75)
        
        self.temperature = QLabel(self)
        self.temperature.setFont(QFont('Arial', 19))
        self.temperature.setStyleSheet('background-color:white; color: black;')
        self.temperature.setGeometry(340,175,170,75)
        self.temperature.setText(self.set_temperature)

        self.timer = QLabel(self)
        self.timer.setFont(QFont('Arial', 19))
        self.timer.setStyleSheet('background-color:white; color: black;')
        self.timer.setGeometry(340,290,170,75)
        self.timer.setText(self.set_timer)

                
        self.username = QLabel(self)
        self.username.setFont(QFont('Arial', 19))
        self.username.setStyleSheet('background-color:white; color: black;')
        self.username.setGeometry(340,395,170,75)
        self.username.setText(self.set_username)
        
        self.status = QLabel(self)
        self.status.setFont(QFont('Arial', 19))
        self.status.setStyleSheet('background-color:white; color: black;')
        self.status.setGeometry(340,505,170,75)
        self.status.setText(self.set_status)


        self.show()

    def call_first1(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.mainwindow.show()
class runninggraphwindow(QMdiSubWindow):
    def __init__(self,name):
        super().__init__()
        self.title = "App3"
        self.top = 0
        self.left = 0
        self.width = 1024
        self.height = 768
        self.mainwindow=name
        self.i=0
        self.time1=[]
        self.only1=0
        self.only2=0
        self.dusra_variable=0
        self.startUI()
        self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55

    def update_plot_data(self):
        #time = QTime.currentTime().toString()
            # currentDT = datetime.now()
            # date_test=currentDT.strftime("%d-%m-%Y")
            # time_test=currentDT.strftime("%H:%M:%S")
            # key_1=currentDT.strftime("%Y%m%d%H%M%S")
            # #print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            # conn = sqlite3.connect('faisal.db')
            # c = conn.cursor()
            # #c.execute(f"DELETE from Userdata where ActionKey={keydata.editdata}") 
            # c.execute("INSERT INTO result(Date,Time,Temperature,Timer,Username,FanSpeed,Level,Status,Key) VALUES(?,?,?,?,?,?,?,?,?)",(date_test,time_test,starttestdata.temperature,timer_data,starttestdata.username,starttestdata.fanspeed,starttestdata.level,status,key_1))
            # conn.commit()
        now = time.time()
        #print(type(now))
        #timestamps = numpy.linspace(now - 3600, now, 100)
        self.time.append(now)
        #self.time1.append(self.i)
        #self.ticks = [list(zip(range(self.i), self.time))]
        #self.i=self.i+1

        #self.xax.setTicks(self.ticks)
        
        #self.x = self.x[1:]  # Remove the first y element.
        #time = QTime.currentTime().toString()
        #self.time.append('time')  # Add a new value 1 higher than the last.


        #self.y = self.y[1:]  # Remove the first

        x_t=self.temp_call() 
        #print(type(x_t))
        self.temperature.append(x_t)
        mainwindow1.toptext="Current Temperature:"+"  "+str(x_t)  # Add a new random value.
        #mainwindow1.lowertext="Timer :"+"  "+str(self.time_show)
        #self.xdict=dict(enumerate(self.time))

        self.data_line .setData(self.time, self.temperature)
        self.gauge.update_value(x_t)  # Update the data.
        if (float(x_t)<float(starttestdata.temperature)):
                self.dusra_variable=1
        if(self.only2==0):
            self.only2=1
            self.pid1=External2()
            self.calc = External1()
            self.pid1.start()
        if(float(x_t)>=float(starttestdata.temperature) and self.only1==0 and self.dusra_variable==1):
            self.only1=1
            self.calc.countChanged.connect(self.onCountChanged)
            self.calc.start()

    def startUI(self):
        if(starttestdata.hours=='infinity'):
            self.time_show='infinity'
            mainwindow1.lowertext="Timer :"+"  "+str("Infinity")
            self.inf=External3()
            self.inf.start()
        else:
            self.time_show=str(starttestdata.hours)+'Hrs'+str(starttestdata.minutes)+'Mins'
            mainwindow1.lowertext="Timer :"+"  "+str(self.time_show)
    def onCountChanged(self, value):
        #self.progress.setValue(value)
        if(value=="stop"):
            self.call_stopfinal()
    def InitUI(self):

        self.setWindowTitle(self.title)
        testclass.test="running"

        #self.setStyleSheet("background-image: url(header.png);")


        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setCursor(Qt.BlankCursor)
        self.label = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.label.setPixmap(QPixmap('graph_screen.png'))
        self.label.setGeometry(0,100,1024,668)
        
        self.set_temp = QLabel("Set Temperature :",self)
        self.set_temp.setFont(QFont('Arial', 17))
        self.set_temp.setStyleSheet('background-color:white; color: black;')
        self.set_temp.setGeometry(120,500,200,85)
        
        self.set_temp_data = QLabel(self)
        self.set_temp_data.setFont(QFont('Arial', 17))
        self.set_temp_data.setStyleSheet('background-color:white; color: black;')
        self.set_temp_data.setGeometry(300,500,100,85)
        self.set_temp_data.setText(starttestdata.temperature)

        self.set_timer = QLabel("Set Timer :",self)
        self.set_timer.setFont(QFont('Arial', 17))
        self.set_timer.setStyleSheet('background-color:white; color: black;')
        self.set_timer.setGeometry(650,500,130,85)
        
        self.set_timer_data = QLabel(self)
        self.set_timer_data.setFont(QFont('Arial', 17))
        self.set_timer_data.setStyleSheet('background-color:white; color: black;')
        self.set_timer_data.setGeometry(780,500,200,85)
        self.set_timer_data.setText(self.time_show)
        #self.time_show

        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,130,270, 440)
        self.gauge.setStyleSheet("background-color:white;")
        #self.gauge.show()
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setGeometry(70,140,550, 350)
        self.graphWidget.setBackground('w')
        self.graphWidget.plotItem.setMouseEnabled(y=False) # Only allow zoom in X-axis
        self.graphWidget.setMouseEnabled(x=False)
        #pg.setConfigOption('leftButtonPan', False)
        #pg.setConfigOption('WheelspinPan', False)
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
        #self.graphWidget.addPlot(axisItems={'bottom': stringaxis})
           # x = ['a', 'b', 'c', 'd', 'e', 'f']
    #y = [1, 2, 3, 4, 5, 6]
    #xdict = dict(enumerate(x))

    #win = pg.GraphicsWindow()
    #stringaxis = MyStringAxis(xdict, orientation='bottom')
    #plot = win.addPlot(axisItems={'bottom': stringaxis})
    #curve = plot.plot(list(xdict.keys()),y)
        
        self.time = store.time_list  # 100 time points
        #self.xdict=dict(enumerate(self.time))
        #self.stringaxis = MyStringAxis(self.xdict, orientation='bottom')
        #self.graphWidget.addPlot(axisItems={'bottom': self.stringaxis})
        self.axis = DateAxisItem(orientation='bottom')
        self.axis.attachToPlotItem(self.graphWidget.getPlotItem())

        #self.xax = self.graphWidget.getAxis('bottom')
        #self.xax.setStyle(autoExpandTextSpace=True,tickTextHeight=25)
        self.temperature = store.temp_list
        #self.xax.setTicks(ticks)
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.time, self.temperature, pen=pen)
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        #self.graphWidget.show()
        
        #self.setCentralWidget(self.graphWidget)

        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        #self.graphWidget.plot(hour, temperature)
        self.Home = QPushButton('Home', self)
        self.Home.setGeometry(120,600,250,90)
        self.Home.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.Home.clicked.connect(self.call_home)
        self.stoptest = QPushButton('Stop Test', self)
        self.stoptest.setGeometry(650,600,250,90)
        self.stoptest.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        #self.buttonWindow12.move(100, 100)
        self.stoptest.clicked.connect(self.popup_stoptest)

        self.show()
    def insert_data(self):
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor() 

            if(starttestdata.hours=='infinity'):
                c.execute("UPDATE powerfailure set startmode=0 where key=1")
                conn.commit()
                timer_data='infinity'
                key_1=starttestdata.key
                Value={'Time':self.time , 'Temperature':self.temperature}
                df1=DataFrame(Value,columns=['Time','Temperature'])
                ex_csv=key_1+'.csv'
                export_csv=df1.to_csv(ex_csv,index=None,header=True)
                self.inf.terminate()
                #starttestdata.key=key_1
            else:
                timer_data=str(starttestdata.hours)+"hrs"+str(starttestdata.minutes)+"mins"
                status=setstatus.status
                currentDT = datetime.now()
                date_test=currentDT.strftime("%d-%m-%Y")
                time_test=currentDT.strftime("%H:%M:%S")
                key_1=currentDT.strftime("%Y%m%d%H%M%S")
                #print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)

                c.execute("INSERT INTO result(Date,Time,Temperature,Timer,Username,FanSpeed,Level,Status,Key) VALUES(?,?,?,?,?,?,?,?,?)",(date_test,time_test,starttestdata.temperature,timer_data,starttestdata.username,starttestdata.fanspeed,starttestdata.level,status,key_1))
                conn.commit()

                Value={'Time':self.time , 'Temperature':self.temperature}
                df1=DataFrame(Value,columns=['Time','Temperature'])
                ex_csv=key_1+'.csv'
                export_csv=df1.to_csv(ex_csv,index=None,header=True)
                starttestdata.key=key_1
                setstatus.status='halted'
            c.close()
            conn.close()
            #self.close()
            #self.destroy()
            #gc.collect()
    def call_home(self):
        self.close()
        self.mm=running_window(self)
        windoww.win.addSubWindow(self.mm)
        self.mm.show()
    def call_stopfinal(self):
                self.insert_data()
                del self.time
                del self.temperature
                del store.time_list[:]
                del store.temp_list[:]
                #a.close()
                #a.destroy()
                self.timer.stop()
                self.close()
                self.destroy()
                gc.collect()
                testclass.test="notrunning"
                self.calc.terminate()
                self.pid1.terminate()
                
                #IO.setmode (IO.BOARD)
                #IO.setup(12,IO.OUT)
                #IO.output(12,0)
                self.grw=graphresultwindow(self.mainwindow)
                windoww.win.addSubWindow(self.grw)
                self.grw.show()
    def popup_stoptest(self):
            def call_no():
                a.close()
                a.destroy()
                gc.collect()

                #pass
            #print("popup")
            a=QFrame()
            a.setGeometry(237,209,550,350)
            a.setWindowModality(Qt.ApplicationModal)
            a.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
            a.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(a)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Error',a)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel('Are you sure you want to stop this test !',a)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            yes_delete = QPushButton('Yes !', a)
            yes_delete .setGeometry(50,240,240,90)
            yes_delete .setFont(QFont('Arial', 21))
            yes_delete .setStyleSheet('background-color:#d00403; color: white')
            yes_delete .clicked.connect(self.call_stopfinal)
            yes_delete .clicked.connect(call_no)
            no = QPushButton('No', a)
            no.setGeometry(270,240,240,90)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(call_no)
            a.show()
    def call_stoptest(self):
        self.popup_stoptest()

class setstatus():
  status='halted'
class startwindow(QMdiSubWindow):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.setupUi()
    def call_b(self,data):
        print("asdss",data)
        if(data=="temperature"):
            user_data=self.lineEdit.text()
            self.close()
            #self.destroy()
            #gc.collect()
            starttestdata.level=self.comboBox.currentText()
            starttestdata.fanspeed=self.comboBox_2.currentText()
            self.nk=temperature_keyboard(self.name,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="hours"):
            user_data=self.lineEdit_2.text()
            if(user_data=='infinity'):
                user_data=''
                starttestdata.hours=''
                starttestdata.minutes=''
            self.close()
            #self.destroy()
            #gc.collect()
            starttestdata.level=self.comboBox.currentText()
            starttestdata.fanspeed=self.comboBox_2.currentText()
            self.nk=timer_keyboard(self.name,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="minutes"):
            user_data=self.lineEdit_3.text()
            if(user_data=='infinity'):
                user_data=''
                starttestdata.hours=''
                starttestdata.minutes=''
            self.close()
            #self.destroy()
            #gc.collect()
            starttestdata.level=self.comboBox.currentText()
            starttestdata.fanspeed=self.comboBox_2.currentText()
            self.nk=timer_keyboard(self.name,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=='username'):
            self.close()
            #self.destroy()
            #gc.collect()
            starttestdata.level=self.comboBox.currentText()
            starttestdata.fanspeed=self.comboBox_2.currentText()
            self.sc=selectuserscreen(self.name)
            windoww.win.addSubWindow(self.sc)
            self.sc.show()

    def setupUi(self):
        #self.setObjectName("self")
        self.setWindowModality(Qt.NonModal)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setEnabled(True)
        #self.resize(1024, 668)
        self.setGeometry(0,0,1024,768)
        font = QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setMouseTracking(True)
        self.setAcceptDrops(False)
        self.setToolTip("")
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(247, 247, 255)")

        self.TestScreen = QLabel(self)
        self.TestScreen.setGeometry(QRect(410, 120, 151, 31))
        font = QFont()
        font.setPointSize(20)
        self.TestScreen.setFont(font)
        self.TestScreen.setAutoFillBackground(False)
        self.TestScreen.setStyleSheet("")
        self.TestScreen.setObjectName("TestScreen")
        self.graphicsView = QGraphicsView(self)
        self.graphicsView.setGeometry(QRect(20, 250, 981, 81))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = extQLineEdit1(self)
        self.lineEdit.setGeometry(QRect(710, 270, 211, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QFont('Arial', 21))
        self.lineEdit.setPlaceholderText('Temperature')
        self.lineEdit.speak.connect(partial(self.call_b,data='temperature'))
        self.graphicsView_2 = QGraphicsView(self)
        self.graphicsView_2.setGeometry(QRect(20, 330, 981, 81))
        self.graphicsView_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.lineEdit_2 = extQLineEdit1(self)
        self.lineEdit_2.setGeometry(QRect(710, 350, 101, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QFont('Arial', 21))
        self.lineEdit_2.setPlaceholderText('Hrs')
        self.lineEdit_2.speak.connect(partial(self.call_b,data='hours'))
        self.graphicsView_3 = QGraphicsView(self)
        self.graphicsView_3.setGeometry(QRect(20, 490, 981, 81))
        self.graphicsView_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.lineEdit_3 = extQLineEdit1(self)
        self.lineEdit_3.setGeometry(QRect(820, 350, 101, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(QFont('Arial', 21))
        self.lineEdit_3.setPlaceholderText('Min')
        self.lineEdit_3.speak.connect(partial(self.call_b,data='minutes'))
        self.lineEdit_6 = extQLineEdit1(self)
        self.lineEdit_6.setGeometry(QRect(710, 590, 231, 41))
        self.lineEdit_6.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setFont(QFont('Arial', 21))
        self.lineEdit_6.setPlaceholderText('Username')
        self.lineEdit_6.speak.connect(partial(self.call_b,data='username'))
        self.graphicsView_6 = QGraphicsView(self)
        self.graphicsView_6.setGeometry(QRect(20, 410, 981, 81))
        self.graphicsView_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_7 = QGraphicsView(self)
        self.graphicsView_7.setGeometry(QRect(20, 570, 981, 81))
        self.graphicsView_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.TestScreen_2 = QLabel(self)
        self.TestScreen_2.setGeometry(QRect(50, 280, 211, 31))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_2.setFont(font)
        self.TestScreen_2.setCursor(QCursor(Qt.UpArrowCursor))
        self.TestScreen_2.setAutoFillBackground(False)
        self.TestScreen_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_2.setObjectName("TestScreen_2")
        self.TestScreen_3 = QLabel(self)
        self.TestScreen_3.setGeometry(QRect(50, 360, 141, 31))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_3.setFont(font)
        self.TestScreen_3.setAutoFillBackground(False)
        self.TestScreen_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_3.setObjectName("TestScreen_3")
        self.TestScreen_4 = QLabel(self)
        self.TestScreen_4.setGeometry(QRect(50, 440, 141, 31))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_4.setFont(font)
        self.TestScreen_4.setAutoFillBackground(False)
        self.TestScreen_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_4.setObjectName("TestScreen_4")
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(710, 430, 231, 41))
        self.comboBox.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.TestScreen_5 = QLabel(self)
        self.TestScreen_5.setGeometry(QRect(50, 520, 171, 31))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_5.setFont(font)
        self.TestScreen_5.setAutoFillBackground(False)
        self.TestScreen_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_5.setObjectName("TestScreen_5")
        self.TestScreen_6 = QLabel(self)
        self.TestScreen_6.setGeometry(QRect(50, 600, 151, 31))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TestScreen_6.setFont(font)
        self.TestScreen_6.setAutoFillBackground(False)
        self.TestScreen_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";")
        self.TestScreen_6.setObjectName("TestScreen_6")
        self.comboBox_2 = QComboBox(self)
        self.comboBox_2.setGeometry(QRect(710, 510, 231, 41))
        self.comboBox_2.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox_2.setAcceptDrops(False)
        self.comboBox_2.setStyleSheet("font: 87 15pt \"Arial\";background-color: rgb(241, 241, 241);")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(660, 152, 291, 71))
        self.pushButton.clicked.connect(self.call_starttest)
        self.pushButton.setStyleSheet("border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 2px;\n"
"background-color: rgb(188, 255, 194);\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QRect(720, 670, 241, 61))
        
        #self.pushButton_2.clicked.connect(qApp.quit)
        #self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_2.clicked.connect(self.call_first1)
        self.pushButton_2.setStyleSheet("background-color:#4299ff;border: none;border-style: outset;\n"
"font: 14pt \"Arial\";\n"
"border-width: 1px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px; color: black")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_7.raise_()
        self.graphicsView_6.raise_()
        self.TestScreen.raise_()
        self.graphicsView.raise_()
        self.lineEdit.raise_()
        self.graphicsView_2.raise_()
        self.lineEdit_2.raise_()
        self.graphicsView_3.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_6.raise_()
        self.TestScreen_2.raise_()
        self.TestScreen_3.raise_()
        self.TestScreen_4.raise_()
        self.comboBox.raise_()
        self.TestScreen_5.raise_()
        self.TestScreen_6.raise_()
        self.comboBox_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        uni=u'\u231A'
        #uni=U+1F550
        self.label = QLabel(uni,self)
        self.label.setFont(QFont('Arial', 38))
        self.label.setStyleSheet('background-color:white;color: black;')
        self.label.setGeometry(924,340,57,45)
        self.retranslateUi()
        self.inserteditdata()
        #QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
       # _translate = QCoreApplication.translate
        self.setWindowTitle( "Start Test")
        self.TestScreen.setText("Test Screen")
        self.TestScreen_2.setText("SET TEMPERATURE")
        self.TestScreen_3.setText( "SET TIMER")
        self.TestScreen_4.setText( "SET LEVEL")
        self.comboBox.setItemText(0,  "FAST")
        self.comboBox.setItemText(1, "MEDIUM")
        self.comboBox.setItemText(2, "SLOW")
        self.TestScreen_5.setText("SET FAN SPEED")
        self.TestScreen_6.setText("SELECT USER")
        self.comboBox_2.setItemText(0, "100%")
        self.comboBox_2.setItemText(1,"50%")
        self.comboBox_2.setItemText(2,"25%")
        self.comboBox_2.setItemText(3, "off")
        self.pushButton.setText("START TEST")
        self.pushButton_2.setText("BACK")
    
    def inserteditdata(self):
            self.lineEdit.setText(starttestdata.temperature)
            self.lineEdit_2.setText(starttestdata.hours)
            self.lineEdit_3.setText(starttestdata.minutes)
            self.lineEdit_6.setText(starttestdata.username)
            self.comboBox.setCurrentText(starttestdata.level)
            self.comboBox_2.setCurrentText(starttestdata.fanspeed)

    def call_first1(self):
        #self.destroy()
        #gc.collect()
        self.close()
        starttestdata.level=self.comboBox.currentText()
        starttestdata.fanspeed=self.comboBox_2.currentText()

        self.name.show()
    def call_starttest(self):
        
        temp=self.lineEdit.text()
        timer1=self.lineEdit_2.text()
        timer2=self.lineEdit_3.text()
        level=self.comboBox.currentText()
        fansp=self.comboBox_2.currentText()
        un=self.lineEdit_6.text()
        try:
            if(len(temp)==0 or len(timer1)==0 or len(timer2)==0 or len(level)==0 or len(fansp)==0 or len(un)==0):
                raise ValueError
            elif(timer1.lower().strip()=="infinity"):
                starttestdata.temperature=self.lineEdit.text()
                starttestdata.hours=self.lineEdit_2.text()
                starttestdata.minutes=self.lineEdit_3.text()
                starttestdata.level=self.comboBox.currentText()
                starttestdata.fanspeed=self.comboBox_2.currentText()
                starttestdata.username=self.lineEdit_6.text() 
                
                timer_data='infinity'
                status='halted'
                currentDT = datetime.now()
                date_test=currentDT.strftime("%d-%m-%Y")
                time_test=currentDT.strftime("%H:%M:%S")
                key_1=currentDT.strftime("%Y%m%d%H%M%S")
                conn = sqlite3.connect("faisal.db")
                c = conn.cursor()
                c.execute("Delete from live")
                c.execute("UPDATE powerfailure set startmode=1 where key=1")
                c.execute("INSERT INTO result(Date,Time,Temperature,Timer,Username,FanSpeed,Level,Status,Key) VALUES(?,?,?,?,?,?,?,?,?)",(date_test,time_test,starttestdata.temperature,timer_data,starttestdata.username,starttestdata.fanspeed,starttestdata.level,status,key_1))
                conn.commit()
                c.close()
                conn.close()
                starttestdata.key=key_1
                self.close()
                self.rg=runninggraphwindow(self.name)
                windoww.win.addSubWindow(self.rg)
                self.rg.show()

            else:
                self.close()
                starttestdata.temperature=self.lineEdit.text()
                starttestdata.hours=self.lineEdit_2.text()
                starttestdata.minutes=self.lineEdit_3.text()
                starttestdata.level=self.comboBox.currentText()
                starttestdata.fanspeed=self.comboBox_2.currentText()
                starttestdata.username=self.lineEdit_6.text()    
                self.rg=runninggraphwindow(self.name)
                windoww.win.addSubWindow(self.rg)
                self.rg.show()
        except ValueError:
            self.popup1=popup1(name='           Please enter all values !',name2='Close')
            self.popup1.show()


    

class contactkeyboard(QMdiSubWindow): 
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):

        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14
        elif(self.previouswindow=='tele_no'):
            self.labelshow="Enter Contact"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 17))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,116,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,233,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,233,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,233,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,337,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,337,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,337,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,441,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,441,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,441,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,545,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,545,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,545,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kplus = QPushButton('+', self)
        kplus.setGeometry(45,649,296,100)
        kplus.setFont(QFont('Arial', 24))
        kplus.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kplus.clicked.connect(self.insert_text)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,649,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,649,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
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
        elif(self.previouswindow=='tele_no'):
            ins_screen.telephoneno=self.entry.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.edituser1=instrumentwindow(self.mainwindowshow)
            windoww.win.addSubWindow(self.edituser1)
            self.edituser1.show()

class numerickeyboard(QMdiSubWindow): 
    def __init__(self,mainwindowshow,previouswindow,entry_numeric):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_n=entry_numeric
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14
        elif(self.previouswindow=='c_name'):
            self.labelshow="Enter Company\nName"
            self.length=14
        elif(self.previouswindow=='pass'):
            self.labelshow="Enter Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="currentservicepassword1"):
            self.labelshow="Current Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword1"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword1"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="result"):
            self.labelshow="Enter Keywords"
            self.length=14

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        #self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)
        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 2px;')
        self.label.setGeometry(20,116,200,85)
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setMaxLength(self.length)
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setFocusPolicy(Qt.NoFocus)
        #lineedit = QApplication.focusWidget()
        #self.connect(self.entry.SIGNAL())
        #self.entry.gotFocus()
        #self.entry.setReadOnly(True)
        self.entry.setText(self.entry_n)
        k1 = QPushButton('1', self)
        k1.setGeometry(45,233,296,100)
        k1.setFont(QFont('Arial', 24))
        k1.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k1.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k2 = QPushButton('2', self)
        k2.setGeometry(358,233,296,100)
        k2.setFont(QFont('Arial', 24))
        k2.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k2.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k3 = QPushButton('3', self)
        k3.setGeometry(670,233,297,100)
        k3.setFont(QFont('Arial', 24))
        k3.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k3.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k4 = QPushButton('4', self)
        k4.setGeometry(45,337,296,100)
        k4.setFont(QFont('Arial', 24))
        k4.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k4.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k5 = QPushButton('5', self)
        k5.setGeometry(358,337,296,100)
        k5.setFont(QFont('Arial', 24))
        k5.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k5.clicked.connect(self.insert_text)
        #k1.clicked.connect(partial(self.insert_text,data='q'))
        k6 = QPushButton('6', self)
        k6.setGeometry(670,337,297,100)
        k6.setFont(QFont('Arial', 24))
        k6.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k6.clicked.connect(self.insert_text)
        
        k7 = QPushButton('7', self)
        k7.setGeometry(45,441,296,100)
        k7.setFont(QFont('Arial', 24))
        k7.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k7.clicked.connect(self.insert_text)
        
        k8 = QPushButton('8', self)
        k8.setGeometry(358,441,296,100)
        k8.setFont(QFont('Arial', 24))
        k8.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k8.clicked.connect(self.insert_text)
        
        k9 = QPushButton('9', self)
        k9.setGeometry(670,441,297,100)
        k9.setFont(QFont('Arial', 24))
        k9.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k9.clicked.connect(self.insert_text)
        
        clr=u'\u232b'
        #clr=str(clr)
        kclr = QPushButton(clr, self)
        kclr.setGeometry(45,545,296,100)
        kclr.setFont(QFont('Arial', 24))
        kclr.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kclr.clicked.connect(self.clear1)
       
        k0 = QPushButton('0', self)
        k0.setGeometry(358,545,296,100)
        k0.setFont(QFont('Arial', 24))
        k0.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        k0.clicked.connect(self.insert_text)
        
        kpo = QPushButton('.', self)
        kpo.setGeometry(670,545,297,100)
        kpo.setFont(QFont('Arial', 28))
        kpo.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kpo.clicked.connect(self.insert_text)
        
        kabc = QPushButton('abc', self)
        kabc.setGeometry(45,649,296,100)
        kabc.setFont(QFont('Arial', 24))
        kabc.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kabc.clicked.connect(self.change_abc)
        
        kspace = QPushButton('space', self)
        kspace.setGeometry(358,649,296,100)
        kspace.setFont(QFont('Arial', 24))
        kspace.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kspace.clicked.connect(self.space1)
        
        kenter = QPushButton('enter', self)
        kenter.setGeometry(670,649,297,100)
        kenter.setFont(QFont('Arial', 24))
        kenter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 15px;
border-color: black;
padding: 4px; color: black''')
        kenter.clicked.connect(self.enter1)

    def insert_text(self,data):
            sender = self.sender()
            self.entry.setText(self.entry.text() + str(sender.text()))
            self.entry.setFocus()
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

    def change_abc(self):
        self.close()
        #self.destroy()
        #gc.collect()        

        self.capital_keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        windoww.win.addSubWindow(self.capital_keyboard1)
        self.capital_keyboard1.show()
    
class keyboard(QMdiSubWindow):
    def __init__(self,mainwindowshow,previouswindow,entry_1):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entry_1=entry_1
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):

        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14
        elif(self.previouswindow=='c_name'):
            self.labelshow="Enter Company Name"
            self.length=14
        elif(self.previouswindow=='pass'):
            self.labelshow="Enter Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="currentservicepassword1"):
            self.labelshow="Current Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword1"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword1"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="result"):
            self.labelshow="Enter Keywords"
            self.length=14
            



    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;border-width: 1px;')
        self.label.setGeometry(20,116,200,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black;border-style:solid;border-width: 2px;')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setMaxLength(self.length)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setText(self.entry_1)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('q', self)
        q.setGeometry(59,249,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('w', self)
        self.w.setGeometry(149,249,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('e', self)
        self.e.setGeometry(240,249,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('r', self)
        self.r.setGeometry(331,249,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('t', self)
        self.t.setGeometry(422,249,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('y', self)
        self.y.setGeometry(513,249,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('u', self)
        self.u.setGeometry(604,249,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('i', self)
        self.i.setGeometry(695,249,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('o', self)
        self.o.setGeometry(786,249,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('p', self)
        self.p.setGeometry(877,249,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('a', self)
        self.a.setGeometry(59,380,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('s', self)
        self.s.setGeometry(149,380,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('d', self)
        self.d.setGeometry(240,380,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('f', self)
        self.f.setGeometry(331,380,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('g', self)
        self.g.setGeometry(422,380,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('h', self)
        self.h.setGeometry(513,380,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('j', self)
        self.j.setGeometry(604,380,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('k', self)
        self.k.setGeometry(695,380,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('l', self)
        self.l.setGeometry(786,380,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,380,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,514,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('z', self)
        self.z.setGeometry(149,513,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('x', self)
        self.x.setGeometry(240,513,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('c', self)
        self.c.setGeometry(331,513,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('v', self)
        self.v.setGeometry(422,513,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('b', self)
        self.b.setGeometry(513,513,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('n', self)
        self.n.setGeometry(604,513,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('m', self)
        self.m.setGeometry(695,513,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,513,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,513,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,638,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,638,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,638,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,638,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
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
            #self.labelshow="Enter Company\nName"
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
        
        
            
class capital_keyboard(QMdiSubWindow):
    def __init__(self,mainwindowshow,previouswindow,entry_small):
        super().__init__()
        self.title = "App"
        self.top = 0
        self.left = 100
        self.width = 1024
        self.height = 768
        self.temp_user=''
        self.entrys=entry_small
        self.mainwindowshow=mainwindowshow
        self.previouswindow=previouswindow
        self.startUI()
        self.InitUI()
    def startUI(self):
        if(self.previouswindow=='e_user' or self.previouswindow=='a_user' ):
            self.labelshow="Enter User Name"
            self.length=14
        elif(self.previouswindow=='e_employer' or self.previouswindow=='a_employer' ):
            self.labelshow="Enter Employer ID"
            self.length=14
        elif(self.previouswindow=='e_designation' or self.previouswindow=='a_designation' ):
            self.labelshow="Enter Designation"
            self.length=14
        elif(self.previouswindow=='e_contact' or self.previouswindow=='a_contact' ):
            self.labelshow="Enter Contact"
            self.length=14
        elif(self.previouswindow=='c_name'):
            self.labelshow="Enter Company\nName"
            self.length=14
        elif(self.previouswindow=='pass'):
            self.labelshow="Enter Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="currentservicepassword1"):
            self.labelshow="Current Password"
            self.length=14
        elif(self.previouswindow=="newservicepassword1"):
            self.labelshow="New Password"
            self.length=14
        elif(self.previouswindow=="confirmservicepassword1"):
            self.labelshow="Confirm Password"
            self.length=14
        elif(self.previouswindow=="result"):
            self.labelshow="Enter Keywords"
            self.length=14


    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('123.png'))
        self.bg.setGeometry(0,100,1024,668)

        self.label = QLabel(self.labelshow,self)
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('background-color:white; color: black; border-style:solid;')
        self.label.setGeometry(20,116,220,85)

        self.entry = QLineEdit(self)
        self.entry.setFont(QFont('Arial', 21))
        self.entry.setGeometry(220,116,750,85)
        self.entry.setStyleSheet('background-color:white; color: black')
        self.entry.setPlaceholderText(self.labelshow)
        self.entry.setAlignment(Qt.AlignLeft)
        self.entry.setReadOnly(True)
        self.entry.setMaxLength(self.length)
        self.entry.setText(self.entrys)
        #self.entry.setEnabled(False);
        #self.entry.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        #self.entry.setFocus()
        q = QPushButton('Q', self)
        q.setGeometry(59,249,82,100)
        q.setFont(QFont('Arial', 24))
        q.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        q.clicked.connect(partial(self.insert_text,data='q'))
        #q.clicked.connect(lambda: self.insert_text(data='q'))
        self.w = QPushButton('W', self)
        self.w.setGeometry(149,249,82,100)
        self.w.setFont(QFont('Arial', 24))
        self.w.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.w.clicked.connect(self.insert_text)
        self.e = QPushButton('E', self)
        self.e.setGeometry(240,249,82,100)
        self.e.setFont(QFont('Arial', 24))
        self.e.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.e.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.r = QPushButton('R', self)
        self.r.setGeometry(331,249,82,100)
        self.r.setFont(QFont('Arial', 24))
        self.r.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.r.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.t = QPushButton('T', self)
        self.t.setGeometry(422,249,82,100)
        self.t.setFont(QFont('Arial', 24))
        self.t.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.t.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.y = QPushButton('Y', self)
        self.y.setGeometry(513,249,82,100)
        self.y.setFont(QFont('Arial', 24))
        self.y.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.y.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.u = QPushButton('U', self)
        self.u.setGeometry(604,249,82,100)
        self.u.setFont(QFont('Arial', 24))
        self.u.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.u.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.i = QPushButton('I', self)
        self.i.setGeometry(695,249,82,100)
        self.i.setFont(QFont('Arial', 24))
        self.i.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.i.clicked.connect(self.insert_text)
        self.o = QPushButton('O', self)
        self.o.setGeometry(786,249,82,100)
        self.o.setFont(QFont('Arial', 24))
        self.o.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.o.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.p = QPushButton('P', self)
        self.p.setGeometry(877,249,82,100)
        self.p.setFont(QFont('Arial', 24))
        self.p.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.p.clicked.connect(self.insert_text)
        
        self.a = QPushButton('A', self)
        self.a.setGeometry(59,380,82,100)
        self.a.setFont(QFont('Arial', 24))
        self.a.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.a.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.s = QPushButton('S', self)
        self.s.setGeometry(149,380,82,100)
        self.s.setFont(QFont('Arial', 24))
        self.s.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.s.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.d = QPushButton('D', self)
        self.d.setGeometry(240,380,82,100)
        self.d.setFont(QFont('Arial', 24))
        self.d.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.d.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.f = QPushButton('F', self)
        self.f.setGeometry(331,380,82,100)
        self.f.setFont(QFont('Arial', 24))
        self.f.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.f.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.g = QPushButton('G', self)
        self.g.setGeometry(422,380,82,100)
        self.g.setFont(QFont('Arial', 24))
        self.g.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.g.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.h = QPushButton('H', self)
        self.h.setGeometry(513,380,82,100)
        self.h.setFont(QFont('Arial', 24))
        self.h.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.h.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.j = QPushButton('J', self)
        self.j.setGeometry(604,380,82,100)
        self.j.setFont(QFont('Arial', 24))
        self.j.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.j.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.k = QPushButton('K', self)
        self.k.setGeometry(695,380,82,100)
        self.k.setFont(QFont('Arial', 24))
        self.k.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.k.clicked.connect(self.insert_text)
        self.l = QPushButton('L', self)
        self.l.setGeometry(786,380,82,100)
        self.l.setFont(QFont('Arial', 24))
        self.l.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.l.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.col = QPushButton(':', self)
        self.col.setGeometry(877,380,82,100)
        self.col.setFont(QFont('Arial', 24))
        self.col.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.col.clicked.connect(self.insert_text)
        qq=u'\u21E7'

        self.shift = QPushButton(qq, self)
        self.shift.setGeometry(58,514,83,100)
        self.shift.setFont(QFont('Arial', 40))
        self.shift.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.shift.clicked.connect(self.shift1)
        
        #self.a.clicked.connect(self.call_delete1)
        self.z = QPushButton('Z', self)
        self.z.setGeometry(149,513,82,100)
        self.z.setFont(QFont('Arial', 24))
        self.z.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.z.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.x = QPushButton('X', self)
        self.x.setGeometry(240,513,82,100)
        self.x.setFont(QFont('Arial', 24))
        self.x.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.x.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.c = QPushButton('C', self)
        self.c.setGeometry(331,513,82,100)
        self.c.setFont(QFont('Arial', 24))
        self.c.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.c.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.v = QPushButton('V', self)
        self.v.setGeometry(422,513,82,100)
        self.v.setFont(QFont('Arial', 24))
        self.v.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.v.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.b = QPushButton('B', self)
        self.b.setGeometry(513,513,82,100)
        self.b.setFont(QFont('Arial', 24))
        self.b.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.b.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.n = QPushButton('N', self)
        self.n.setGeometry(604,513,82,100)
        self.n.setFont(QFont('Arial', 24))
        self.n.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.n.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        self.m = QPushButton('M', self)
        self.m.setGeometry(695,513,82,100)
        self.m.setFont(QFont('Arial', 24))
        self.m.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.m.clicked.connect(self.insert_text)
        self.po = QPushButton('.', self)
        self.po.setGeometry(786,513,82,100)
        self.po.setFont(QFont('Arial', 24))
        self.po.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.po.clicked.connect(self.insert_text)
        #self.a.clicked.connect(self.call_delete1)
        clr=u'\u232b'
        self.clear = QPushButton(clr, self)
        self.clear.setGeometry(877,513,82,100)
        self.clear.setFont(QFont('Arial', 24))
        self.clear.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.clear.clicked.connect(self.clear1)
        self.change = QPushButton('123', self)
        self.change.setGeometry(58,638,180,100)
        self.change.setFont(QFont('Arial', 24))
        self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.change.clicked.connect(self.change_numeric)
        
        self.dash = QPushButton('-', self)
        self.dash.setGeometry(253,638,125,100)
        self.dash.setFont(QFont('Arial', 24))
        self.dash.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.dash.clicked.connect(self.insert_text)
        
        self.space = QPushButton('space', self)
        self.space.setGeometry(388,638,338,100)
        self.space.setFont(QFont('Arial', 24))
        self.space.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
padding: 4px; color: black''')
        self.space.clicked.connect(self.space1)
        
        self.enter = QPushButton('enter', self)
        self.enter.setGeometry(738,638,230,100)
        self.enter.setFont(QFont('Arial', 24))
        self.enter.setStyleSheet('''background-color:white;border: none;border-style: outset;
border-width: 2px;
border-radius: 1px;
border-color: black;
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

        self.keyboard1=keyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        windoww.win.addSubWindow(self.keyboard1)
        self.keyboard1.show()
    def change_numeric(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.numerickeyboard1=numerickeyboard(self.mainwindowshow,self.previouswindow,self.entry.text())
        windoww.win.addSubWindow(self.numerickeyboard1)
        self.numerickeyboard1.show()

class popup1(QDialog):
    def __init__(self,name=None,name2=None):
        super().__init__()
        self.title = "App"
        self.name=name
        self.name2=name2
        #self.tablefirsttime=0
        self.InitUI()
    def InitUI(self):
            #a=QFrame()
            #print("start")
            self.setGeometry(237,209,550,350)
            self.setWindowModality(Qt.ApplicationModal)
            self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
            self.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(self)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Error',self)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel(self.name,self)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            no = QPushButton(self.name2, self)
            no.setGeometry(155,240,240,80)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(self.call_no)
            #self.show()
            #a.show()
    def call_no(self):
        self.close()
        #self.destroy()
        #gc.collect() 
        
class popup2(QDialog):
    def __init__(self,name=None,name2=None):
        super().__init__()
        self.title = "App"
        self.name=name
        self.name2=name2
        #self.tablefirsttime=0
        self.InitUI()
    def InitUI(self):
            #a=QFrame()
            #print("start")
            self.setGeometry(237,209,550,350)
            self.setWindowModality(Qt.ApplicationModal)
            self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
            self.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(self)
            self._gif.setGeometry(160,10,200,100)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("success2.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            movie.start()
            label1 = QLabel('Notification',self)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(220,130)
            label2 = QLabel(self.name,self)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            no = QPushButton(self.name2, self)
            no.setGeometry(165,240,240,80)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(self.call_no)
            #self.show()
            #a.show()
    def call_no(self):
        self.close()
        #self.destroy()
        #gc.collect() 
        
class UsersTable():

    def __init__(self,name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            #print(sqlite3.version)
        except sqlite3.Error as e:
            print("Failed connecting to database...")

    def create_table(self):
        c = self.cursor
        c.execute("""CREATE TABLE IF NOT EXISTS Userdata(Name TEXT,Employerid TEXT , Contact TEXT, Designation TEXT,ActionKey TEXT)""")
    def edit(self,query):#INSERT & UPDATE
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def select(self,query):#SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()
    def delete(self,query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()

class info():
    info1='none'

class testclass():
    test='notrunning'
class subwindow2(QMainWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    def __init__(self):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 0
       self.width = 1024
       self.height = 768
       self.InitUI()
       self.startUI()
    def startUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        y=c.execute("Select * from instrument where  key=1")

        for x in y:
                #print(x,x[0])
                #self.c_name_entry.setText(x[0])    companyname=''
  
                ins_screen.companyname=x[0]
                ins_screen.telephoneno=x[1]
                #self.tele_no_entry.setText(x[1])

        conn.commit()
        c.close()
        conn.close()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        #time = QTime.currentTime().toString()
        currentDT = datetime.now()
        date=currentDT.strftime("%d-%b-%Y")
        time=currentDT.strftime("%H:%M:%S")
        self.date_label.setText(date)
        self.time_label.setText(time)   
        x_t=self.temp_call()
        #my_gauge.value=x_t
        degree_sign=u'\u00B0'
        if(testclass.test=="running"):
            self.ct.setText(mainwindow1.toptext)
            self.ct1.setText(mainwindow1.lowertext)
        else:
            mainwindow1.toptext="Current Temperature"
            mainwindow1.lowertext='           '+str(x_t)+degree_sign+'C'
            self.ct.setText(mainwindow1.toptext)
            self.ct1.setText(mainwindow1.lowertext)
        #self.gauge.update_value(x_t)

       
    def InitUI(self):
        #self.setWindowTitle(self.title)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        #self.setWindowFlags(Qt.WindowStaysOnBottomHint) 
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label=QLabel(self)
        self.label.setPixmap(QPixmap('header.png'))
        self.label.setGeometry(0,0,1024,100)
        self.ct = QLabel(self)
        self.ct.setFont(QFont('Arial', 18))
        #self.ct.setWeight(QFont(Bold))
        self.ct.setStyleSheet('background-color:#efeeef;')
        self.ct.setGeometry(400, 13,500,30)
        self.ct1 = QLabel(self)
        self.ct1.setFont(QFont('Arial', 21))
        self.ct1.setStyleSheet('background-color:#efeeef;')
        self.ct1.setGeometry(400, 48,500,30)
        self.date_label = QLabel(self)
        self.date_label.setFont(QFont('Arial', 20,16))
        self.date_label.setStyleSheet('background-color:#efeeef;')
        self.date_label.setGeometry(800, 13,160,30)
        self.time_label = QLabel(self)
        self.time_label.setFont(QFont('Arial', 20,16))
        self.time_label.setStyleSheet('background-color:#efeeef;')
        self.time_label.setGeometry(830, 48,150,30)
        #self.ct.setObjectName("label")
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(100)
        windoww.win=self.mdi

        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
        y=c.execute("SELECT startmode from powerfailure")
        for x in y:
        #   #print(x[0])
         n=x[0]
        if(n==1):
          mySubwindow=subwindow()
          self.mdi.addSubWindow(mySubwindow)
          mySubwindow.close()
        else:
          mySubwindow=subwindow()
          self.mdi.addSubWindow(mySubwindow)
          #mySubwindow.close()
        # conn.commit()
        # c.close()
        # conn.close()

                #print(x)
        #mySubwindow.close()
        #self.us=userswindow(self)
        #self.setCentralWidget(self.mySubwindow)
       
        #self.mySubwindow.createWindow(1024,668)
        #mySubwindow.show()
        #self.show()
class mm():
    mm=''
class store():
  temp_list=[]
  time_list=[]
class subwindow(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #countChanged = pyqtSignal(int)
    #countChanged1=pyqtSignal(int)
    def __init__(self):
       #parent=None
       super().__init__()
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 0
       self.width = 1024
       self.height = 768
       self.one=0
       self.one1=0
       #self.mainwindow=mainwindow
       #self.faisal=faisal
       self.sUI()
       self.InitUI()
    def sUI(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor()
          
          #self.mdi.addSubWindow(self.my1)
        m=c.execute("Select * from sound where  key=1")
        for z in m:
            #print(z[0],'bool1')
            self.sounds=z[0]
        conn.commit()
        c.close()
        conn.close()
       
       #self.InitUI()
    def temp_call(self):
       
        try:
                t_call=float(temperature_read())
                t_call=round(t_call,1)
                return t_call
        except:
                return 55
    def updateTime(self):
        #print('faisal')
        time = QTime.currentTime().toString()
        x_t=self.temp_call()
        #my_gauge.value=x_t
       #self.label.setText(str(x_t))
        self.gauge.update_value(x_t)
        # if (c_to_f==0):
        #     my_gauge.value_min = 0
        #     my_gauge.value_max = 300
        # if (c_to_f==1):
        #     my_gauge.value_min = 32
        #     my_gauge.value_max = 572

       
    def InitUI(self):
        mm.mm=self
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setAttribute(Qt.WA_AcceptTouchEvents)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.gauge=AnalogGaugeWidget(self)
        self.gauge.setGeometry(660,250,320, 340)
        self.gauge.setStyleSheet("background-color:#f7f7ff;")
        #self.Form = QWidget()
        #self.ui = Ui_Form()
        #self.ui.setupUi(self.Form)
        #self.Form.show()
        # self.label = QLabel('uu',self)
        # self.label.setGeometry(165, 5, 61, 16)
        # self.label.setObjectName("label")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(10)
        #self.gauge.show()
        #self.s1 = Switch(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        buttonWindow1 = QPushButton('Start Test', self)
        buttonWindow1.setFont(QFont('Arial', 27))
        buttonWindow1.setGeometry(20,160,285,155)
        buttonWindow1.setStyleSheet('background-image: url(start.png);')
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
        Settings = QPushButton('Settings  ', self)
        Settings.setFont(QFont('Arial', 27))
        Settings.setGeometry(20,350,285,155)
        Settings.setStyleSheet('background-image: url(setting.png);')
        Settings.clicked.connect(self.settingswindow)
        User = QPushButton('User      ', self)
        User.setFont(QFont('Arial', 27))
        User.setGeometry(20,540,285,155)
        User.setStyleSheet('background-image: url(user.png);')
        User.clicked.connect(self.userswindow)
        
        
        Results = QPushButton('Results', self)
        Results.setFont(QFont('Arial', 27))
        Results.setGeometry(330,160,285,155)
        Results.setStyleSheet('background-image: url(Result.png);')
        Results.clicked.connect(self.resultswindow)
        
        #windoww.win.addSubWindow(self.rw)
        About = QPushButton('About  ', self)
        About.setFont(QFont('Arial', 27))
        About.setGeometry(330,350,285,155)
        About.setStyleSheet('background-image: url(about.png);')
        About.clicked.connect(self.aboutwindow)
        Damper = QPushButton('Damper ', self)
        Damper.setFont(QFont('Arial', 27))
        Damper.setGeometry(330,540,285,155)
        Damper.setStyleSheet('background-image: url(damper.png);')
        Damper.clicked.connect(self.damperwindow)
        self.n = QPushButton(self)
        self.n.setFont(QFont('Arial', 27))
        self.n.setGeometry(800,630,50,50)
        self.n.setStyleSheet('background-image: url(notification1.png);border: none;border-style: outset;')
        self.s = QPushButton(self)
        self.s.setCheckable(True)
        self.s.setFont(QFont('Arial', 27))
        self.s.setChecked(self.sounds)        
        self.s.setStyleSheet(("QPushButton{background-image: url(sound_on.png); color: white;border: none;} QPushButton:checked { background-image: url(sound_off.png);color:black; }"))
        self.s.clicked.connect(lambda sounds:self.control(sounds))
        self.s.setGeometry(715,630,80,50)
        #self.s.setStyleSheet('background-image: url(sound_on.png);border: none;border-style: outset;')         
#         self.change.setStyleSheet('''background-color:white;border: none;border-style: outset;
# border-width: 2px;
# border-radius: 1px;
# border-color: black;
# padding: 4px; color: black''')
        self.n.clicked.connect(self.notification_1)
        #self.close()
        self.start1()
        #self.one=1
        #objgraph.show_refs(self, filename='sample-graph.png')
        #self.show()
    def start1(self):
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        y=c.execute("SELECT startmode from powerfailure")
        for x in y:
          n=x[0]
        if(n==1):
          self.close()
          y1=c.execute("SELECT * FROM live")
          for x in y1:
            print(x[0],x[1])
            store.temp_list.append(float(x[1]))
            store.time_list.append(float(x[0]))

          temp_liststart=[]
                #c.execute("SELECT * FROM stuffToPlot ORDER BY key DESC LIMIT -1")
          c.execute("SELECT * FROM result ORDER BY Key DESC")
          result=c.fetchall()
          for row in result:
              temp_liststart.append(row)
              starttestdata.temperature=temp_liststart[0][2]
              starttestdata.hours='infinity'
              starttestdata.minutes='infinity'
              starttestdata.level=temp_liststart[0][6]
              starttestdata.fanspeed=temp_liststart[0][5]
              starttestdata.username=temp_liststart[0][4]
              starttestdata.key=temp_liststart[0][-1]
          del temp_liststart[:]
          self.my1=runninggraphwindow(self)
          windoww.win.addSubWindow(self.my1)
          self.my1.show()
    def control(self,sounds):
        print(sounds)
        if(sounds==True):
            self.sounds=1
        elif(sounds==False):
            self.sounds=0
        conn = sqlite3.connect('faisal.db')
        c = conn.cursor() 
        c.execute(f"Update sound set volume='{self.sounds}'where Key=1")

        conn.commit()
        c.close()               
        conn.close()
        #pass

    def buttonWindow1_onClick(self):
        self.close()
        #self.faisal.addSubWindow(self.rgwindow)
        #self.destroy()
        #gc.collect()
        self.rgwindow = startwindow(self)
        #self.faisal.addSubWindow(self.rgwindow)
        windoww.win.addSubWindow(self.rgwindow)
        self.rgwindow.show()
    def settingswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.s_w=settingswindow(self)
        windoww.win.addSubWindow(self.s_w)
        self.s_w.show()
        #self.close()
        #self.swindow = settingswindow()
        #self.swindow.show()
    def userswindow(self):
        self.close()
        #self.destroy()
        #gc.collect()
        self.uwindow = userswindow(self)
        windoww.win.addSubWindow(self.uwindow)
        #self.q.show()
        self.uwindow.show()
    def resultswindow(self):
        self.close()
        self.rw=result_window(self)
        windoww.win.addSubWindow(self.rw)
        self.rw.show()
        #self.close()
        #self.rswindow = resultswindow()
        #self.rswindow.show()
    def aboutwindow(self):
        self.close()
        self.a_s=about_screen(self)
        windoww.win.addSubWindow(self.a_s)
        self.a_s.show()
        #self.close()
        #self.abwindow = aboutwindow()
        #self.abwindow.show()
    def damperwindow(self):
        self.close()
        self.d_s=damper_screen(self)
        windoww.win.addSubWindow(self.d_s)
        self.d_s.show()
    def notification_1(self):
        self.close()
        self.n1=notification1(self)
        windoww.win.addSubWindow(self.n1)
        self.n1.show()





class userswindow(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    
    top = 0
    def __init__(self,name):
       super().__init__()
        
       #parent=None
       #super(instrumentwindow,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.insertfirsttime=0
       self.tablefirsttime=0
       self.m=name
       #self.e=name2
       #info.info1=2
       #print(info.info1)
       self.InitUI()

     
       
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        #self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.label = QLabel('Users Data',self)
        self.label.setFont(QFont('Arial', 19))
        self.label.setStyleSheet('background-color:#f7f7ff; color: black')
        self.label.setGeometry(400,120,220,50)


        self.back = QPushButton('Back', self)
        self.back.setGeometry(750,200,240,70)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.back.clicked.connect(self.call_back)
        self.addnewuser = QPushButton('Add New User', self)
        self.addnewuser.setGeometry(30,200,240,70)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.addnewuser.clicked.connect(self.call_add)
        self.edituser = QPushButton('Edit User', self)
        self.edituser.setGeometry(270,200,240,70)
        self.edituser.setFont(QFont('Arial', 21))
        #self.edituser.setStyleSheet('background-color:#4299ff; color: white')
        self.edituser.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.edituser.clicked.connect(self.call_edit)
        self.deleteuser = QPushButton('Delete User', self)
        self.deleteuser.setGeometry(510,200,240,70)
        self.deleteuser.setFont(QFont('Arial', 21))
        self.deleteuser.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.deleteuser.clicked.connect(self.call_delete1)

# tree = QTreeView()
# tree.model = QAbstractItemModel()
# tree.setModel(tree.model)

# size = QtCore.QSize(20, 20)
# index = tree.model.index(row, col)   # row, col are your own
# tree.model.setData(index, size, QtCore.Qt.SizeHintRole)

# delegate = MyDelegate()
# tree.setItemDelegate(delegate)

        self.dataView = extQTreeWidget1(self)
        #self.dataView.model=QAbstractItemModel()
        self.dataView.setRootIsDecorated(False)
        #self.dataView.setExpandsOnDoubleClick(True)
        #self.dataView.setContentsMargins(0,20,0,0)
        #self.dataView.setUniformRowHeights(True)
        #self.dataView.uniformRowHeights()
        #self.dataView.setAlternatingRowColors(True)
        self.dataView.setHeaderLabels(['Ref No','User Name','Employer Id','Contact','Designation'])
        #self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size: 21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        #item=QTreeWidgetItem(['Ref No','User Name','Employer Id','Contact','Designation'])
        #self.dataView.addTopLevelItem(item)
        #self.dataView.header().setStretchLastSection(False)
        #self.dataView.header().setResizeMode(6, QHeaderView.Stretch)
        self.dataView.header().setStyleSheet('padding-top:-2px;background-color:white;font-size:21pt; font-family: Arial;border-width:1px;border-style:outset;border-color:black; ')
        #self.dataView.header().setSelected(False)
        #self.dataView.header().setStretchLastSection(False)
        #self.dataView.header().sectionsMovable()
        #self.dataView.header().setResizeMode(0, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(1, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(2, QHeaderView.Stretch)
        self.dataView.header().setResizeMode(3, QHeaderView.Stretch)
        #self.dataView.header().setResizeMode(4, QHeaderView.Stretch)
        #self.dataView.header().setSectionResizeMode(Fixed)
        #font=QFont()            
        #font.setPointSize(22)
        #self.dataView.setPointSize(24)
        #self.dataView.header().setFont(font)
        #tree=QTreeWidget()
#tree.setHeaderLabels(['One','Two','Tree','Four','Five'])
# font=QFont()            
# font.setPointSize(24)
# tree.header().setFont(font)
        #self.dataView.setHeaderHidden(True)
        #self.dataView.Header().setVisible(False)
       #self.dataView.header().setResizeMode(False)
        self.dataView.setColumnCount(5)
        #self.dataView.setSizeHint(0,QSize(10,10))
        self.dataView.setColumnWidth(0,100)
        self.dataView.setColumnWidth(1,100)
        self.dataView.setColumnWidth(2,100)
        self.dataView.setColumnWidth(3,100)
        self.dataView.setColumnWidth(4,100)
        self.dataView.setColumnWidth(5,0)
        self.dataView.setStyleSheet('background-color:white;color: black;')
        #self.dataView.item.setStyleSheet('color:yellow;')
        self.dataView.setFont(QFont('Times New Roman', 22))
        #self.dataView.setIconSize(QSize(32,32))
        #self.create_table()
        self.insert_data()

##        l=[['faisal111111111111111111','12345','',''],['faisal','','',''],['faisal','','','']]
##        for x in l:
##           QTreeWidgetItem(self.dataView,x) 

        self.dataView.setGeometry(10,300,1010,465)
        #self.dataView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        QScroller.grabGesture(self.dataView.viewport(), QScroller.TouchGesture)
        #self.dataView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.dataView.itemClicked.connect(self.onItemClicked)
        #self.show()

    #@QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self):
        #global getChildNode
        getSelected = self.dataView.selectedItems()
        #if getSelected:
        baseNode = getSelected[0]
        self.getChildNode = baseNode.text(5)


    def create_table(self):
        if(self.tablefirsttime==0):
            self.tablefirsttime=1
            test = UsersTable("faisal.db")
            test.create_table()

        
    def insert_data(self):
        #if(self.insertfirsttime==0):
            #self.dataView.clear()
            self.insertfirsttime=1
            l=[]
            test = UsersTable("faisal.db")
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                #print(row)
                l.append(row)
            for i,x in enumerate(l):
                #print(i,x)
                QTreeWidgetItem(self.dataView,[str(i),x[0],x[1],x[2],x[3],x[4]]) 
            


    def call_back(self):
            self.close()
            self.m.show()
            #mm.mm.show()

    
    def call_add(self):
        #global getChildNode
        self.getChildNode=''
        adduserdata.username=''
        adduserdata.employerid=''
        adduserdata.contact=''
        adduserdata.designation=''
        self.close()
        #self.destroy()
        #gc.collect()
        self.y=adduser(self.m)
        windoww.win.addSubWindow(self.y)
        self.y.show()
        #self.close()
        #self.destroy()
        #gc.collect()
        #y=adduser()                            
        #y.exec_()
        #self.destroy()
        
        #gc.collect() 
        #self.svwindow = adduser()
        #self.svwindow.show()
        #del self
    def call_delete1(self):
        #global getChildNode
        #self.close()
        #self.svwindow = adduser()
        #self.svwindow.show()
        def call_no():
                a.close()
                gc.collect() 
                a.destroy()
        def call_delete():
            #global getChildNode
            l=[]
            #sip.delete(getChildNode)
            self.dataView.clear()
            test = UsersTable("faisal.db")
            #y=test.delete(f"SELECT * from stufftoplot WHERE {temp_search} LIKE '{mg}%';") 
            y=test.delete(f"DELETE from Userdata where ActionKey={self.getChildNode}") 
            x=test.select("SELECT * FROM Userdata order by ActionKey DESC")
            for row in x:
                    #print(row)
                    l.append(row)
            for i,x in enumerate(l):
                    #print(i,x)
                    QTreeWidgetItem(self.dataView,[str(i),x[0],x[1],x[2],x[3],x[4]])

            a.close()
            a.destroy()
            gc.collect()
            self.getChildNode=''
            #def call_no(self):
                #a.close()
        try:
            if len(self.getChildNode)==0:
                raise ValueError 
                #self.m=popup1(name='    Please select any user to continue',name2='Okay!')
                #self.m.show()
                
            
            print(len(self.getChildNode))
            a=QFrame()
            a.setGeometry(237,209,550,350)
            a.setWindowModality(Qt.ApplicationModal)
            a.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
            
            #a.setFocus()
            #a.activateWindow()
            #a.setWindowModality(QtCore.Qt.ApplicationModal)
            #a.setWindowState(a.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
            a.setStyleSheet('background-color:white;border:2px solid black')
            self._gif =QLabel(a)
            self._gif.move(215,30)
            self._gif.setStyleSheet('background-color:white;border:0px solid white')
            movie = QMovie("as4.gif")
            self._gif.setMovie(movie)
            movie.setSpeed(500)
            #movie.setDuration(1000)
            #movie.setLoopCount(2)
            #movie.setStartValue(QColor(0, 0, 0))
            #movie.setEndValue(QColor(255, 255, 255))
            #print(movie.state())
            movie.start()
            label1 = QLabel('Error',a)
            label1.setFont(QFont('Arialbold', 22))
            label1.setStyleSheet('background-color:white;border:0px solid white')
            label1.move(236,130)
            label2 = QLabel('Are you sure you want to delete this user !',a)
            label2.setFont(QFont('Arial', 19))
            label2.setStyleSheet('background-color:white;border:0px solid white')
            label2.move(50,170)
            yes_delete = QPushButton('Yes !', a)
            yes_delete .setGeometry(50,240,240,90)
            yes_delete .setFont(QFont('Arial', 21))
            yes_delete .setStyleSheet('background-color:#d00403; color: white')
            yes_delete .clicked.connect(call_delete)
            no = QPushButton('No', a)
            no.setGeometry(270,240,240,90)
            no.setFont(QFont('Arial', 21))
            no.setStyleSheet('background-color:#4299ff; color: white')
            no.clicked.connect(call_no)
            a.show()
        except:
            print("error")
            self.popup1=popup1(name='    Please select any user to continue',name2='Okay!')
            self.popup1.show()

        
        #if( movie.frameCount()>=21):
            #movie.stop()
        #movie.stop()
        #movie.jumpToFrame(0)
        #label = QLabel('', self)
        #movie = QMovie("as2.gif")
        #label.setMovie(movie)
        #movie.start() 
        
        
    def call_edit(self):
        #global getChildNode
        try:
            if len(self.getChildNode)==0:
                raise ValueError 
            self.close()
            #self.destroy()
            #gc.collect() 
            #info.info1=getChildNode
            #self.e.show()
            keydata.editdata=self.getChildNode
            self.edituser=edituser(self.m,self.getChildNode)
            windoww.win.addSubWindow(self.edituser)
            self.edituser.show()
            self.getChildNode=''
        except:
            print("error")
            self.popup1=popup1(name='      Please select any user to edit!',name2='Okay!')
            self.popup1.show()

    
        
class extQLineEdit(QLineEdit):
    def __init__(self,parent,get_entry):
        self.get_entry=get_entry
        QLineEdit.__init__(self,parent)
    def mousePressEvent(self,QMouseEvent):
        print("check",self.get_entry)
        if(self.get_entry=="e_user"):
            self.nk=numerickeyboard('')
            self.nk.show()
class extQLineEdit1(QLineEdit):
    #closeApp = pyqtSignal()
    #trigger = pyqtSignal()
    speak = pyqtSignal(str) 
    def __init__(self,parent):
          super(QLineEdit,self).__init__(parent)
    def mousePressEvent(self,QMouseEvent):
    #     self.trigger.emit()
         self.speak.emit('clicked()') 
         print("check")

class extQTreeWidget1(QTreeWidget):
    #closeApp = pyqtSignal()
    #trigger = pyqtSignal()
    #speak = Signal(str)         
    def __init__(self,parent):
          super(QTreeWidget,self).__init__(parent)
          self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
          QScroller.grabGesture(self.viewport(), QScroller.LeftMouseButtonGesture)
          self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)


class adduser(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    def __init__(self,name):
       #parent=None
       super().__init__() 
       #super(adduser,self).__init__(parent)
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 0
       self.width = 1024
       self.height = 768
       self.temp_user=''
       self.r=name
       self.InitUI()
       self.inserteditdata()
    def call_b(self,data):
        print("asdss",data)
        if(data=="a_user"):
            user_data=self.e_user.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="a_employer"):
            user_data=self.e_employer.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="a_contact"):
            user_data=self.e_contact.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=contactkeyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="a_designation"):
            user_data=self.e_designation.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
            
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose) 
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setStyleSheet('background-color:#f7f7ff;')
        self.bg = QLabel(self)
        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('userscreen.png'))
        self.bg.setGeometry(0,100,1024,668)

        self.label = QLabel('Add New User',self)
        self.label.setFont(QFont('Arial', 22))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(460,135,300,50)

        back = QPushButton('Back', self)
        back.setGeometry(755,547,190,75)
        back.setFont(QFont('Arial', 21))
        back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        back.clicked.connect(self.call_back)

        self.addnewuser = QPushButton('Add User', self)
        self.addnewuser.setGeometry(535,547,200,75)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.addnewuser.clicked.connect(self.call_add)


#self.entry = extQLineEdit(self,'entry2')
        self.e_user = extQLineEdit1(self)
        self.e_user.setFont(QFont('Arial', 21))
        self.e_user.setGeometry(469,240,493,53)
        self.e_user.setStyleSheet('background-color:white; color: black')
        self.e_user.setPlaceholderText('Enter User Name')
        self.e_user.speak.connect(partial(self.call_b,data='a_user'))

        self.e_employer = extQLineEdit1(self)
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,315,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')
        self.e_employer.setPlaceholderText('Enter Employer Id')
        self.e_employer.speak.connect(partial(self.call_b,data='a_employer'))

        self.e_contact = extQLineEdit1(self)
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,385,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')
        self.e_contact.setPlaceholderText('Enter Contact')
        self.e_contact.speak.connect(partial(self.call_b,data='a_contact'))

        self.e_designation = extQLineEdit1(self)
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,455,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')
        self.e_designation.setPlaceholderText('Enter Designation')
        self.e_designation.speak.connect(partial(self.call_b,data='a_designation'))

        self.user = QLabel('Enter Name',self)
        self.user.setFont(QFont('Arial', 19))
        self.user.setStyleSheet('background-color:white; color: black')
        self.user.setGeometry(70,270,300,30)

        self.employer_id = QLabel('Enter Employer ID',self)
        self.employer_id.setFont(QFont('Arial', 19))
        self.employer_id.setStyleSheet('background-color:white; color: black')
        self.employer_id.setGeometry(70,340,300,30)

        self.contact = QLabel('Enter Contact',self)
        self.contact.setFont(QFont('Arial', 19))
        self.contact.setStyleSheet('background-color:white; color: black')
        self.contact.setGeometry(70,410,300,30)

        self.designation = QLabel('Enter Designation',self)
        self.designation.setFont(QFont('Arial', 19))
        self.designation.setStyleSheet('background-color:white; color: black')
        self.designation.setGeometry(70,480,300,30)
        #self.exec_()
##    def __del__(self):
##        #print("destructor called")
##        self.destroy()
##        gc.collect()
    def inserteditdata(self):
            self.e_user.setText(adduserdata.username)
            self.e_employer.setText(adduserdata.employerid)
            self.e_contact.setText(adduserdata.contact)
            self.e_designation.setText(adduserdata.designation)
    def call_back(self):
        #self.destroy()
        self.close()
        #self.destroy()
        #weakref.ref(dialog, self.dialogs.remove)
        #gc.collect() 
        self.m=userswindow(self.r)
        windoww.win.addSubWindow(self.m)
        self.m.show()

        
        #dialog.destroyed.connect(self.on_destroyed)
        #self.dialogs.append(dialog)
        #self.m.exec_()
        #self.m.show()
        #del self
    def call_add(self):
        self.user_name = self.e_user.text()
        self.user_employerid = self.e_employer.text()
        self.user_contact = self.e_contact.text()
        self.user_designation = self.e_designation.text()
        try:
            if(len(self.user_name)==0 or len(self.user_employerid)==0):
               raise NameError
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select Name from Userdata")
            for x in y:
                print(x)
                for n in x:
                    if (self.user_name.lower()==n.lower()):
                        #print('True')
                        self.temp_user=True
                #self.m=popup1(name='',name2='')
                #self.m.show()
            if(self.temp_user==True):
                self.temp_user=False
                raise ValueError
            currentDT = datetime.now()
            key_1=currentDT.strftime("%Y%m%d%H%M%S")
            print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            #conn = sqlite3.connect('faisal.db')
            #c = conn.cursor()
            c.execute("INSERT INTO Userdata(Name,Employerid,Contact,Designation,ActionKey) VALUES(?,?,?,?,?)",(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1))
            conn.commit()
            c.close()
            conn.close()
            self.close()
            #self.destroy()
            #gc.collect()
            self.swindow = userswindow(self.r)
            windoww.win.addSubWindow(self.swindow)
            self.swindow.show()
            self.popup2=popup2(name='                User has been added !',name2='Close')
            self.popup2.show()
            
            
        except ValueError:
                print("error")
                self.popup1=popup1(name='           User is already present !',name2='Close')
                self.popup1.show()
        except NameError:
                print("error")
                self.popup1=popup1(name='            Please Enter All Values !',name2='Close')
                self.popup1.show()
            

class edituser(QMdiSubWindow):
        #def __init__(self, parent=None):
        #super(AnalogGaugeWidget, self).__init__(parent)
    #FROM, SUBJECT, DATE = range(3)
    def __init__(self,name,editdata):
       #parent=None
       super().__init__() 
       #self.setGeometry(0, 100, 1024, 668)
       self.title = "App"
       self.top = 0
       self.left = 100
       self.width = 1024
       self.height = 768
       self.r=name

       self.editdata=editdata
       self.temp_user=''
       
       

       #print(self.name)
       #print(instrumentwindow.top)
       self.InitUI()
       self.inserteditdata()
       
    def call_b(self,data):
        print("asdss",data)
        if(data=="e_user"):
            user_data=self.e_user.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="e_employer"):
            user_data=self.e_employer.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="e_contact"):
            user_data=self.e_contact.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=contactkeyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
        elif(data=="e_designation"):
            user_data=self.e_designation.text()
            self.close()
            #self.destroy()
            #gc.collect()
            self.nk=keyboard(self.r,data,user_data)
            windoww.win.addSubWindow(self.nk)
            self.nk.show()
       

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setStyleSheet('background-color:white;')
        self.bg = QLabel(self)
##        #self.pixmap = QPixmap('header.png')
        self.bg.setPixmap(QPixmap('userscreen.png'))
        self.bg.setGeometry(0,100,1024,668)

        self.label = QLabel('Edit Current User',self)
        self.label.setFont(QFont('Arial', 22))
        self.label.setStyleSheet('background-color:white; color: black')
        self.label.setGeometry(460,135,300,50)

        self.back = QPushButton('Back', self)
        self.back.setGeometry(755,547,190,75)
        self.back.setFont(QFont('Arial', 21))
        self.back.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.back.clicked.connect(self.call_back)

        self.addnewuser = QPushButton('Edit User', self)
        self.addnewuser.setGeometry(535,547,200,75)
        self.addnewuser.setFont(QFont('Arial', 21))
        self.addnewuser.setStyleSheet('''background-color:#4299ff;border: none;border-style: outset;
border-width: 0.5px;
border-radius: 0px;
border-color: black;
padding: 4px; color: black''')
        self.addnewuser.clicked.connect(self.call_edit)

        self.e_user = extQLineEdit1(self)
        self.e_user.setFont(QFont('Arial', 21))
        self.e_user.setGeometry(469,240,493,53)
        self.e_user.setStyleSheet('background-color:white; color: black')
        self.e_user.setPlaceholderText('Enter User Name')
        self.e_user.speak.connect(partial(self.call_b,data='e_user'))


        self.e_employer = extQLineEdit1(self)
        self.e_employer.setFont(QFont('Arial', 21))
        self.e_employer.setGeometry(469,315,492,53)
        self.e_employer.setStyleSheet('background-color:white; color: black')
        self.e_employer.setPlaceholderText('Enter Employer Id')
        self.e_employer.speak.connect(partial(self.call_b,data='e_employer'))

        self.e_contact = extQLineEdit1(self)
        self.e_contact.setFont(QFont('Arial', 21))
        self.e_contact.setGeometry(469,385,493,53)
        self.e_contact.setStyleSheet('background-color:white; color: black')
        self.e_contact.setPlaceholderText('Enter Contact')
        self.e_contact.speak.connect(partial(self.call_b,data='e_contact'))

        self.e_designation = extQLineEdit1(self)
        self.e_designation.setFont(QFont('Arial', 21))
        self.e_designation.setGeometry(469,455,492,53)
        self.e_designation.setStyleSheet('background-color:white; color: black')
        self.e_designation.setPlaceholderText('Enter Designation')
        self.e_designation.speak.connect(partial(self.call_b,data='e_designation'))

        self.user = QLabel('Enter Name',self)
        self.user.setFont(QFont('Arial', 19))
        self.user.setStyleSheet('background-color:white; color: black')
        self.user.setGeometry(70,270,300,30)

        self.employer_id = QLabel('Enter Employer ID',self)
        self.employer_id.setFont(QFont('Arial', 19))
        self.employer_id.setStyleSheet('background-color:white; color: black')
        self.employer_id.setGeometry(70,340,300,30)

        self.contact = QLabel('Enter Contact',self)
        self.contact.setFont(QFont('Arial', 19))
        self.contact.setStyleSheet('background-color:white; color: black')
        self.contact.setGeometry(70,410,300,30)

        self.designation = QLabel('Enter Designation',self)
        self.designation.setFont(QFont('Arial', 19))
        self.designation.setStyleSheet('background-color:white; color: black')
        self.designation.setGeometry(70,480,300,30)




##    def __del__(self):
##        #print("destructor called")
##        self.destroy()
##        gc.collect()

    def call_back(self):
        #self.destroy()
        #weakref.ref(dialog, self.dialogs.remove)
        #gc.collect() 

        self.close()
        self.m=userswindow(self.r)
        windoww.win.addSubWindow(self.m)
        self.m.show()

    def inserteditdata(self):
        if(len(self.editdata)>0):
            l=[]
            
            try:
                test = UsersTable("faisal.db")
                y=test.select(f"Select * from Userdata where ActionKey={self.editdata}")
                for row in y:
                        print(row)
                        l.append(row)
                self.e_user.setText(l[0][0])
                self.e_employer.setText(l[0][1])
                self.e_contact.setText(l[0][2])
                self.e_designation.setText(l[0][3])
                keydata.username=self.e_user.text()
                keydata.employerid=self.e_employer.text()
                keydata.contact=self.e_contact.text()
                keydata.designation=self.e_designation.text()

            except:
                print('insideeditdataerror')
        else:
            self.e_user.setText(keydata.username)
            self.e_employer.setText(keydata.employerid)
            self.e_contact.setText(keydata.contact)
            self.e_designation.setText(keydata.designation)

            
    def call_edit(self):
        #test = UsersTable("faisal.db")
        #y=test.delete(f"SELECT * from stufftoplot WHERE {temp_search} LIKE '{mg}%';") 
        #y=test.delete(f"DELETE from Userdata where ActionKey={self.name}") 
        self.user_name = self.e_user.text()
        self.user_employerid = self.e_employer.text()
        self.user_contact = self.e_contact.text()
        self.user_designation = self.e_designation.text()
        try:
            if(len(self.user_name)==0 or len(self.user_employerid)==0):
               raise NameError
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            y=c.execute("Select Name from Userdata")
            for x in y:
                print(x)
                for n in x:
                    if (self.user_name.lower()==n.lower()):
                        #print('True')
                        self.temp_user=True
                #self.m=popup1(name='',name2='')
                #self.m.show()
            if(self.temp_user==True):
                self.temp_user=False
                raise ValueError
            currentDT = datetime.now()
            key_1=currentDT.strftime("%Y%m%d%H%M%S")
            #print(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),key_1)
            conn = sqlite3.connect('faisal.db')
            c = conn.cursor()
            c.execute(f"DELETE from Userdata where ActionKey={keydata.editdata}") 
            c.execute("INSERT INTO Userdata(Name,Employerid,Contact,Designation,ActionKey) VALUES(?,?,?,?,?)",(self.user_name.strip(),self.user_employerid.strip(),self.user_contact.strip(),self.user_designation.strip(),keydata.editdata))
            conn.commit()
            c.close()
            conn.close()
            self.close()
            #self.destroy()
            #gc.collect()
            self.swindow = userswindow(self.r)
            windoww.win.addSubWindow(self.swindow)
            self.swindow.show()
            self.popup2=popup2(name='                User has been edited !',name2='Close')
            self.popup2.show()

        except ValueError:
                print("error")
                self.popup1=popup1(name='           User is already present !',name2='Close')
                self.popup1.show()
        except NameError:
                print("error")
                self.popup1=popup1(name='            Please Enter All Values !',name2='Close')
                self.popup1.show()
class password_screen():
    password=''
class ins_screen():
    companyname=''
    telephoneno=''
class point_2calibration():
    e_p1=''
    e_p2=''
class point_1calibration():
    e_p1=''
class starttestdata():
    temperature=''
    hours=''
    minutes=''
    level=''
    fanspeed=''
    username=''
    key=''
class adduserdata():
    username=''
    employerid=''
    contact=''
    designation=''

class keydata():
    username=None
    employerid=''
    contact=''
    designation=''
    editdata=''
class mainwindow1():
    toptext='Current Temperature'
    lowertext=''
class windoww():
    win=''
if __name__ == '__main__':
    import sys
    #from mem_top import mem_top
    #print(mem_top())
    app = QApplication(sys.argv)
    gc.enable()
    w = subwindow2()
    #windoww.win=w
    w.show()
    sys.exit(app.exec_())
