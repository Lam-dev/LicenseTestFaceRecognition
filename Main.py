from    CameraAndFaceRecognition.CameraAndFaceRecognition  import GetImageFromCamera, FaceRecognition
from    MainScreen.MainScreen   import MainScreen

from    DatabaseAccess.DatabaseAccess    import *
from    PyQt5                   import QtCore, QtGui, QtWidgets, Qt
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from         PyQt5              import QtCore, QtGui, QtWidgets
from         PyQt5              import QtGui
from         PyQt5              import QtWidgets
from         PyQt5.QtGui        import QPixmap,QColor
from         PyQt5.QtWidgets    import *
import       sys
from         datetime           import datetime
from         Sound.OrangePiSound  import Sound
from         SocketConnect.SocketClient   import SocketClient
import       os

# from   Sound.Sound              import Sound
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hideCameraPixmap = QtGui.QPixmap("icon/imageFaceRecognition.png")
        self.mainScreenObj = MainScreen(self)
        self.cameraObj = GetImageFromCamera(labelObject= self.mainScreenObj.label_showCamera)

        self.newestExamination, self.lstStudent = GetDataFromDatabase().GetListStudentNewest()
        
        self.faceRecognitionObj = FaceRecognition(self.lstStudent)
        self.socketObject = SocketClient() 
        if(type(self.newestExamination) is not bool):
            self.socketObject.SetFTPfilePathToUpLoad(self.newestExamination.DuongDanLuuAnh)

        self.mainScreenObj.SetGeometryForLabelShowCamera(273,381)
        # self.mainScreenObj.pushButton_shutdown.clicked.connect(lambda:os.system('sudo shutdown now'))
        self.mainScreenObj.pushButton_shutdown.clicked.connect(self.__ShowSettingScreen)
        # self.mainScreenObj.ShowNotStudentInformation()
        self.mainScreenObj.SignalGoToDesktop.connect(self.close)
        self.mainScreenObj.SignalModifyImageQuality.connect(self.__ModifyImageQuality)
        self.mainScreenObj.SignalModifyFaceMark.connect(self.__ModifyFaceMark)
        self.mainScreenObj.SignalModifyFRthreshold.connect(self.__ModifyFRthreshold)
        self.mainScreenObj.SignalUpdateDatabaseFinish.connect(self.__UpdateDatabaseFinish)
        self.mainScreenObj.SignalConnectNewServer.connect(self.socketObject.ConnectNewServer)
        self.mainScreenObj.SignalConnectNewFTPserver.connect(self.__ConnectNewFTPserver)
        self.soundObj = Sound()
#region   dieu khien signal tu camera

        self.cameraObj.PixmapFromCamera.connect(self.__ShowImageFromCamera)
        self.cameraObj.CanNotConnectCamera.connect(self.mainScreenObj.ShowCanNotConnectCamera)
        self.cameraObj.StartReadImage()
        self.cameraObj.SignalHideCamera.connect(self.__ShowImageHideCamera)

        self.faceRecognitionObj.StudentRecognized.connect(self.__RecognizedStudent)
        self.faceRecognitionObj.StudentNotRecognized.connect(self.__NotRecognized)
        self.faceRecognitionObj.SignalAddFaceEncoding.connect(self.__SaveAddedImage)
        self.faceRecognitionObj.StartFaceTracking()
        # self.faceRecognitionObj.StartFaceRecognize()
        
#endregion
#region cac cai dat
        self.settingFindOrConfirmStudent = "C" # che do tim mot hoc vien hoac xac nhan hoc vien gui xuong
#endregion
#region
        self.socketObject.ShowStudentForConfirm.connect(self.__ShowAndChooseStudentForConfirm)
        self.socketObject.SignalServerNotConnect.connect(self.ServerNotConnect)
        self.socketObject.SignalServerConnected.connect(self.ServerConnected)
        self.socketObject.SignalWaitForUpdateDatabase.connect(self.WaitForUpdateDatabase)
        self.socketObject.SignalUpdateDatabaseSuccess.connect(self.UpdateDatabaseSuccess)
        self.socketObject.SignalNumberStudentParsed.connect(self.NumberStudentParsed)
        self.socketObject.SignalGoToLicenseTest.connect(self.__GoToLicenseTest)
        self.socketObject.SignalGoToGraduateTest.connect(self.__GoToGraduateTest)
        self.socketObject.SignalResponseUpdateStatus.connect(self.__ResponseUpdateStatus)
        self.socketObject.SignalServerRequestStopUpdate.connect(self.__StopUpdate)
