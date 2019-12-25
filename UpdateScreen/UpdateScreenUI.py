# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrameContainUpdateScreen(object):
    def setupUi(self, FrameContainUpdateScreen):
        FrameContainUpdateScreen.setObjectName("FrameContainUpdateScreen")
        FrameContainUpdateScreen.resize(659, 423)
        FrameContainUpdateScreen.setStyleSheet("background-color: rgb(255, 255, 235);")
        FrameContainUpdateScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        FrameContainUpdateScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line = QtWidgets.QFrame(FrameContainUpdateScreen)
        self.line.setGeometry(QtCore.QRect(60, 80, 545, 1))
        self.line.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(FrameContainUpdateScreen)
        self.label.setGeometry(QtCore.QRect(8, 4, 85, 75))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FrameContainUpdateScreen)
        self.label_2.setGeometry(QtCore.QRect(100, 12, 549, 51))
        self.label_2.setStyleSheet("color: rgb(59, 59, 59);\n"
"font: 75 bold 20pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.frame_containCourseInfo = QtWidgets.QFrame(FrameContainUpdateScreen)
        self.frame_containCourseInfo.setGeometry(QtCore.QRect(6, 88, 303, 169))
        self.frame_containCourseInfo.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-radius:7px")
        self.frame_containCourseInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containCourseInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containCourseInfo.setObjectName("frame_containCourseInfo")
        self.label_3 = QtWidgets.QLabel(self.frame_containCourseInfo)
        self.label_3.setGeometry(QtCore.QRect(32, 6, 251, 33))
        self.label_3.setStyleSheet("color: rgb(0, 0, 124);")
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_containCourseInfo)
        self.frame_3.setGeometry(QtCore.QRect(2, 40, 297, 125))
        self.frame_3.setStyleSheet("border-width:1px;\n"
"border-color:rgb(180, 180, 180)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(0, 42, 297, 1))
        self.line_2.setStyleSheet("border-style:solid;\n"
"border-width:0px;\n"
"background-color: rgb(180, 180, 180)")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(0, 82, 297, 1))
        self.line_3.setStyleSheet("border-style:solid;\n"
"border-width:0px;\n"
"background-color: rgb(180, 180, 180)")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(8, 6, 65, 31))
        self.label_4.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_4.setObjectName("label_4")
        self.label_forShowDataTime = QtWidgets.QLabel(self.frame_3)
        self.label_forShowDataTime.setGeometry(QtCore.QRect(122, 6, 163, 31))
        self.label_forShowDataTime.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_forShowDataTime.setObjectName("label_forShowDataTime")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(8, 86, 101, 31))
        self.label_7.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_7.setObjectName("label_7")
        self.label_forShowNumberStudent = QtWidgets.QLabel(self.frame_3)
        self.label_forShowNumberStudent.setGeometry(QtCore.QRect(122, 86, 163, 31))
        self.label_forShowNumberStudent.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_forShowNumberStudent.setText("")
        self.label_forShowNumberStudent.setObjectName("label_forShowNumberStudent")
        self.label_forShowCourseName = QtWidgets.QLabel(self.frame_3)
        self.label_forShowCourseName.setGeometry(QtCore.QRect(122, 48, 163, 31))
        self.label_forShowCourseName.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_forShowCourseName.setObjectName("label_forShowCourseName")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(8, 48, 93, 31))
        self.label_9.setStyleSheet("border-style:solid;\n"
"border-width:0px")
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(FrameContainUpdateScreen)
        self.frame_2.setGeometry(QtCore.QRect(6, 262, 303, 155))
        self.frame_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-radius:7px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(8, 8, 93, 39))
        self.label_10.setStyleSheet("color: rgb(0, 0, 124);")
        self.label_10.setObjectName("label_10")
        self.label_forShowNumberUpdated = QtWidgets.QLabel(self.frame_2)
        self.label_forShowNumberUpdated.setGeometry(QtCore.QRect(110, 6, 187, 41))
        self.label_forShowNumberUpdated.setStyleSheet("color: rgb(61, 61, 61);\n"
"font: 57 bold 14pt \"Ubuntu\";")
        self.label_forShowNumberUpdated.setObjectName("label_forShowNumberUpdated")
        self.pushButton_cancerUpdate = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_cancerUpdate.setGeometry(QtCore.QRect(162, 106, 131, 39))
        self.pushButton_cancerUpdate.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(221, 0, 0);")
        self.pushButton_cancerUpdate.setObjectName("pushButton_cancerUpdate")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(8, 48, 93, 37))
        self.label_12.setStyleSheet("color: rgb(0, 0, 124);")
        self.label_12.setObjectName("label_12")
        self.label_forShowNumberError = QtWidgets.QLabel(self.frame_2)
        self.label_forShowNumberError.setGeometry(QtCore.QRect(110, 42, 185, 41))
        self.label_forShowNumberError.setStyleSheet("color: rgb(61, 61, 61);\n"
"font: 57 bold 14pt \"Ubuntu\";")
        self.label_forShowNumberError.setObjectName("label_forShowNumberError")
        self.frame_4 = QtWidgets.QFrame(FrameContainUpdateScreen)
        self.frame_4.setGeometry(QtCore.QRect(316, 88, 337, 329))
        self.frame_4.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style:solid;\n"
"border-radius:7px")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.retranslateUi(FrameContainUpdateScreen)
        QtCore.QMetaObject.connectSlotsByName(FrameContainUpdateScreen)

    def retranslateUi(self, FrameContainUpdateScreen):
        _translate = QtCore.QCoreApplication.translate
        FrameContainUpdateScreen.setWindowTitle(_translate("FrameContainUpdateScreen", "Frame"))
        self.label_2.setText(_translate("FrameContainUpdateScreen", "CẬP NHẬT DANH SÁCH HỌC VIÊN"))
        self.label_3.setText(_translate("FrameContainUpdateScreen", "THÔNG TIN KHÓA HỌC"))
        self.label_4.setText(_translate("FrameContainUpdateScreen", "Ngày"))
        self.label_forShowDataTime.setText(_translate("FrameContainUpdateScreen", "TextLabel"))
        self.label_7.setText(_translate("FrameContainUpdateScreen", "Số học viên"))
        self.label_forShowCourseName.setText(_translate("FrameContainUpdateScreen", "Tên Khóa hoc"))
        self.label_9.setText(_translate("FrameContainUpdateScreen", "Tên khóa"))
        self.label_10.setText(_translate("FrameContainUpdateScreen", "ĐÃ XONG"))
        self.label_forShowNumberUpdated.setText(_translate("FrameContainUpdateScreen", "0/0"))
        self.pushButton_cancerUpdate.setText(_translate("FrameContainUpdateScreen", "HỦY CẬP NHÂT"))
        self.label_12.setText(_translate("FrameContainUpdateScreen", "LỖI"))
        self.label_forShowNumberError.setText(_translate("FrameContainUpdateScreen", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrameContainUpdateScreen = QtWidgets.QFrame()
    ui = Ui_FrameContainUpdateScreen()
    ui.setupUi(FrameContainUpdateScreen)
    FrameContainUpdateScreen.show()
    sys.exit(app.exec_())
