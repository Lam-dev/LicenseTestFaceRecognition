import xml.etree.ElementTree as ET
import base64
from pgmagick import Image
from DatabaseAccess.DatabaseAccess    import  ThongTinThiSinh
from ParseXML    import ImageProcessing
from PIL         import Image
import io
import numpy
import copy
from    PyQt5.QtCore            import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from CameraAndFaceRecognition.CameraAndFaceRecognition    import GetFaceEncodingFromImage
LOCAL_PATH_CONTAIN_DATA_UPDATE                      = "DataUpdate/"
class ParseXML(QObject):

    SignalNumberParsed = pyqtSignal(int, int)
    
    def __init__(self):
        super().__init__()
    
    def ReadListStudentFromXML(self, fileName):
        tree = ET.parse(LOCAL_PATH_CONTAIN_DATA_UPDATE + fileName)
        root = tree.getroot()
        numberRecord = self.__GetNumberRecord(root)
        lstHocVien = []
        for i in range(0, numberRecord):
            try:
                self.SignalNumberParsed.emit(i, numberRecord)
                hocVien = ThongTinThiSinh()
                hocVien.ID = list(root.iter("SO_TT"))[i].text
                hocVien.SBD = list(root.iter("SO_BAO_DANH"))[i].text
                hocVien.HoVaTen = list(root.iter("HO_VA_TEN"))[i].text
                hocVien.NgaySinh = list(root.iter("NGAY_SINH"))[i].text
                hocVien.SoCMTND = list(root.iter("SO_CMT"))[i].text
                hocVien.MaDK = list(root.iter("MA_DK"))[i].text
                # hocVien.AnhDangKy = ImageProcessing.ConvertImageInXMLToJpegData(list(root.iter("ANH_CHAN_DUNG"))[i].text)

                fp = open(LOCAL_PATH_CONTAIN_DATA_UPDATE + hocVien.MaDK + '.jpg', 'rb')
                hocVien.AnhDangKy = fp.read()

                image = Image.open(io.BytesIO(hocVien.AnhDangKy))
                image = image.convert("RGB")
                npArrayImage = numpy.array(image)
                hocVien.NhanDienKhuonMatStr = GetFaceEncodingFromImage().GetFaceEncodingStr(npArrayImage)
                # if(i == 1):
                    
                #     for j in range(0, 3000):
                #         hocVienx = copy.copy(hocVien)
                #         hocVienx.ID = 50 + j
                #         lstHocVien.append(hocVienx)
                # else:
                lstHocVien.append(hocVien)
                del hocVien
            except:
                pass
        return lstHocVien
    
    def __GetNumberRecord(self, root):
        try:
            a = root.getchildren()
            for child in a:
                if(child.tag == "HEADER"):
                    lstChild = child.getchildren()
                    for child1 in lstChild:
                        if(child1.tag == "TONG_SO_BAN_GHI"):
                            return int(child1.text)

        except:
            return False
