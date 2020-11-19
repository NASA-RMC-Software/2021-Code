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

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

#accessing QtDesigner File
window = uic.loadUi("GCSStart.ui")

#showing GUI and executing command
window.show()
app.exec()