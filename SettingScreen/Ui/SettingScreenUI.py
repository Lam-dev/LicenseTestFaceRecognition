# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManHinhSetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frame_settingScreen(object):
    def setupUi(self, frame_settingScreen):
        frame_settingScreen.setObjectName("frame_settingScreen")
        frame_settingScreen.resize(659, 429)
        frame_settingScreen.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 255, 235);")
        frame_settingScreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_settingScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_settingMenu = QtWidgets.QFrame(frame_settingScreen)
        self.frame_settingMenu.setGeometry(QtCore.QRect(2, -2, 209, 427))
        self.frame_settingMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_settingMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_settingMenu.setObjectName("frame_settingMenu")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_settingMenu)
        self.formLayoutWidget.setGeometry(QtCore.QRect(12, 22, 171, 347))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(14)
        self.formLayout.setObjectName("formLayout")
        self.lb_iconScreenSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_iconScreenSetting.setText("")
        self.lb_iconScreenSetting.setPixmap(QtGui.QPixmap("iconPicture.png"))
        self.lb_iconScreenSetting.setObjectName("lb_iconScreenSetting")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_iconScreenSetting)
        self.lb_textScreenSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_textScreenSetting.setObjectName("lb_textScreenSetting")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lb_textScreenSetting)
        self.lb_iconSoundSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_iconSoundSetting.setText("")
        self.lb_iconSoundSetting.setPixmap(QtGui.QPixmap("iconSound.png"))
        self.lb_iconSoundSetting.setObjectName("lb_iconSoundSetting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_iconSoundSetting)
        self.lb_textSoundSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_textSoundSetting.setObjectName("lb_textSoundSetting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lb_textSoundSetting)
        self.lb_iconSystemSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_iconSystemSetting.setText("")
        self.lb_iconSystemSetting.setPixmap(QtGui.QPixmap("iconSystem.png"))
        self.lb_iconSystemSetting.setObjectName("lb_iconSystemSetting")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_iconSystemSetting)
        self.lb_textSystemSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_textSystemSetting.setObjectName("lb_textSystemSetting")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lb_textSystemSetting)
        self.lb_iconDatabaseSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_iconDatabaseSetting.setText("")
        self.lb_iconDatabaseSetting.setPixmap(QtGui.QPixmap("iconDatabase.png"))
        self.lb_iconDatabaseSetting.setObjectName("lb_iconDatabaseSetting")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lb_iconDatabaseSetting)
        self.lb_textDatabaseSetting = QtWidgets.QLabel(self.formLayoutWidget)
        self.lb_textDatabaseSetting.setObjectName("lb_textDatabaseSetting")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lb_textDatabaseSetting)
        self.pushButton_shutdown = QtWidgets.QPushButton(self.frame_settingMenu)
        self.pushButton_shutdown.setGeometry(QtCore.QRect(12, 388, 37, 31))
        self.pushButton_shutdown.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../icon/iconShutdown.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton_shutdown.setIcon(icon)
        self.pushButton_shutdown.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_shutdown.setObjectName("pushButton_shutdown")
        self.frame_containSettingContent = QtWidgets.QFrame(frame_settingScreen)
        self.frame_containSettingContent.setGeometry(QtCore.QRect(210, 0, 447, 425))
        self.frame_containSettingContent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_containSettingContent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_containSettingContent.setObjectName("frame_containSettingContent")
        self.line = QtWidgets.QFrame(self.frame_containSettingContent)
        self.line.setGeometry(QtCore.QRect(-10, 2, 16, 415))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(frame_settingScreen)
        QtCore.QMetaObject.connectSlotsByName(frame_settingScreen)

    def retranslateUi(self, frame_settingScreen):
        _translate = QtCore.QCoreApplication.translate
        frame_settingScreen.setWindowTitle(_translate("frame_settingScreen", "Frame"))
        self.lb_textScreenSetting.setText(_translate("frame_settingScreen", "<html><head/><body><p><span style=\" font-size:12pt;\">Hiển thị</span></p></body></html>"))
        self.lb_textSoundSetting.setText(_translate("frame_settingScreen", "<html><head/><body><p><span style=\" font-size:12pt;\">Âm thanh</span></p></body></html>"))
        self.lb_textSystemSetting.setText(_translate("frame_settingScreen", "<html><head/><body><p><span style=\" font-size:12pt;\">Hệ thống</span></p></body></html>"))
        self.lb_textDatabaseSetting.setText(_translate("frame_settingScreen", "<html><head/><body><p>Cơ sở dữ liệu</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame_settingScreen = QtWidgets.QFrame()
    ui = Ui_frame_settingScreen()
    ui.setupUi(frame_settingScreen)
    frame_settingScreen.show()
    sys.exit(app.exec_())
