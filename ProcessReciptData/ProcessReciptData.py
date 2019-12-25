import math
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from    SocketConnect.FTPclient import FTPclient 
from    CameraAndFaceRecognition.CameraAndFaceRecognition     import GetFaceEncodingFromImage
from    DatabaseAccess.DatabaseAccess    import *
from    ParseXML.ParseXML                import ParseXML
from    GetSettingFromJSON    import GetSetting
import  json

CLIENT_REQUEST_CONNECT                              = 0
SERVER_ACCEPT_CONNECT                               = 1
PING_PONG                                           = 2
IMAGE_DIRECTORY_SERVER_SEND_TO_CLIENT               = 3
CLIENT_CONFIRM_RECIPTED_IMAGE_DIRECTORY             = 4
STUDENT_INFOMATION_TO_CONFIRM                       = 5
FACE_RECOGNITION_RESULT                             = 6
SERVER_REQUEST_CLIENT_TAKE_PICTURE                  = 7 
CLIENT_CONFIRM_TAKE_PICTURE                         = 8
SERVER_REQUEST_MODE_LICENSE_GRADUATE_TEST           = 9
CLIENT_RESPONSE_UPDATE_DATA_COMPLETE                = 10
SERVER_REQUEST_CLIENT_STOP_UPDATE                   = 11
CLIENT_RESPONSE_UPDATE_BUSY                         = 12

MAC_ADDRESS_LENGTH                                  = 8
FTP_FILE_PATH_TO_UPLOAD                             = GetSetting.GetSetting("--ServerImageDir")

class ProcessReciptData(QObject):
    ShowStudentForConfirm = pyqtSignal(str)
    ServerRequestTakePicture = pyqtSignal()
    ServerConfirmedConnect = pyqtSignal()
    ResponseRequestUpdataFromServer = pyqtSignal(str)
    SignalUpdateDataBaseSuccess = pyqtSignal(list)
    SignalNumberStudentParsed = pyqtSignal(int, int)
    SignalGoToLicenseTest = pyqtSignal()
    SignalGoToGraduateTest = pyqtSignal()
    SignalResponseUpdateStatus = pyqtSignal()
    SignalServerRequestStopUpdate = pyqtSignal(bool) #true:xoa danh sach da cap nhat, false: khong xoa danh sach da cap nhat
    
    def __init__(self):
        super().__init__()
        # self.ftpObj = FTPclient()
        self.dataUpdating = False
    def ProcessDataFrame(self, khungNhan):
        try:
            if((chr(khungNhan[0]) == 'E') & (chr(khungNhan[1]) == 'S') & (chr(khungNhan[2]) == 'M')):
                code = khungNhan[3]
                if(self.dataUpdating):
                    if(code == SERVER_REQUEST_CLIENT_STOP_UPDATE):
                        self.__ServerRequestStopUpdate(self.__CatLayPhanDataTrongFrame(khungNhan))
                    else:
                        self.SignalResponseUpdateStatus.emit()
                    return

                if(code == STUDENT_INFOMATION_TO_CONFIRM):
                    self.__ReciptedStudentInformationToConfirm(self.__CatLayPhanDataTrongFrame(khungNhan))

                elif(code == SERVER_REQUEST_CLIENT_TAKE_PICTURE):
                    self.ServerRequestTakePicture.emit()
                
                elif(code == SERVER_ACCEPT_CONNECT):
                    self.__ServerAcceptConnect(self.__CatLayPhanDataTrongFrame(khungNhan))

                elif(code == IMAGE_DIRECTORY_SERVER_SEND_TO_CLIENT):
                    
                    remoteUpdateDir = self.__CatLayPhanDataTrongFrame(khungNhan)
                    self.dataUpdating = True
                    self.ResponseRequestUpdataFromServer.emit(remoteUpdateDir)
                    
                    # self.__ServerRequestUpdateDatabase(remoteUpdateDir)
                elif(code == SERVER_REQUEST_MODE_LICENSE_GRADUATE_TEST):
                    self.__SwitchLicenseTestOrGraduateTest(self.__CatLayPhanDataTrongFrame(khungNhan))
            
    
        except:
            pass
    
    def __ServerRequestStopUpdate(self, frame):
        modeDict = json.loads(frame)
        self.dataUpdating = False
        if(modeDict['XoaDS'] == "T"):
            self.SignalServerRequestStopUpdate.emit(True)
        else:
            self.SignalServerRequestStopUpdate.emit(False)

    def __SwitchLicenseTestOrGraduateTest(self, frameMessage):
        jsonMessage = json.loads(frameMessage)
        if(jsonMessage["TSH"] == "T"):
            self.SignalGoToLicenseTest.emit()
        else:
            self.SignalGoToGraduateTest.emit()


    def __ServerAcceptConnect(self, frame):
        self.ServerConfirmedConnect.emit()
        
    def __ServerRequestUpdateDatabase(self, ftpFileDir):
