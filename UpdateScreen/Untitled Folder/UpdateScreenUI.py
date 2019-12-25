# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(477, 286)
        Frame.setStyleSheet("background-color: rgb(0, 200, 255);")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_dangCapNhat = QtWidgets.QLabel(Frame)
        self.label_dangCapNhat.setGeometry(QtCore.QRect(20, 2, 439, 43))
        self.label_dangCapNhat.setStyleSheet("color: rgb(66, 66, 66);\n"
"font: 75 bold 16pt \"Ubuntu\";")
        self.label_dangCapNhat.setObjectName("label_dangCapNhat")
        self.frame_showInformation = QtWidgets.QFrame(Frame)
        self.frame_showInformation.setGeometry(QtCore.QRect(8, 42, 461, 193))
        self.frame_showInformation.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.frame_showInformation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_showInformation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showInformation.setObjectName("frame_showInformation")
        self.label_daXuLy = QtWidgets.QLabel(self.frame_showInformation)
        self.label_daXuLy.setGeometry(QtCore.QRect(30, 4, 367, 31))
        self.label_daXuLy.setStyleSheet("font: 75 bold 11pt \"Ubuntu\";")
        self.label_daXuLy.setObjectName("label_daXuLy")
        self.label_loi = QtWidgets.QLabel(self.frame_showInformation)
        self.label_loi.setGeometry(QtCore.QRect(30, 34, 367, 31))
        self.label_loi.setStyleSheet("font: 75 bold 11pt \"Ubuntu\";")
        self.label_loi.setObjectName("label_loi")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(312, 240, 143, 37))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_dangCapNhat.setText(_translate("Frame", "ĐANG CẬP NHẤT CƠ SỞ DỮ LIỆU"))
        self.label_daXuLy.setText(_translate("Frame", "Đã cập nhật x/x thí sinh"))
        self.label_loi.setText(_translate("Frame", "Lỗi x thí sinh"))
        self.pushButton.setText(_translate("Frame", "Hủy câp nhật"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
