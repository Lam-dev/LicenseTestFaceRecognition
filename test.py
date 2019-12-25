# from  ParseXML.ParseXML   import ParseXML
# from DatabaseAccess.DatabaseAccess   import ThiSinhRepository

# x = ParseXML()
# listHocVien = x.ReadListStudentFromXML("/home/lam/AppLoadXml/K13C003VietBac.xml")
# khoThiSinh = ThiSinhRepository()
# for hocVien in listHocVien:
#     khoThiSinh.ghiDuLieu(hocVien)
import socket
import json
SERVER_IP                                           = "192.168.1.15"
SERVER_PORT                                         = 2019
def __DungKhungGiaoTiep(noiDung, malenh):
        
        if(type(noiDung) is not str): 
            return False, False
        print(len(noiDung))
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
# stopUpdateDict = {
#     "TSH":"F"
# }
hvDict = {
    "MaDK":"27012-20180828-100457",
    "HVT":"Nguyen Hong Lam"
}
lstHv = []
for i in range(0, 5):
    lstHv.append(hvDict)

dictList = {
    "DSHV":lstHv
    
}
f,s = __DungKhungGiaoTiep(json.dumps(dictList), 5)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
client.send(f)

# clientObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientObj.connect((SERVER_IP, SERVER_PORT))
# clientObj.sendall(b'aaaa')

# clientObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientObj.connect((SERVER_IP, SERVER_PORT))
# clientObj.sendall(b'aaaa')
# x = [1,2,3]
# print(x)
# x.extend([3,4,5])
# print(x)
