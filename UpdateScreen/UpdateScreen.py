from        UpdateScreen.UpdateScreenUI   import Ui_FrameContainUpdateScreen
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5.QtGui     import QPixmap
from        PyQt5           import QtWidgets, QtGui, QtCore
from        PIL             import Image, ImageQt
from        SocketConnect.FTPclient       import FTPclient
from        DatabaseAccess.DatabaseAccess    import *
import      io
from        CameraAndFaceRecognition.CameraAndFaceRecognition    import GetFaceEncodingFromImage
from        datetime        import datetime
import      threading
import      numpy

class UpdateScreen(QObject, Ui_FrameContainUpdateScreen):
    __SignalCountUpNumberUpdated = pyqtSignal(str)
    __SignalShowNumberStudent = pyqtSignal(int)
    __SignalCountUpNumberError = pyqtSignal(str)
    __SignalNoStudentForUpdate = pyqtSignal()
    __SignalThreadFinish = pyqtSignal()
    SignalUpdateFinish = pyqtSignal(str, str, str)
    SignalUpdateStopped = pyqtSignal()

    def __init__(self, frame, filePath):
        QObject.__init__(self)
        Ui_FrameContainUpdateScreen.__init__(self)
        self.setupUi(frame)
        self.numberStudentError = 0
        self.numberStudent = 0
        self.numberStudentUpdated = 0
        self.stopUpdate = False
        self.label_forShowDataTime.setText(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        frame.setGeometry((800 - frame.width())/2, (480 - frame.height())/2, frame.width(), frame.height())
        frame.show()
        self.label.setPixmap(QtGui.QPixmap("icon/iconStudentUpdate.png"))
        self.__SignalCountUpNumberUpdated.connect(self.__CountUpNumberUpdated)
        self.__SignalCountUpNumberError.connect(self.__CountUpNumberStudentError)
        self.__SignalShowNumberStudent.connect(self.__ShowNumberStudent)
        self.__SignalThreadFinish.connect(self.__ThreadFinish)
        self.__ListStudentUpdateError = []
        self.__ListStudentUpdateSuccess = []
        self.__numberThreadFinished = 0
        self.__DownLoadAndUpdateData(filePath)
        
        

    def __ThreadFinish(self):
        self.__numberThreadFinished += 1
        if(self.__numberThreadFinished == 2):
            if(self.stopUpdate):
                try:
                    khoKhoaThi = KhoaThiRepository()
                    khoKhoaThi.xoaBanGhi(" IDKhoaThi = %s"%(self.IDKhoaThi))
                    khoThiSinh = ThiSinhRepository()
                    khoThiSinh.xoaBanGhi(" IDKhoaThi = %s"%(self.IDKhoaThi))
                    self.SignalUpdateStopped.emit()
                except NameError as e:
                    pass
            else:
                self.__CreateLogFile()

    def __CreateLogFile(self):
        try:
            logFile = open("log.txt","w+")
            logFile.write("Thời gian: %s \t Tên khóa thi: %s\n"%( datetime.now().strftime("%d//%m//%Y %H:%M:%S"), ""))
            allNumberStudent = str(self.__ListStudentUpdateError.__len__()+self.__ListStudentUpdateSuccess.__len__())
            numberSuccess = str(self.__ListStudentUpdateSuccess.__len__())
            numberError = str(self.__ListStudentUpdateError.__len__())
            logFile.write("Tổng số thí sinh: %s \t Cập nhật thành công: %s \t Cập nhật lỗi: %s \n"%(allNumberStudent, numberSuccess, numberError))
            logFile.write("Danh sách thí sinh lỗi: \n")
            for student in self.__ListStudentUpdateError:
                logFile.write("%s \n"%(str(student)))
            logFile.write("Danh sách thí sinh cập nhật thành công:\n")
            for student in self.__ListStudentUpdateSuccess:
                logFile.write("%s \n"%(str(student)))
            logFile.close()
            self.SignalUpdateFinish.emit("log.txt", numberSuccess, numberError)
        except:
            pass
        

    def __ShowNumberStudent(self, numberStudent):
        self.numberStudent = numberStudent
        self.label_forShowNumberStudent.setText(str(numberStudent))

    def __CountUpNumberUpdated(self, MDKstudent):
        self.numberStudentUpdated += 1
        self.__ListStudentUpdateSuccess.append(MDKstudent)
        string = "%s/%s thí sinh"%(self.numberStudentUpdated, self.numberStudent)
        self.label_forShowNumberUpdated.setText(string)

    def __CountUpNumberStudentError(self, MDKstudent):
        self.numberStudentError += 1
        self.__ListStudentUpdateError.append(MDKstudent)
        string = "%s thí sinh"%(str(self.numberStudentError))
        self.label_forShowNumberError.setText(string)

    def __CreateCourse(self, filePath):
        khoaThi = ThongTinKhoaThi()
        khoaThi.NgayTao = datetime.now().strftime("%d//%m//%Y %H/%M/%S")
        khoaThi.DuongDanLuuAnh = filePath + "AnhThiSinh/"
        khoKhoaThi = KhoaThiRepository()
        return khoKhoaThi.ghiDuLieu(khoaThi)
        
    def __DownLoadAndUpdateData(self, ftpFileDir):
        try:
            ftpObj = FTPclient()
            self.IDKhoaThi = self.__CreateCourse(ftpFileDir)
            lstImage = ftpObj.GetListStudentImage(ftpFileDir)
            numberImage = len(lstImage)
            if(numberImage == 0):
                self.__SignalNoStudentForUpdate.emit()
            # self.__SignalShowNumberStudent.emit(numberImage)
            self.__ShowNumberStudent(numberImage)
            if(numberImage == 1):
                thread1 = threading.Thread(target = self.__ProcessImage, args=(lstImage, self.IDKhoaThi, 0, numberImage))
                thread1.start()
            else:
                thread1 = threading.Thread(target = self.__ProcessImage, args=(lstImage, self.IDKhoaThi, 0, int(numberImage/2)))   
                thread2 = threading.Thread(target = self.__ProcessImage, args=(lstImage, self.IDKhoaThi, int(numberImage/2), numberImage))
                thread1.start()
                thread2.start()
        except NameError as e:
            print(e)
            pass
    
    def __ProcessImage(self, lstImage, IDKhoaThi, start, end):
            khoThiSinh = ThiSinhRepository()
            for i in range(start, end):
                if(self.stopUpdate):
                    break
                try:
                    thiSinh = ThongTinThiSinh()
                    thiSinh.MaDK = lstImage[i].split(".")[0]
                    fp = open("DataUpdate/" + lstImage[i], 'rb')
                    thiSinh.AnhDangKy = fp.read()
                    image = Image.open(io.BytesIO(thiSinh.AnhDangKy))
                    image = image.convert("RGB")
                    npArrayImage = numpy.array(image)
                    thiSinh.NhanDienKhuonMatStr = GetFaceEncodingFromImage().GetFaceEncodingStr(npArrayImage)
                    thiSinh.IDKhoaThi = IDKhoaThi
                    khoThiSinh.ghiDuLieu(thiSinh)
                    self.__SignalCountUpNumberUpdated.emit(thiSinh.MaDK)
                except:
                    self.__SignalCountUpNumberError.emit(thiSinh.MaDK)
            self.__SignalThreadFinish.emit()
    def __ServerRequestUpdateDatabase(self, ftpFileDir):
        
        try:
            ftpObj = FTPclient()
            lstImage = ftpObj.GetListStudentImage(ftpFileDir)
            self.label_forShowNumberStudent.setText(len(lstImage))
            listHocVien = []
            
            for imageName in lstImage:
                try:
                    hocVien = ThongTinThiSinh()
                    fp = open(imageName +'.jpg', 'rb')
                    hocVien.AnhDangKy = fp.read()
                    image = Image.open(io.BytesIO(hocVien.AnhDangKy))
                    image = image.convert("RGB")
                    npArrayImage = numpy.array(image)
                    hocVien.NhanDienKhuonMatStr = GetFaceEncodingFromImage().GetFaceEncodingStr(npArrayImage)
                    hocVien.IDKhoaHoc = idKhoaHoc
                    hocVien.MaDK = imageName
                    listHocVien.append(hocVien)

                except NameError as e:
                    print(imageName)
                    self.__CountUpNumberStudentError()
            khoThiSinh = ThiSinhRepository()
            for hocVien in listHocVien:
                khoThiSinh.ghiDuLieu(hocVien)

            # for imageAndXml in lstImageAndXMLfile:
            #     if(imageAndXml.__contains__(".xml") | imageAndXml.__contains__(".XML")):
            #         self.parseXMLobj = ParseXML()
            #         self.parseXMLobj.SignalNumberParsed.connect(self.__NumberStudentParsed)
            #         lstHocVienCongThem = self.parseXMLobj.ReadListStudentFromXML(imageAndXml)
            #         for hocVien in lstHocVienCongThem:
            #             listHocVien.append(hocVien)
            # khoThiSinh = ThiSinhRepository()
            # khoThiSinh.xoaBanGhi( " 1 = 1 ")
            # for hocVien in listHocVien:
            #     khoThiSinh.ghiDuLieu(hocVien)
            # global FTP_FILE_PATH_TO_UPLOAD
            # FTP_FILE_PATH_TO_UPLOAD = remoteUpdateDir + "AnhNhanDien/"
            # GetSetting.UpdateServerImageDir(FTP_FILE_PATH_TO_UPLOAD)
            # self.SignalUpdateDataBaseSuccess.emit(listHocVien)

        except NameError as e:
            print(e)
            pass
    
    
