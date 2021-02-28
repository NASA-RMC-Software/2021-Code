#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#from PyQt5.QtCore import pyqtSlot
#import sys

#app = QApplication(sys.argv)
#win = QMainWindow()
#win.setGeometry(200, 200, 300, 300) #(x, y, width, height)
#win.setWindowTitle("It's Time Boys")

#button = QPushButton('On', win)
#button.setToolTip('This is to turn the robot on and off')
#button.move(0,0)

#win.show()
#sys.exit(app.exec_())

#window()

import sys

import logging
from datetime import datetime 

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

#accessing QtDesigner File
window = uic.loadUi("GCSStart.ui")


#logger stoof

timestamp = datetime.today()

LoggerTest = open("LoggerTest.txt","r")

print(timestamp, LoggerTest.read())

#showing GUI and executing command
window.show()
app.exec()