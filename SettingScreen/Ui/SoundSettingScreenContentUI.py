# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoiDungManHinhCaiDatAmThanh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget_ContainSoundSettingContent(object):
    def setupUi(self, Widget_ContainSoundSettingContent):
        Widget_ContainSoundSettingContent.setObjectName("Widget_ContainSoundSettingContent")
        Widget_ContainSoundSettingContent.resize(420, 381)
        self.frame_containVolumeSetting = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.frame_containVolumeSetting.setGeometry(QtCore.QRect(0, 56, 421, 81))
        self.frame_containVolumeSetting.setStyleSheet("border:0px;")
        self.frame_containVolumeSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containVolumeSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containVolumeSetting.setObjectName("frame_containVolumeSetting")
        self.label_amLuong = QtWidgets.QLabel(self.frame_containVolumeSetting)
        self.label_amLuong.setGeometry(QtCore.QRect(10, 10, 295, 21))
        self.label_amLuong.setMouseTracking(True)
        self.label_amLuong.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";")
        self.label_amLuong.setObjectName("label_amLuong")
        self.label_iconVolume = QtWidgets.QLabel(self.frame_containVolumeSetting)
        self.label_iconVolume.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.label_iconVolume.setText("")
        self.label_iconVolume.setPixmap(QtGui.QPixmap("iconVolume.png"))
        self.label_iconVolume.setObjectName("label_iconVolume")
        self.horizontalSlider_ForChangeVolume = QtWidgets.QSlider(self.frame_containVolumeSetting)
        self.horizontalSlider_ForChangeVolume.setGeometry(QtCore.QRect(80, 40, 251, 29))
        self.horizontalSlider_ForChangeVolume.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_ForChangeVolume.setObjectName("horizontalSlider_ForChangeVolume")
        self.frame_containSilentSetting = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.frame_containSilentSetting.setGeometry(QtCore.QRect(0, 150, 421, 107))
        self.frame_containSilentSetting.setStyleSheet("border:0px;")
        self.frame_containSilentSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containSilentSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containSilentSetting.setObjectName("frame_containSilentSetting")
        self.label_cheDoImLang = QtWidgets.QLabel(self.frame_containSilentSetting)
        self.label_cheDoImLang.setGeometry(QtCore.QRect(10, 10, 365, 21))
        self.label_cheDoImLang.setMouseTracking(True)
        self.label_cheDoImLang.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";")
        self.label_cheDoImLang.setObjectName("label_cheDoImLang")
        self.comboBox_ForChooseYesOrNoSilent = QtWidgets.QComboBox(self.frame_containSilentSetting)
        self.comboBox_ForChooseYesOrNoSilent.setGeometry(QtCore.QRect(10, 64, 161, 31))
        self.comboBox_ForChooseYesOrNoSilent.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);")
        self.comboBox_ForChooseYesOrNoSilent.setObjectName("comboBox_ForChooseYesOrNoSilent")
        self.label_ctKhongPhatAmvv = QtWidgets.QLabel(self.frame_containSilentSetting)
        self.label_ctKhongPhatAmvv.setGeometry(QtCore.QRect(10, 34, 391, 21))
        self.label_ctKhongPhatAmvv.setMouseTracking(True)
        self.label_ctKhongPhatAmvv.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 25 10pt \"Ubuntu\";")
        self.label_ctKhongPhatAmvv.setWordWrap(True)
        self.label_ctKhongPhatAmvv.setObjectName("label_ctKhongPhatAmvv")
        self.frame_ContainSoundMessageSetting = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.frame_ContainSoundMessageSetting.setGeometry(QtCore.QRect(0, 270, 421, 109))
        self.frame_ContainSoundMessageSetting.setStyleSheet("border:0px;")
        self.frame_ContainSoundMessageSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ContainSoundMessageSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ContainSoundMessageSetting.setObjectName("frame_ContainSoundMessageSetting")
        self.label_tuDongPhatTinNhanThoai = QtWidgets.QLabel(self.frame_ContainSoundMessageSetting)
        self.label_tuDongPhatTinNhanThoai.setGeometry(QtCore.QRect(10, 12, 397, 19))
        self.label_tuDongPhatTinNhanThoai.setMouseTracking(True)
        self.label_tuDongPhatTinNhanThoai.setAccessibleDescription("")
        self.label_tuDongPhatTinNhanThoai.setStyleSheet("font: 75 bold 12pt \"Ubuntu\";")
        self.label_tuDongPhatTinNhanThoai.setObjectName("label_tuDongPhatTinNhanThoai")
        self.comboBox_forChoseYesOrNoPlaySoundMessage = QtWidgets.QComboBox(self.frame_ContainSoundMessageSetting)
        self.comboBox_forChoseYesOrNoPlaySoundMessage.setGeometry(QtCore.QRect(10, 64, 161, 31))
        self.comboBox_forChoseYesOrNoPlaySoundMessage.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);")
        self.comboBox_forChoseYesOrNoPlaySoundMessage.setObjectName("comboBox_forChoseYesOrNoPlaySoundMessage")
        self.label_ctTudongPhatvv = QtWidgets.QLabel(self.frame_ContainSoundMessageSetting)
        self.label_ctTudongPhatvv.setGeometry(QtCore.QRect(10, 34, 391, 21))
        self.label_ctTudongPhatvv.setMouseTracking(True)
        self.label_ctTudongPhatvv.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 25 10pt \"Ubuntu\";")
        self.label_ctTudongPhatvv.setWordWrap(True)
        self.label_ctTudongPhatvv.setObjectName("label_ctTudongPhatvv")
        self.label = QtWidgets.QLabel(Widget_ContainSoundSettingContent)
        self.label.setGeometry(QtCore.QRect(150, 10, 205, 41))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet("font: 75 bold 18pt \"Ubuntu\";\n"
"color: rgb(85, 85, 0);")
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.line_3.setGeometry(QtCore.QRect(20, 44, 371, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.line_4.setGeometry(QtCore.QRect(20, 138, 371, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Widget_ContainSoundSettingContent)
        self.line_5.setGeometry(QtCore.QRect(20, 256, 371, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Widget_ContainSoundSettingContent)
        QtCore.QMetaObject.connectSlotsByName(Widget_ContainSoundSettingContent)

    def retranslateUi(self, Widget_ContainSoundSettingContent):
        _translate = QtCore.QCoreApplication.translate
        Widget_ContainSoundSettingContent.setWindowTitle(_translate("Widget_ContainSoundSettingContent", "Form"))
        self.label_amLuong.setText(_translate("Widget_ContainSoundSettingContent", "Âm lượng"))
        self.label_cheDoImLang.setText(_translate("Widget_ContainSoundSettingContent", "Chế độ im lặng"))
        self.label_ctKhongPhatAmvv.setText(_translate("Widget_ContainSoundSettingContent", "(Không phát bất kỳ âm thanh nào)"))
        self.label_tuDongPhatTinNhanThoai.setText(_translate("Widget_ContainSoundSettingContent", "Tự động phát tin nhắn thoại"))
        self.label_ctTudongPhatvv.setText(_translate("Widget_ContainSoundSettingContent", "(Tự động phát tin nhắn thoại khi nhận được )"))
        self.label.setText(_translate("Widget_ContainSoundSettingContent", "ÂM THANH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget_ContainSoundSettingContent = QtWidgets.QWidget()
    ui = Ui_Widget_ContainSoundSettingContent()
    ui.setupUi(Widget_ContainSoundSettingContent)
    Widget_ContainSoundSettingContent.show()
    sys.exit(app.exec_())