#endregion
        self.filePathForDownloadStudentImage = ""

    def __ConnectNewFTPserver(self, ftpServerDict):
        connectAvailabel = self.socketObject.ftpObj.ConnectNewFTPserver(ftpServerDict)
        self.mainScreenObj.ShowFTPserverConnectAvailabel(connectAvailabel)

    def __StopUpdate(self):
        try:
            self.mainScreenObj.updateScreenObj.stopUpdate = True
        except:
            pass

    def __ResponseUpdateStatus(self):
        try:
            numberSuccess = self.mainScreenObj.updateScreenObj.numberStudentUpdated
            numberError  = self.mainScreenObj.updateScreenObj.numberStudentError
            numberAll = self.mainScreenObj.updateScreenObj.numberStudent
            self.socketObject.SendUpdateStatusToServer(numberAll, numberSuccess, numberError)
        except:
            pass 

    def __GoToLicenseTest(self):
        self.faceRecognitionObj.licenseTestMode = True

    def __GoToGraduateTest(self):
        self.faceRecognitionObj.licenseTestMode = False

    def __UpdateDatabaseFinish(self, logFileName, numberSuccess, numberError):
        self.socketObject.processReciptDataObj.dataUpdating = False
        self.socketObject.SendUpdateLogFile(logFileName, self.filePathForDownloadStudentImage, numberSuccess, numberError)
        self.newestExamination, self.lstStudent = GetDataFromDatabase().GetListStudentNewest()
        if(type(self.newestExamination) is not bool):
            self.socketObject.SetFTPfilePathToUpLoad(self.newestExamination.DuongDanLuuAnh)

    def __SaveAddedImage(self, maDK,lstEncoding):
        lstFaceEncodeStr = []
        count = 0
        for encoding in lstEncoding:
            faceEncodeStr = ",".join([str(elem) for elem in encoding])
            lstFaceEncodeStr.append(faceEncodeStr)
        faceEncodesStr = ';'.join(lstFaceEncodeStr)
        khoThiSinh = ThiSinhRepository()
        khoThiSinh.capNhatTruong(("NhanDienKhuonMatDaThem", ), (faceEncodesStr, ), ' MaDK = "%s"'%(maDK))

    def __ModifyImageQuality(self, quality):
        print(quality)

    def __ModifyFaceMark(self, mark):
        print(mark)

    def __ModifyFRthreshold(self, threshold):
        self.faceRecognitionObj.FRthreshold = threshold

    def NumberStudentParsed(self, number, all):
        self.mainScreenObj.ShowNumberStudentParsed(number, all)

    def UpdateDatabaseSuccess(self, listStudents):
        self.lstStudent.clear()
        self.lstStudent.extend(listStudents)
        self.faceRecognitionObj.StartFaceRecognize()
        self.cameraObj.StartReadImage()
        self.mainScreenObj.HideUpdateScreen()

    def WaitForUpdateDatabase(self, filePath):
        self.filePathForDownloadStudentImage = filePath
        self.faceRecognitionObj.StopFaceRecognize()
        self.cameraObj.StopReadImage()
        self.mainScreenObj.ShowUpdateScreen(filePath)

    def __ShowSettingScreen(self):
        self.faceRecognitionObj.StopFaceRecognize()
        self.cameraObj.StopReadImage()
        self.faceRecognitionObj.StopFaceTracking()
        self.mainScreenObj.ShowSettingScreen()
        
    def ServerNotConnect(self):
        # self.cameraObj.StopReadImage()
        self.mainScreenObj.ShowNotConnect()

    def ServerConnected(self):
        # self.cameraObj.StartReadImage()
        self.mainScreenObj.ShowConnected()
        pass

    def __NotRecognized(self, student, jpegData):
        # self.soundObj.ThreadPlayBip__Bip()
        self.soundObj.ThreadPlayTSkhongTrungKhop()
        fp = open("imageTosend.jpg", 'wb')
        fp.write(jpegData)
        self.socketObject.SendResultsFaceRecognize(student.MaDK, "F", "imageTosend.jpg")
    
    def __ShowAndChooseStudentForConfirm(self, maDK):
        for student in self.lstStudent:
            if(student.MaDK.__str__() == maDK):
                self.mainScreenObj.ShowWarningLookAtCamera()
                self.mainScreenObj.ShowStudentInfomation(student)
                studentForConfirm = []
                studentForConfirm.append(student)
                self.faceRecognitionObj.SetListStudent(studentForConfirm)
                self.faceRecognitionObj.StartFaceRecognize()
                return
                
    def __RecognizedStudent(self, studentObj, faceImageJpgData):
        if(self.settingFindOrConfirmStudent == "C"):
            # self.soundObj.ThreadPlayBipBipBip()
            self.soundObj.ThreadPlayMoiTSlenXe()
            fp = open("imageTosend.jpg", 'wb')
            fp.write(faceImageJpgData)
            self.mainScreenObj.ShowFaceRecognizeOK()
            self.socketObject.SendResultsFaceRecognize(studentObj.MaDK, "T", "imageTosend.jpg")
            
        # self.mainScreenObj.ShowStudentInfomation(studentObj)
        # lichSu = ThongTinLichSuDiemDanh()
        # lichSu.IDThiSinh = studentObj.ID
        # lichSu.ThoiGian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # lichSu.Anh = faceImageJpgData
        # self.socketObject.GuiThongTinNguoiCheck(lichSu)
        # khoLichSu = LichSuRepository()
        # khoLichSu.ghiDuLieu(lichSu)        # self.soundObj.PlayBipBipBip()
        # print(studentObj.HoVaTen)

    def __ShowImageFromCamera(self, pixmap):
        self.mainScreenObj.label_showCamera.setPixmap(pixmap)

    def __ShowImageHideCamera(self):
        self.mainScreenObj.label_showCamera.setPixmap(self.hideCameraPixmap)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
