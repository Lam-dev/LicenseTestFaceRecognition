from PyQt5                  import QtCore, QtGui, QtWidgets
from PyQt5                  import QtCore, QtGui, QtWidgets
from PyQt5.QtGui            import QIcon, QPixmap
from PyQt5.QtCore           import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty
from SettingScreen.SettingScreenUI    import Ui_frame_settingScreen
from SettingScreen.ScreenSettingContent   import ScreenSettingContent
from SettingScreen.SystemSettingContent   import SystemSettingContent
from SettingScreen.SoundSettingContent    import SoundSettingContent
from KeyBoard               import KeyBoard

class SettingScreen(Ui_frame_settingScreen, QObject):
    RequestOpenDatabaseScreen = pyqtSignal()
    RequestOpenKeyBoard = pyqtSignal(object)
    SignalModifyFRthreshold = pyqtSignal(float)
    SignalModifyFaceMark = pyqtSignal(bool)
    SignalModifyImageQuality = pyqtSignal(int)
    SignalConnectNewServer = pyqtSignal(dict)
    SignalConnectNewFTPserver = pyqtSignal(dict)
    
    def __init__(self, Frame):
        
        Ui_frame_settingScreen.__init__(self)
        QObject.__init__(self)
        Ui_frame_settingScreen.setupUi(self,Frame)
        Frame.setGeometry((800-Frame.width())/2, (480-Frame.height())/2, Frame.width(), Frame.height())
        self.boldFont=QtGui.QFont()
        self.boldFont.setBold(True)
        self.noBoldFont = QtGui.QFont()
        self.noBoldFont.setBold(False)
        self.ScrollArea = MyScrollArea(self.frame_containSettingContent)
        self.ScrollArea.setGeometry(0, 0, 440, 440)
        self.frameContainSettingScreen  = Frame
        self.keyboardIsShow = False

        self.pixmapConnected = QtGui.QPixmap("icon/iconConnected.png")
        self.pixmapWaitForConnect = QtGui.QPixmap("icon/iconWaitForConnect.png")

        self.lb_textScreenSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textScreenSetting)
        self.lb_iconScreenSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textScreenSetting)
        self.lb_textSoundSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSoundSetting)
        self.lb_iconSoundSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSoundSetting)
        self.lb_textSystemSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSystemSetting)
        self.lb_iconSystemSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSystemSetting)
        # self.lb_textSecuritySetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSecuritySetting)
        # self.lb_iconSecuritySetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textSecuritySetting)
        self.lb_iconDatabaseSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textDatabaseSetting)
        self.lb_textDatabaseSetting.enterEvent = lambda event: self.MouseEnterItems(self.lb_textDatabaseSetting)
        
        self.lb_textScreenSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textScreenSetting)
        self.lb_iconScreenSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textScreenSetting)
        self.lb_textSoundSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSoundSetting)
        self.lb_iconSoundSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSoundSetting)
        self.lb_textSystemSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSystemSetting)
        self.lb_iconSystemSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSystemSetting)
        # self.lb_textSecuritySetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSecuritySetting)
        # self.lb_iconSecuritySetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textSecuritySetting)
        self.lb_iconDatabaseSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textDatabaseSetting)
        self.lb_textDatabaseSetting.leaveEvent = lambda event: self.MouseLeaveItems(self.lb_textDatabaseSetting)
        
        self.lb_textScreenSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(1)
        self.lb_iconScreenSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(1)
        self.lb_textSoundSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(2)
        self.lb_iconSoundSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(2)
        self.lb_textSystemSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(3)
        self.lb_iconSystemSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(3)
        # self.lb_textSecuritySetting.mousePressEvent = lambda event: self.ChooseScreenSetting(4)
        # self.lb_iconSecuritySetting.mousePressEvent = lambda event: self.ChooseScreenSetting(4)
        self.lb_iconDatabaseSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(5)
        self.lb_textDatabaseSetting.mousePressEvent = lambda event: self.ChooseScreenSetting(5)
        self.lb_iconDatabaseSetting.setPixmap(QtGui.QPixmap("icon/iconDatabase.png"))
        self.lb_iconScreenSetting.setPixmap(QtGui.QPixmap("icon/iconPicture.png"))
        # self.lb_iconSecuritySetting.setPixmap(QtGui.QPixmap("icon/iconSecurity.png"))
        self.lb_iconSoundSetting.setPixmap(QtGui.QPixmap("icon/iconSound.png"))
        self.lb_iconSystemSetting.setPixmap(QtGui.QPixmap("icon/iconSystem.png"))
        self.content = False
        self.ChooseScreenSetting(1)
        self.settingNumber = 1
    
    def ShowConnectFTPserverStatusToSettingScreen(self, statusStr, connectAvailalbe):
        if(self.settingNumber == 3):
            self.content.label_showFTPconnectStatus.setText(statusStr)
            if(connectAvailalbe):
                self.content.label_forShowIconFTPstatus.setPixmap(self.pixmapConnected)
            else:
                self.content.label_forShowIconFTPstatus.setPixmap(self.pixmapWaitForConnect)
    
    def ShowConnectStatusToSettingScreen(self, statusStr, connected):
        if(self.settingNumber == 3):
            self.content.label_showSocketConnectStatus.setText(statusStr)
            if(connected):
                self.content.label_iconSocketStatus.setPixmap(self.pixmapConnected)
            else:
                self.content.label_iconSocketStatus.setPixmap(self.pixmapWaitForConnect)

    def __OpenKeyboard(self, widgetTakeInput):
        self.RequestOpenKeyBoard.emit(widgetTakeInput)

    def __ChangedFRpoint(self, threadHold):
        self.SignalModifyFRthreshold.emit(threadHold)

    def __ChangeImageQuality(self, quality):
        self.SignalModifyImageQuality.emit(quality)

    def __ChangeImageFaceMark(self, mark):
        self.SignalModifyFaceMark.emit(mark)

    def __KeyBoardClosed(self):
        self.keyboardIsShow = False

    def MouseEnterItems(self, sender):
        sender.setFont(self.boldFont)

    def MouseLeaveItems(self, sender):
        sender.setFont(self.noBoldFont)

    def ChooseScreenSetting(self, settingNumber):
        self.settingNumber = settingNumber
        if(type(self.content) is not bool):
            self.content.SaveSetting()

        if(settingNumber == 1):
            self.lb_textScreenSetting.setFont(self.boldFont)
            self.content = ScreenSettingContent()
            widgetContent = self.content.GetWidgetContent()
            self.ScrollArea.SetContent(widgetContent)
      
        elif(settingNumber == 2):
            self.lb_textSoundSetting.setFont(self.boldFont)
            self.content = SoundSettingContent()
            widgetContent = self.content.GetWidgetContent()
            self.ScrollArea.SetContent(widgetContent)
            
        elif(settingNumber == 3):
            self.lb_textSystemSetting.setFont(self.boldFont)
            self.content = SystemSettingContent()
            self.content.GetTextFromKeyBoard.connect(self.__OpenKeyboard)
            widgetContent = self.content.GetWidgetContent()
            self.ScrollArea.SetContent(widgetContent)
            
            self.content.SignalModifyFRpoint.connect(self.__ChangedFRpoint)
            self.content.SignalModifyFaceMark.connect(self.__ChangeImageFaceMark)
            self.content.SignalModifyImageQuality.connect(self.__ChangeImageQuality)
            self.content.SignalConnectNewServer.connect(self.SignalConnectNewServer.emit)
            self.content.SignalConnectNewFTPserver.connect(self.SignalConnectNewFTPserver.emit)

            self.content.lineEdit_forInputIP.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputIP)
            self.content.lineEdit_forInputPort.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputPort)
            self.content.lineEdit_forInputAccount.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputAccount)
            self.content.lineEdit_forInputPassword.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputPassword)
            self.content.lineEdit_forInputFTPIP.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputFTPIP)
            self.content.lineEdit_forInputFTPport.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputFTPport)
            self.content.lineEdit_forInputFTPaccount.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputFTPaccount)
            self.content.lineEdit_forInputFPTpassword.mousePressEvent = lambda event:self.__OpenKeyboard(self.content.lineEdit_forInputFPTpassword)

            
            
            
            # self.ScrollArea.GetTextFromKeyBoard.connect(self.__OpenKeyboard())
      
        elif(settingNumber == 4):
            # self.lb_textSecuritySetting.setFont(self.boldFont)
            # content = SecurityContent()
            # widgetContent = content.GetWidgetContent()
            # self.ScrollArea.SetContent(widgetContent)
            pass
        else: 
            self.lb_textDatabaseSetting.setFont(self.boldFont)
            self.RequestOpenDatabaseScreen.emit()
    
class MyScrollArea(QtWidgets.QScrollArea):
    def __init__(self, frameContain):
        super().__init__(frameContain)
        self.setGeometry(0, 0, frameContain.width(), frameContain.height())
        self.preX = 0
        self.preY = 0
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def mouseMoveEvent(self, e):
        # self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (e.x()-self.preX))
        self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (e.y()-self.preY))
        # self.preX = e.x()
        self.preY = e.y()

    def mousePressEvent(self, e):
        # self.preX = e.x()
        self.preY = e.y()

    def SetContent(self, content):
        self.setWidget(content)
        self.setWidgetResizable(False)
        self.setGeometry(0, 0, 421, 421)

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frame_settingScreen = QtWidgets.QFrame()
    ui = SettingScreen(frame_settingScreen)
    frame_settingScreen.show()
    sys.exit(app.exec_())