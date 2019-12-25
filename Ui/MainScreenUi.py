# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_MainScreen(object):
    def setupUi(self, Frame_MainScreen):
        Frame_MainScreen.setObjectName("Frame_MainScreen")
        Frame_MainScreen.resize(800, 480)
        Frame_MainScreen.setStyleSheet("background-color: rgb(167, 200, 191);\n"
"")
        Frame_MainScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame_MainScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containName = QtWidgets.QFrame(Frame_MainScreen)
        self.frame_containName.setGeometry(QtCore.QRect(0, 2, 799, 59))
        self.frame_containName.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.frame_containName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containName.setObjectName("frame_containName")
        self.label_cty = QtWidgets.QLabel(self.frame_containName)
        self.label_cty.setGeometry(QtCore.QRect(114, -6, 539, 37))
        self.label_cty.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 75 bold 14pt \"Ubuntu\";")
        self.label_cty.setIndent(-1)
        self.label_cty.setObjectName("label_cty")
        self.label_trungTam = QtWidgets.QLabel(self.frame_containName)
        self.label_trungTam.setGeometry(QtCore.QRect(182, 28, 453, 27))
        self.label_trungTam.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";\n"
"color: rgb(255, 0, 0);")
        self.label_trungTam.setObjectName("label_trungTam")
        self.label_7 = QtWidgets.QLabel(self.frame_containName)
        self.label_7.setGeometry(QtCore.QRect(654, 4, 155, 37))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../icon/iconEcotek.png"))
        self.label_7.setObjectName("label_7")
        self.pushButton_shutdown = QtWidgets.QPushButton(self.frame_containName)
        self.pushButton_shutdown.setGeometry(QtCore.QRect(8, 2, 39, 35))
        self.pushButton_shutdown.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius:2px;")
        self.pushButton_shutdown.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/iconShutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_shutdown.setIcon(icon)
        self.pushButton_shutdown.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_shutdown.setObjectName("pushButton_shutdown")
        self.line = QtWidgets.QFrame(Frame_MainScreen)
        self.line.setGeometry(QtCore.QRect(132, 52, 487, 17))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(Frame_MainScreen)
        self.frame.setGeometry(QtCore.QRect(350, 66, 441, 205))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:7px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(5)
        self.frame.setObjectName("frame")
        self.label_forShowName = QtWidgets.QLabel(self.frame)
        self.label_forShowName.setGeometry(QtCore.QRect(166, 44, 263, 103))
        self.label_forShowName.setStyleSheet("font: 75 bold 22pt \"Ubuntu\";\n"
"color: rgb(70, 70, 70);\n"
"border-radius:3px;\n"
"")
        self.label_forShowName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_forShowName.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_forShowName.setLineWidth(1)
        self.label_forShowName.setMidLineWidth(0)
        self.label_forShowName.setWordWrap(True)
        self.label_forShowName.setObjectName("label_forShowName")
        self.frame_containLabelShowRegisImage = QtWidgets.QFrame(self.frame)
        self.frame_containLabelShowRegisImage.setGeometry(QtCore.QRect(10, 8, 149, 183))
        self.frame_containLabelShowRegisImage.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.frame_containLabelShowRegisImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containLabelShowRegisImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containLabelShowRegisImage.setObjectName("frame_containLabelShowRegisImage")
        self.label_regisImage = QtWidgets.QLabel(self.frame_containLabelShowRegisImage)
        self.label_regisImage.setGeometry(QtCore.QRect(8, 10, 131, 165))
        self.label_regisImage.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_regisImage.setText("")
        self.label_regisImage.setPixmap(QtGui.QPixmap("../icon/iconImageRepresent.png"))
        self.label_regisImage.setObjectName("label_regisImage")
        self.label_showConnectOrDisconnect = QtWidgets.QLabel(self.frame)
        self.label_showConnectOrDisconnect.setGeometry(QtCore.QRect(412, 6, 16, 16))
        self.label_showConnectOrDisconnect.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius:8")
        self.label_showConnectOrDisconnect.setText("")
        self.label_showConnectOrDisconnect.setObjectName("label_showConnectOrDisconnect")
        self.frame_3 = QtWidgets.QFrame(Frame_MainScreen)
        self.frame_3.setGeometry(QtCore.QRect(10, 66, 329, 405))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width:5px;\n"
"border-radius:7px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_containLabelShowCamera = QtWidgets.QFrame(self.frame_3)
        self.frame_containLabelShowCamera.setGeometry(QtCore.QRect(16, 8, 297, 391))
        self.frame_containLabelShowCamera.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.frame_containLabelShowCamera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containLabelShowCamera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containLabelShowCamera.setObjectName("frame_containLabelShowCamera")
        self.label_showCamera = QtWidgets.QLabel(self.frame_containLabelShowCamera)
        self.label_showCamera.setGeometry(QtCore.QRect(0, 0, 283, 381))
        self.label_showCamera.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_showCamera.setText("")
        self.label_showCamera.setObjectName("label_showCamera")
        self.frame_containWarning = QtWidgets.QFrame(Frame_MainScreen)
        self.frame_containWarning.setGeometry(QtCore.QRect(350, 280, 441, 191))
        self.frame_containWarning.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-radius:7px;")
        self.frame_containWarning.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containWarning.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containWarning.setLineWidth(3)
        self.frame_containWarning.setMidLineWidth(2)
        self.frame_containWarning.setObjectName("frame_containWarning")
        self.label_iconWarning = QtWidgets.QLabel(self.frame_containWarning)
        self.label_iconWarning.setGeometry(QtCore.QRect(190, 6, 81, 73))
        self.label_iconWarning.setText("")
        self.label_iconWarning.setPixmap(QtGui.QPixmap("../icon/iconOk.png"))
        self.label_iconWarning.setObjectName("label_iconWarning")
        self.label_warningContentText = QtWidgets.QLabel(self.frame_containWarning)
        self.label_warningContentText.setGeometry(QtCore.QRect(26, 86, 389, 89))
        self.label_warningContentText.setStyleSheet("color: rgb(0, 143, 0);\n"
"font: 75 bold 16pt \"Ubuntu\";")
        self.label_warningContentText.setAlignment(QtCore.Qt.AlignCenter)
        self.label_warningContentText.setObjectName("label_warningContentText")

        self.retranslateUi(Frame_MainScreen)
        QtCore.QMetaObject.connectSlotsByName(Frame_MainScreen)

    def retranslateUi(self, Frame_MainScreen):
        _translate = QtCore.QCoreApplication.translate
        Frame_MainScreen.setWindowTitle(_translate("Frame_MainScreen", "Frame"))
        self.label_cty.setText(_translate("Frame_MainScreen", "TRƯỜNG CAO ĐẲNG CÔNG NGHIỆP VÀ XÂY DỰNG"))
        self.label_trungTam.setText(_translate("Frame_MainScreen", "TRUNG TÂM ĐÀO TẠO VÀ SÁT HẠCH LÁI XE"))
        self.label_forShowName.setText(_translate("Frame_MainScreen", "CHƯA NHẬN ĐƯỢC THÔNG TIN"))
        self.label_warningContentText.setText(_translate("Frame_MainScreen", "NHẬN DIỆN THÀNH CÔNG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_MainScreen = QtWidgets.QFrame()
    ui = Ui_Frame_MainScreen()
    ui.setupUi(Frame_MainScreen)
    Frame_MainScreen.show()
    sys.exit(app.exec_())
