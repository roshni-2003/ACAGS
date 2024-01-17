from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import sys
import teacher_UI,student_UI,Warning_UI,final_UI
from PyQt5.uic import *
class Open():
    def __init__(self,data):
        self.data=data
        if(self.data=="teacher"):
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            ui = teacher_UI.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
        elif(self.data=="student"):
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            ui = student_UI.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
        elif(self.data=="warning"):
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            ui = Warning_UI.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
        elif(self.data=="final"):
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            ui = final_UI.Ui_Dialog()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
class MainWindow(QMainWindow,QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=loadUi("UI_main.ui",self)
