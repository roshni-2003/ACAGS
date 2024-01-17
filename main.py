import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import teacher_UI

app = QApplication(sys.argv)

MainWindow = QMainWindow()

teacher_ui = teacher_UI.Ui_MainWindow.get_ui_instance(MainWindow)

MainWindow.show()
sys.exit(app.exec_())