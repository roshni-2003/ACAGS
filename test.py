import student_UI,teacher_UI,Warning_UI,final_UI
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI_main import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from teacher_UI import Ui_MainWindow as teacher
import sys
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = teacher()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print(ui.file_name())
    sys.exit(app.exec_())

