import socket
from    datetime                import datetime
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
import  threading
from    ProcessReciptData.ProcessReciptData       import ProcessReciptData
import  math
import  time
from    SocketConnect.FTPclient import FTPclient
from    GetSettingFromJSON    import GetSetting
import  json

# SERVER_IP                                           = "192.168.1.254"
# SERVER_PORT                                         = 6363

SETTING_DICT                                        = GetSetting.LoadSettingFromFile()
SERVER_IP                                           = SETTING_DICT["serverIP"]
SERVER_PORT                                         = int(SETTING_DICT["serverPort"])


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
# CLIENT_RESPONSE_UPDATE_DATA_COMPLETE              = 10
CLIENT_RESPONSE_UPDATE_RESULTS                      = 11
CLIENT_RESPONSE_UPDATE_BUSY                         = 12
CLIENT_RESPONSE_UPLOAD_IMAGE_ERROR                  = 13

MAC_ADDRESS                                         = "123456"#[0xC8, 0X93, 0X46, 0X4E,0X5D,0XD9]C8-93-46-4E-5D-D9
IMAGE_TO_SEND_SERVER_PATH                           = "/StudentRecognize/SocketConnect/"
FTP_FILE_PATH_TO_UPLOAD                             = GetSetting.GetSetting("--ServerImageDir")

