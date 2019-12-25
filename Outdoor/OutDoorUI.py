# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutDoor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(328, 190)
        Frame.setStyleSheet("background-color: rgb(188, 188, 188);")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineEdit_inputNumber = QtWidgets.QLineEdit(Frame)
        self.lineEdit_inputNumber.setGeometry(QtCore.QRect(42, 34, 231, 45))
        self.lineEdit_inputNumber.setObjectName("lineEdit_inputNumber")
        self.pushbutton_exit = QtWidgets.QPushButton(Frame)
        self.pushbutton_exit.setGeometry(QtCore.QRect(40, 120, 99, 27))
        self.pushbutton_exit.setObjectName("pushbutton_exit")
        self.pushButtonEnter = QtWidgets.QPushButton(Frame)
        self.pushButtonEnter.setGeometry(QtCore.QRect(172, 120, 99, 27))
        self.pushButtonEnter.setObjectName("pushButtonEnter")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushbutton_exit.setText(_translate("Frame", "Hủy"))
        self.pushButtonEnter.setText(_translate("Frame", "Xác nhận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
