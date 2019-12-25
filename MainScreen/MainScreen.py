from        MainScreen.MainScreenUi    import Ui_Frame_MainScreen
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5.QtGui     import QPixmap
from        PyQt5           import QtWidgets, QtGui, QtCore
from        PIL             import Image, ImageQt
import      io
from    UpdateScreen.UpdateScreen  import UpdateScreen
from    Outdoor.OutDoor          import OutDoor
from    SettingScreen.SettingScreen   import SettingScreen
from    KeyBoard.KeyBoard             import KeyBoard

class MainScreen(QObject, Ui_Frame_MainScreen):
    SignalGoToDesktop = pyqtSignal()
    SignalModifyFRthreshold = pyqtSignal(float)
    SignalModifyFaceMark = pyqtSignal(bool)
    SignalModifyImageQuality = pyqtSignal(int)
    SignalUpdateDatabaseFinish = pyqtSignal(str, str, str)
    SignalConnectNewFTPserver = pyqtSignal(dict)
    SignalConnectNewServer = pyqtSignal(dict)


    def __init__(self, MainWindow):
        QObject.__init__(self)
        Ui_Frame_MainScreen.__init__(self)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 800, 480))

        self.centralFrame = QtWidgets.QFrame(self.centralWidget)
        self.__keyBoardOpened = False
        self.setupUi(self.centralFrame)
        # self.label_logoEcotek.setPixmap(QtGui.QPixmap("icon/logo_.png"))
        self.pixmapNoCamera = QtGui.QPixmap("icon/noCamera.png")
        self.pixmapEyeIcon = QtGui.QPixmap("icon/iconEye.png")
        self.pixmapOkIcon = QtGui.QPixmap("icon/iconOk.png")
        self.pixmapFailIcon = QtGui.QPixmap("icon/iconFail.png")
        self.pixmapWarningIcon = QtGui.QPixmap("icon/iconWarning.png")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/iconShutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_shutdown.setIcon(icon)
        self.label_7.setPixmap(QtGui.QPixmap("icon/iconEcotek.png"))
        self.label_regisImage.setPixmap(QtGui.QPixmap("icon/iconImageRepresent.png"))
        self.label_7.mouseDoubleClickEvent = lambda event: self.__OpenOutdoor()
        self.timerFlickerWarning = QTimer(self)
        self.timerFlickerWarning.timeout.connect(self.__FlickerWarning)
        self.FlagSocketConnected = False
        self.connectFTPstatus = ""
    def __OpenOutdoor(self):
        self.outdoorScreenShadow = QtWidgets.QFrame(self.centralWidget)
        self.outdoorScreenShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.outdoorScreenShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frameContainOutdoor = QtWidgets.QFrame(self.outdoorScreenShadow)
        self.outdoorObj = OutDoor(self.frameContainOutdoor)
        self.outdoorScreenShadow.raise_()
        self.outdoorScreenShadow.show()
        self.outdoorObj.SignalHideExitScreen.connect(self.__HideOutdoorScreen)
        self.outdoorObj.SignalGoToDesktop.connect(self.__GoToDesktop)

    def __GoToDesktop(self):
        self.SignalGoToDesktop.emit()
        
    def __HideOutdoorScreen(self):
        self.outdoorScreenShadow.hide()
        self.outdoorScreenShadow.deleteLater()

    def ShowNotConnect(self):
        self.label_showConnectOrDisconnect.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.FlagSocketConnected = False
        try:
            self.settingScreenObj.ShowConnectStatusToSettingScreen("Đang kết nối ...", False)
        except:
            pass
    def ShowConnected(self):
        self.FlagSocketConnected = True
        try:
            self.settingScreenObj.ShowConnectStatusToSettingScreen("Đã kết nối", True)
        except:
            pass
        self.label_showConnectOrDisconnect.setStyleSheet("background-color: rgb(0, 170, 0);")

    def ShowFTPserverConnectAvailabel(self, connectAvailable):
        try:
            if(connectAvailable):
                self.settingScreenObj.ShowConnectFTPserverStatusToSettingScreen("Máy chủ đang hoạt động", True)
            else:
                self.settingScreenObj.ShowConnectFTPserverStatusToSettingScreen("Máy chủ không hoạt động", False)
        except:
            pass
        
    def ShowCanNotConnectCamera(self):
        self.label_showCamera.setPixmap(self.pixmapNoCamera)

    def __FlickerWarning(self):
        if(self.label_textWarning.isHidden()):
            self.label_textWarning.show()
        else:
            self.label_textWarning.hide()

    def ShowStudentInfomation(self, student):
        image = Image.open(io.BytesIO(student.AnhDangKy))
        # im_data = ImageQt._toqclass_helper(image)
        # pixmap = QPixmap(im_data['im'].size[0], im_data['im'].size[1])
        # resizeImage = pixmap.scaled(150, 250, QtCore.Qt.KeepAspectRatio)
        # self.label_regisImage.setPixmap(resizeImage)
        # self.label_forShowName.setText(student.HoVaTen)
        # self.label_forShowNumberCard.setText(student.SBD)
        qim = ImageQt.ImageQt(image)
        pix = QtGui.QPixmap.fromImage(qim)
        resizePixmap = pix.scaled(150, 200, QtCore.Qt.KeepAspectRatio)
        self.SetGeometryForLabelShowRegisImage(resizePixmap.width(), resizePixmap.height())
        self.label_regisImage.setPixmap(resizePixmap)
        # self.label_forShowName.setText(student.HoVaTen.upper())
        # self.label_forShowNumberCard.setText(student.SBD)
        # self.label_forShowIdentNumber.setText(student.SoCMTND)
        

    def SetGeometryForLabelShowCamera(self, cameraWidth, cameraHeight):
        x = (self.frame_containLabelShowCamera.width() - cameraWidth)/2
        y = (self.frame_containLabelShowCamera.height() - cameraHeight)/2
        self.label_showCamera.setGeometry(x, y, cameraWidth, cameraHeight)

    def SetGeometryForLabelShowRegisImage(self, regisImageWidth, regisImageHeight):
        x = (self.frame_containLabelShowRegisImage.width() - regisImageWidth)/2
        y = (self.frame_containLabelShowRegisImage.height() - regisImageHeight)/2
        self.label_regisImage.setGeometry(x, y, regisImageWidth, regisImageHeight)

    def ShowNotStudentInformation(self):
        self.label_iconWarning.setPixmap(self.pixmapWarningIcon)
        self.label_textWarning.setStyleSheet('color: rgb(160, 160, 0);\nfont: 75 bold 14pt "Ubuntu";')
        self.label_textWarning.setText("CHƯA NHẬN ĐƯỢC THÍ SINH \n TỪ MÁY CHỦ")

    def ShowWarningLookAtCamera(self):
        self.label_iconWarning.setPixmap(self.pixmapEyeIcon)
        self.label_warningContentText.setStyleSheet('color: rgb(70, 70, 70);\nfont: 75 bold 14pt "Ubuntu";')
        self.label_warningContentText.setText("VUI LÒNG NHÌN THẲNG VÀO CAMERA")
        # self.timerFlickerWarning.start(1000)

    def ShowFaceRecognizeOK(self):
        self.label_iconWarning.setPixmap(self.pixmapOkIcon)
        self.label_warningContentText.setStyleSheet('color: rgb(0, 160, 0);\nfont: 75 bold 14pt "Ubuntu";')
        self.label_warningContentText.setText("ĐÚNG THÍ SINH \nMỜI RA XE")

    def ShowFaceRecogntizeFail(self):
        self.label_iconWarning.setPixmap(self.pixmapFailIcon)
        self.label_warningContentText.setStyleSheet('color: rgb(160, 0, 0);\nfont: 75 bold 14pt "Ubuntu";')
        self.label_warningContentText.setText("KHÔNG NHẬN DIỆN ĐƯỢC THÍ SINH")

    def ShowUpdateScreen(self, filePath):
        self.updateSettingShadow = QtWidgets.QFrame(self.centralWidget)
        self.updateSettingShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.updateSettingShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.frameUpdateScreen = QtWidgets.QFrame(self.updateSettingShadow)
        self.updateScreenObj = UpdateScreen(self.frameUpdateScreen, filePath)
        self.updateScreenObj.SignalUpdateFinish.connect(self.__UpdateFinish)
        self.updateScreenObj.SignalUpdateStopped.connect(self.__UpdateStopped)
        self.updateSettingShadow.raise_()
        self.updateSettingShadow.show()


    def __UpdateStopped(self):
        self.updateSettingShadow.hide()
        self.updateScreenObj.deleteLater()
        self.updateSettingShadow.deleteLater()

    def __UpdateFinish(self, logFile, numberSuccess, numberError):
        self.updateSettingShadow.hide()
        self.updateScreenObj.deleteLater()
        self.updateSettingShadow.deleteLater()
        self.SignalUpdateDatabaseFinish.emit(logFile, numberSuccess, numberError)
        

    def ShowSettingScreen(self):
        self.settingScreenShadow = QtWidgets.QFrame(self.centralWidget)
        self.settingScreenShadow.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.settingScreenShadow.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.settingScreenShadow.mousePressEvent = lambda event: self.__HideSettingScreen()
        self.frameContainUpdateScreen = QtWidgets.QFrame(self.settingScreenShadow)
        self.frameContainUpdateScreen.mousePressEvent = lambda event: self.__EventDontUse()
        self.settingScreenObj = SettingScreen(self.frameContainUpdateScreen)
        self.settingScreenObj.SignalModifyFaceMark.connect(self.__ModifyFaceMark)
        self.settingScreenObj.SignalModifyFRthreshold.connect(self.__ModifyFRthreadhold)
        self.settingScreenObj.SignalModifyImageQuality.connect(self.__SignalModifyImageQuality)
        self.settingScreenObj.RequestOpenKeyBoard.connect(self.__ShowKeyBoard)
        self.settingScreenObj.SignalConnectNewFTPserver.connect(self.SignalConnectNewFTPserver.emit)
        self.settingScreenObj.SignalConnectNewServer.connect(self.SignalConnectNewServer.emit)
        self.settingScreenShadow.show()
        self.settingScreenShadow.raise_()

    def __HideSettingScreen(self):
        self.settingScreenShadow.hide()
        self.settingScreenShadow.deleteLater()
        self.settingScreenObj.deleteLater()

    def __EventDontUse(self):
        pass

    def __ShowKeyBoard(self, widgetTakeInput):
        if(not self.__keyBoardOpened):
            self.frameContainKeyBoard = QtWidgets.QFrame(self.centralWidget)
            self.frameContainKeyBoard.setGeometry(0, 0, 480, 220)
            self.keyBoardObject = KeyBoard(widgetTakeInput, self.frameContainKeyBoard)
            self.keyBoardObject.CloseKeyBoardSignal.connect(self.__CloseKeyBoard)
            self.__keyBoardOpened = True

    def __CloseKeyBoard(self):
        self.frameContainKeyBoard.deleteLater()
        self.keyBoardObject.deleteLater()
        self.__keyBoardOpened = False

    def __ModifyFaceMark(self, mark):
        self.SignalModifyFaceMark.emit(mark)

    def __ModifyFRthreadhold(self, threshold):
        self.SignalModifyFRthreshold.emit(threshold)

    def __SignalModifyImageQuality(self, imageQuality):
        self.SignalModifyImageQuality.emit(imageQuality)

    def HideUpdateScreen(self):
        self.updateSettingShadow.hide()
        self.updateSettingShadow.deleteLater()

    def ShowNumberStudentParsed(self, number, all):
        self.updateScreenObj.ShowNumberUpdate(number, all)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame_MainScreen = QtWidgets.QFrame()
    ui = MainScreen(Frame_MainScreen)
    Frame_MainScreen.show()
    sys.exit(app.exec_())