class SocketClient(QObject):
    ShowStudentForConfirm = pyqtSignal(str)
    __SignalRecreateConnect = pyqtSignal()
    SignalServerNotConnect = pyqtSignal()
    SignalServerConnected = pyqtSignal()
    SignalWaitForUpdateDatabase = pyqtSignal(str)
    SignalUpdateDatabaseSuccess = pyqtSignal(list)
    SignalNumberStudentParsed = pyqtSignal(int, int)
    SignalGoToLicenseTest = pyqtSignal()
    SignalGoToGraduateTest = pyqtSignal()
    SignalResponseUpdateStatus = pyqtSignal()
    SignalServerRequestStopUpdate = pyqtSignal(bool)
    __SignalConnected = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ftpObj = FTPclient()

        self.ftpObj.SignalUploadFileError.connect(self.SendMessageUploadImageError)

        self.timerPingPong = QTimer(self)
        self.timerPingPong.timeout.connect(self.__PingPong)
        self.__SignalConnected.connect(self.__ServerConnected)
        self.processReciptDataObj = ProcessReciptData()
        self.processReciptDataObj.ShowStudentForConfirm.connect(self.__ShowStudentForConfirmSlot)
        self.processReciptDataObj.ServerConfirmedConnect.connect(self.__ServerConfirmedConnect)
        self.processReciptDataObj.ResponseRequestUpdataFromServer.connect(self.__ResponseResquestUpdateDatabaseFromServer)
        self.processReciptDataObj.SignalUpdateDataBaseSuccess.connect(self.__UpdateDataBaseSuccess)
        self.processReciptDataObj.SignalNumberStudentParsed.connect(self.__NumberStudentParsed)
        self.processReciptDataObj.SignalGoToLicenseTest.connect(self.SignalGoToLicenseTest.emit)
        self.processReciptDataObj.SignalGoToGraduateTest.connect(self.SignalGoToGraduateTest)
        self.processReciptDataObj.SignalResponseUpdateStatus.connect(self.SignalResponseUpdateStatus.emit)
        self.processReciptDataObj.SignalServerRequestStopUpdate.connect(self.SignalServerRequestStopUpdate.emit)

        self.chuaXuLy = b''

        self.FlagServerConfirmedForConnect = False
        self.FlagServerISconnect = False
        self.clientObj = ""
        self.TimerWaitForServerConfirm = QTimer(self)
        self.TimerWaitForServerConfirm.timeout.connect(self.__ThreadCreateConnect)
        self.TimerWaitForServerConfirm.start(2000)
        
        self.__TimerSendPingPong = QTimer(self)
        self.__TimerSendPingPong.timeout.connect(self.__SendPingPong)
        
        self.__SignalRecreateConnect.connect(self.__RecreateConnect)
        self.__FlagSendPingPong = True
        self.waitingForConnect = False

    def ConnectNewFTPserver(self, ftpServerInfoDict):
        pass
    def ConnectNewServer(self, serverInfoDict):
        global SERVER_IP, SERVER_PORT
        try:
            self.clientObj.shutdown(1)
        except:
            pass
        SERVER_IP = serverInfoDict["serverIP"]
        SERVER_PORT = int(serverInfoDict["serverPort"])
        self.FlagServerISconnect = False
        self.__SignalRecreateConnect.emit()

    def SendUpdateLogFile(self, logFile, ftpRemoteFile, numberSuccess, numberError):
        messageDict = {
            "TC":numberSuccess,
            "Loi":numberError
        }
        frame, checkSum = self.__DungKhungGiaoTiep(json.dumps(messageDict), 10)
        self.__SendDataViaSocket(frame)
        self.ftpObj.SendFileToFTPserver(logFile, ftpRemoteFile + logFile)
    
    def SendUpdateStatusToServer(self, numberAll, success, error):
        messageDict = {
            "Tong": numberAll,
            "DaXong":success,
            "Loi":error
        }
        frame, checkSum = self.__DungKhungGiaoTiep(json.dumps(messageDict), CLIENT_RESPONSE_UPDATE_BUSY)
        self.__SendDataViaSocket(frame)

    def SendMessageUploadImageError(self, errorString):
        dictMessage = {
            "MAC":MAC_ADDRESS,
            "ER": errorString
        }
        resultFrame, sumcheck = self.__DungKhungGiaoTiep(json.dumps(dictMessage), CLIENT_RESPONSE_UPLOAD_IMAGE_ERROR)
        self.__SendDataViaSocket(bytes(resultFrame))

    def SetFTPfilePathToUpLoad(self, filePath):
        global FTP_FILE_PATH_TO_UPLOAD
        FTP_FILE_PATH_TO_UPLOAD = filePath
    
    def __SendPingPong(self):
        if(self.__FlagSendPingPong):
            self.__PingPong()
        else:
            self.__FlagSendPingPong = True

    def __NumberStudentParsed(self, number, all):
        self.SignalNumberStudentParsed.emit(number, all)

    def __UpdateDataBaseSuccess(self, lstStudent):
        self.SignalUpdateDatabaseSuccess.emit(lstStudent)

    def __ResponseResquestUpdateDatabaseFromServer(self, remoteFilePath):
        global FTP_FILE_PATH_TO_UPLOAD
        FTP_FILE_PATH_TO_UPLOAD = remoteFilePath + "AnhNhanDien/"
        
        self.__SendDataViaSocket(self.__DungKhungGiaoTiep(remoteFilePath + ";"+ MAC_ADDRESS, CLIENT_CONFIRM_RECIPTED_IMAGE_DIRECTORY)[0])
        self.SignalWaitForUpdateDatabase.emit(remoteFilePath)

    def __RecreateConnect(self):
        self.FlagServerISconnect = False
        if(not self.TimerWaitForServerConfirm.isActive()):
            self.TimerWaitForServerConfirm.start(2000)
    
    def __SendQueueData(self):
        data = self.hangDoiGuiLenServer.ConnectAllFrame()
        try:
            if(len(data) == ""):
                self.__PingPong()
            else:
                self.__SendDataViaSocket(data)
        except:
            self.__SignalRecreateConnect.emit()
            time.sleep(0.5)

    def __SendDataViaSocket(self, data):
        try:
            self.clientObj.send(data)
            self.__FlagSendPingPong = False
        except:
            self.FlagServerISconnect
            self.__SignalRecreateConnect.emit()

    def __ShowStudentForConfirmSlot(self, maDK):
        self.ShowStudentForConfirm.emit(maDK)


    def ThreadWaitForReciptData(self):
        threadReciptData = threading.Thread(target= self.__ListenResponseFromServer, args=(), daemon= True) 
        threadReciptData.start()

    def __ListenResponseFromServer(self):
        while True:
            if(not self.FlagServerISconnect):
                continue
            try:
                recvData = self.clientObj.recv(2048)
                print(recvData)
                len(recvData)
                if(recvData == b''):
                    self.__SignalRecreateConnect.emit()
                    return
                else: 
                    lstCacKhungNhan = self.__TachCacKhungTruyen(recvData)
                    self.__FlagSendPingPong = False
                    for khung in lstCacKhungNhan:
                        self.__PhanTichKhungNhan(khung)
            except:
                self.__SignalRecreateConnect.emit()
                return
    def __PhanTichKhungNhan(self, khungNhan):
        try:
            if(not self.__CheckSumKhungTruyen(khungNhan)):
                return
        
            self.processReciptDataObj.ProcessDataFrame(khungNhan)
                    
        except:
            print("khung trong")

    def __CheckSumKhungTruyen(self, frameNhan):
        # return True ## test
        try:
            tong = 0
            for i in range (3, len(frameNhan) - 1):
                tong = tong + frameNhan[i]
            tong = -(~tong) % 256
            # print("sum = ", tong) #test
            if(tong == frameNhan[len(frameNhan)-1]):
                # print("checksum dung")
                return True
            else:
                # print("checksum sai")
                return False
        except:
            return False

    def __TachCacKhungTruyen(self, duLieu):
        if(duLieu == b''):
            return []
        self.chuaXuLy = self.chuaXuLy + duLieu
        lstKhungDL = []
        i = 0
        while True:
            if(i == len(self.chuaXuLy)):
                break
            if( self.chuaXuLy[i:i+3].__str__().__contains__("ESM")):
                try:
                    print(self.chuaXuLy[i+4])
                    print(self.chuaXuLy[i+5])
                    chieuDaiDl = self.chuaXuLy[i+4] + self.chuaXuLy[i+5] * math.pow(2, 8)
                    chieuDaiKhung = i + int(chieuDaiDl) + 7
                    if(chieuDaiKhung + i <= len(self.chuaXuLy)):
                        lstKhungDL.append(self.chuaXuLy[i:chieuDaiKhung])
                        self.chuaXuLy = self.chuaXuLy[chieuDaiKhung: len(self.chuaXuLy)]
                        i = -1
                    else:
                        self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                        break
                except NameError as e:
                    self.chuaXuLy = self.chuaXuLy[i: len(self.chuaXuLy)]
                    print(e)
                    break
            i = i + 1
        return lstKhungDL

    def __ThreadCreateConnect(self):
        if(self.waitingForConnect):
            return
        thread = threading.Thread(target=self.CreateConnect, args=(), daemon = True)
        thread.start()

    def __ServerConnected(self):
        try:
            self.FlagServerISconnect = True
            self.TimerWaitForServerConfirm.stop()
            self.ThreadWaitForReciptData()
            self.timerPingPong.start(30000)
        except:
            pass

    def CreateConnect(self):
        global SERVER_IP, SERVER_PORT
        self.waitingForConnect = True
        try:
            if(not self.FlagServerISconnect):
                self.clientObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.clientObj.connect((SERVER_IP, SERVER_PORT))
                self.clientObj.send(self.__DungKhungGiaoTiep(MAC_ADDRESS, CLIENT_REQUEST_CONNECT)[0])
                self.SignalServerConnected.emit()
                self.__SignalConnected.emit()

        except:
            self.SignalServerNotConnect.emit()
            print("khong the ket noi") #test
            self.FlagServerISconnect = False
        self.waitingForConnect = False

    def __ServerConfirmedConnect(self):
        self.FlagServerConfirmedForConnect = True
        self.TimerWaitForServerConfirm.stop()


    def __PingPong(self):
        try:
            khungTruyen, tong = self.__DungKhungGiaoTiep(datetime.now().strftime("%d//%m//%Y %H/%M/%S") + MAC_ADDRESS, 2)
            self.clientObj.sendall(khungTruyen)
        except:
            self.__SignalRecreateConnect.emit()
    
    def __DungKhungGiaoTiep(self, noiDung, malenh):
        
        if(type(noiDung) is not str): 
            return False, False
        highChieuDaiTen = int(len(noiDung) / 256)
        lowChieuDaiTen = int(len(noiDung) % 256)
        khungTruyen = [0x45, 0x53, 0x4D, malenh,lowChieuDaiTen, highChieuDaiTen]
        tong = malenh + lowChieuDaiTen + highChieuDaiTen
        j = 0
        for i in range (len(khungTruyen), len(khungTruyen) + len(noiDung)):
            khungTruyen.append('')
            khungTruyen[i] = ord(noiDung[j])
            tong = tong + ord(noiDung[j])
            j = j+ 1
            
        tong = -(~tong) % 256
        khungTruyen.append(0x00)
        khungTruyen[len(khungTruyen)-1] = tong
        return bytes(khungTruyen), tong