#region truong hop khong doc duoc anh tu xml
        # readFaceEncodingObj = GetFaceEncodingFromImage()

        # lstImageDir = self.ftpObj.GetListStudentImage()
        # lstStudent = []
        # for imageDir in lstImageDir:
        #     if(imageDir.__contains__("/")):
        #         parts = imageDir.split("/")
        #         maDK = (parts[len(parts) - 1].split("."))[0]
        #     else:
        #         maDK = imageDir.split(".")[0]
        #     studentObj = ThongTinThiSinh()
            
        #     encoding, encodingStr = readFaceEncodingObj.GetFaceEncodingFromImageFile(image)

        #     if(type(encoding) is not bool):
        #         lstStudent.append(studentObj)
#endregion
#region Truong hop lay thong tin thi sinh tu xml
        try:
            ftpObj = FTPclient()
            lstImageAndXMLfile = ftpObj.GetListStudentImage(ftpFileDir)
            listHocVien = []
            for imageAndXml in lstImageAndXMLfile:
                if(imageAndXml.__contains__(".xml") | imageAndXml.__contains__(".XML")):
                    self.parseXMLobj = ParseXML()
                    self.parseXMLobj.SignalNumberParsed.connect(self.__NumberStudentParsed)
                    lstHocVienCongThem = self.parseXMLobj.ReadListStudentFromXML(imageAndXml)
                    for hocVien in lstHocVienCongThem:
                        listHocVien.append(hocVien)
            khoThiSinh = ThiSinhRepository()
            khoThiSinh.xoaBanGhi( " 1 = 1 ")
            for hocVien in listHocVien:
                khoThiSinh.ghiDuLieu(hocVien)
            global FTP_FILE_PATH_TO_UPLOAD
            FTP_FILE_PATH_TO_UPLOAD = remoteUpdateDir + "AnhNhanDien/"
            GetSetting.UpdateServerImageDir(FTP_FILE_PATH_TO_UPLOAD)
            self.SignalUpdateDataBaseSuccess.emit(listHocVien)

        except NameError as e:
            print(e)
            pass
# #endregion 
        # try:
        #     ftpObj = FTPclient()
        #     lstImage = ftpObj.GetListStudentImage(ftpFileDir)
        #     lstStudent = []
        #     for image in lstImage:
        #         student = ThongTinThiSinh()
        #         fp = open(LOCAL_PATH_CONTAIN_DATA_UPDATE + image + '.jpg', 'rb')
        #         hocVien.AnhDangKy = fp.read()
        #         image = Image.open(io.BytesIO(hocVien.AnhDangKy))
        #         image = image.convert("RGB")
        #         npArrayImage = numpy.array(image)
        #         hocVien.NhanDienKhuonMatStr = GetFaceEncodingFromImage().GetFaceEncodingStr(npArrayImage)

    def __NumberStudentParsed(self, number, all):
        self.SignalNumberStudentParsed.emit(number, all)

    def __ReciptedStudentInformationToConfirm(self, data):
        try:
            studentDict = json.loads(data)
            lstStudent = studentDict["DSHV"]
            self.ShowStudentForConfirm.emit(lstStudent[0]["MaDK"])
        except:
            pass
        

    def __CatLayPhanDataTrongFrame(self, frameNhan):
        chieuDaiDl = frameNhan[4] + frameNhan[5] * math.pow(2, 8)
        duLieu = []
        j = 0
        for i in range(6, int(chieuDaiDl)+6):
            duLieu.append("")
            duLieu[j] = chr(frameNhan[i])
            j += 1
            chuoiDuLieu = ''.join(duLieu)
        return chuoiDuLieu