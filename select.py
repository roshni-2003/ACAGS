# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Selected.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QFileDialog,QMainWindow,QWidget,QPushButton
class Ui_Selecting_file(object):
    def setupUi(self, Selecting_file):
        Selecting_file.setObjectName("Selecting_file")
        Selecting_file.resize(328, 118)
        self.pushButton = QtWidgets.QPushButton(Selecting_file)
        self.pushButton.setGeometry(QtCore.QRect(90, 30, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browsefiles)
        self.retranslateUi(Selecting_file)
        QtCore.QMetaObject.connectSlotsByName(Selecting_file)
    def browsefiles(self):
        filename = QFileDialog.getOpenFileName()

    def retranslateUi(self, Selecting_file):
        _translate = QtCore.QCoreApplication.translate
        Selecting_file.setWindowTitle(_translate("Selecting_file", "Select"))
        self.pushButton.setText(_translate("Selecting_file", "Selecting file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Selecting_file = QtWidgets.QDialog()
    ui = Ui_Selecting_file()
    ui.setupUi(Selecting_file)
    Selecting_file.show()
    sys.exit(app.exec_())