#region nhom ham gui thong tin cho server
    def SendResultsFaceRecognize(self, maDK ,confirmTrueOrFalse, nameOfPhotoTaked):
        self.ftpObj.SendFileToFTPserver(nameOfPhotoTaked, FTP_FILE_PATH_TO_UPLOAD + maDK + ".jpg")
        dictMessage = {
            "MAC":MAC_ADDRESS,
            "MaDK":maDK, 
            "KQ":confirmTrueOrFalse,
            "Anh": maDK + ".jpg"
        }
        resultFrame, sumcheck = self.__DungKhungGiaoTiep(json.dumps(dictMessage), FACE_RECOGNITION_RESULT)
        self.__SendDataViaSocket(bytes(resultFrame))
        

#endregion
    
class HangDoi(QObject):
    DangCho = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.queue = list()
    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            self.DangCho.emit()
            # print("hang doi  = ", self.printQueue())
            return True
        return False
        
    def remove(self, data):
        self.queue.remove(data)

    def enqueuePrioty(self, data):
        if data not in self.queue:
            self.queue.append(data)
            self.DangCho.emit()
            # print("hang doi  = ", self.printQueue())
            return True
        return False
    
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("Queue Empty!")
    
    def size(self):
        return len(self.queue)
    
    def printQueue(self):
        return self.queue
    
    def ConnectAllFrame(self):
        connectedFrame = ""
        for frame in self.queue:
            connectedFrame += frame
        return connectedFrame
    
    def ConnectAllFrameAndClear(self):
        connectedFrame = ""
        for frame in self.queue:
            connectedFrame += frame
        return 
        self.queue.clear()

