# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.resize(294, 131)
        self.label = QtWidgets.QLabel(Warning)
        self.label.setGeometry(QtCore.QRect(90, 50, 171, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Warning)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        _translate = QtCore.QCoreApplication.translate
        Warning.setWindowTitle(_translate("Warning", "Warning"))
        self.label.setText(_translate("Warning", "No File has been found"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Warning = QtWidgets.QDialog()
    ui = Ui_Warning()
    ui.setupUi(Warning)
    Warning.show()
    sys.exit(app.exec_())