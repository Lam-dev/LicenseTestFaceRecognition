import ftplib
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
import  os
import shutil
from    GetSettingFromJSON    import GetSetting
# ftp = ftplib.FTP("192.168.1.46")
# ftp.login("etm", "1")
# file = []


# def getFile(ftp, filename):
#     try:
#         x = ftp.retrbinary("RETR " + filename ,open(""+filename, 'wb').write)
#         print(x)
#     except:
#         print ("Error")

# data = []
# ftp.cwd('/files/raspi_3g/')         # change directory to /pub/
# # getFile(ftp, "TTDD_29A-999999_2019-11-05_16-47-05.json")
# files = ftp.nlst()
# for f in files:
#     print(f)

# files = ftp.nlst()
# for f in files:
#     print(f)
SETTING_DICT                                        = GetSetting.LoadSettingFromFile()
FTP_IP       =  SETTING_DICT["ftpIP"]
FTP_PORT     =  SETTING_DICT["ftpPort"]
FTP_ACCOUNT  =  SETTING_DICT["ftpAccount"]
FTP_PASSWORD =  SETTING_DICT["ftpPassword"]
LOCAL_PATH_CONTAIN_DATA_UPDATE = "DataUpdate/"

class FTPclient(QObject):
    SignalFTPnotConnect = pyqtSignal()
    SignalFolderNotExist = pyqtSignal()
    SignalUploadFileError = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.__CreateConnect()

    def ConnectNewFTPserver(self, inforDict):
        global FTP_IP, FTP_PORT, FTP_ACCOUNT, FTP_PASSWORD
        FTP_IP = inforDict["ftpIP"]
        FTP_PORT = int(inforDict["ftpPort"])
        FTP_ACCOUNT = inforDict["ftpAccount"]
        FTP_PASSWORD  = inforDict["ftpPassword"]
        return self.__CreateConnect()

    def __CreateConnect(self):
        global FTP_IP, FTP_PORT, FTP_ACCOUNT, FTP_PASSWORD
        try:
            self.ftpObj = ftplib.FTP(FTP_IP)
            self.ftpObj.timeout = 1500
            self.ftpObj.login(FTP_ACCOUNT, FTP_PASSWORD)
            return True
        except:
            return False

    def GetListStudentImage(self, fileDir):
        for i in range(0, 3):
            try:
                self.ftpObj.cwd(fileDir)
                lstFile = self.ftpObj.nlst()
                lstImage = []
                for f in lstFile:
                    
                    if(f.__contains__("jpg")):
                        lstImage.append(f)
                self.__GetListFileFromServer(lstImage)
                return lstImage
            except NameError as e:
                print(e)
                self.__CreateConnect()
        
    def SendFileToFTPserver(self, localfile, remotefile):
        fp = open(localfile, 'rb')
        try:
            self.__CreateConnect()
            self.ftpObj.storbinary('STOR %s' % remotefile, fp, 1024)
            
        except ftplib.all_errors as e:
            # print(e)
            # print("ok")
            self.SignalUploadFileError.emit(e.__str__())
            # print("remotefile not exist error caught" + remotefile)
            # path,filename = os.path.split(remotefile)
            # print("creating directory: " + remotefile)
            # self.ftpObj.mkd(path)
            # self.SendImageToFTPserver(localfile, remotefile)
            # fp.close()
            # return

        fp.close()
                    
    def __GetListFileFromServer(self, lstFile):
        numberFileGraped = 0
        # os.removedirs(LOCAL_PATH_CONTAIN_DATA_UPDATE)
        # os.makedirs(LOCAL_PATH_CONTAIN_DATA_UPDATE)
        try:
            shutil.rmtree(LOCAL_PATH_CONTAIN_DATA_UPDATE)
        except:
            pass
        os.mkdir("DataUpdate")
        for f in lstFile:
            if(not f.__contains__(".jpg")):
                continue
            try:
                self.ftpObj.retrbinary("RETR " + f ,open(LOCAL_PATH_CONTAIN_DATA_UPDATE + f, 'wb').write)
                numberFileGraped += 1

            except Exception as e:
                print(e.args)
                pass

    

# x = FTPclient()
# x.GetListStudentImage("/files/")
# x.SendImageToFTPserver("/home/lam/AppLoadXml/aaa.jpg", "files/aaa.jpg")

    