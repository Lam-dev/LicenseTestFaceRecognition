import sqlite3

duongDanTepSqlite = "DatabaseAccess/Database"

class LayDuLieuTrongDataBase:
    def __init__(self, duongDanDataBase, tenBang):
        #self.duongDanDataBase = duongDanDataBase; 
        # print("aaa", duongDanDataBase)
        self.CSDL = sqlite3.connect(duongDanDataBase)

        self.tenBang = tenBang

    """
    lay danh sach du lieu
    """
    def capNhatTruong(self, truongTuple, giaTriTuple, oDau):
        try:
            cursor = self.CSDL.cursor()
            sql = 'update `' + self.tenBang + '` set '
            for i in range(0,truongTuple.__len__()):
                if(i < truongTuple.__len__() - 1):
                    sql += '`%s` = "%s", ' % (truongTuple[i].__str__(), giaTriTuple[i].__str__())
                else:
                    sql += '`%s` = "%s" ' % (truongTuple[i].__str__(), giaTriTuple[i].__str__())
            sql += 'where %s' % (oDau)
            print("sql = ", sql)
            cursor.execute(sql)
            self.CSDL.commit()
        except:
            pass
    """
    Lay du lieu o mot hoac mot so truong
    """
    def LayDuLieuTaiTruong(self, truongTuple, oDau): #moi chi dung de lay du lieu (ID_Thi_Sinh, Cam_Bien_van_tay)
        cursor = self.CSDL.cursor()
        select = ""
        for i in range(0,truongTuple.__len__()):
            if(i < truongTuple.__len__() - 1):
                select += '`%s`,'%(truongTuple[i])
            else:
                select += '`%s`'%(truongTuple[0])
        sql = 'SELECT %s FROM `%s` WHERE %s' %(select, self.tenBang, oDau)   
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    """
    Lay danh sach hoc vien
    """
    def layDanhSach(self, where):
        cursor = self.CSDL.cursor()
        sql = 'SELECT  * FROM `'+ self.tenBang + '` WHERE ' + where
        cursor.execute(sql)
        results = cursor.fetchall()
        if(self.tenBang == "ThongTinThiSinh"):
            listThiSinh = []
            for i in range(0, len(results)):
                thiSinh = ThongTinThiSinh()
                thiSinh.ID = results[i][0]
                thiSinh.IDKhoaHoc = results[i][1]
                thiSinh.SBD = results[i][2]
                thiSinh.HoVaTen = results[i][3]
                thiSinh.NgaySinh = results[i][4]
                thiSinh.SoCMTND = results[i][5]
                thiSinh.NgayDangKy = results[i][6]
                thiSinh.AnhDangKy = results[i][7]
                
                lstDSdacTrung = results[i][8].split(';')
                for k in range (0, len(lstDSdacTrung)):
                    lstDacTrung = lstDSdacTrung[k].split(',')
                    thiSinh.NhanDienKhuonMat.append([])
                    if(len(lstDacTrung) == 128):
                        for j in range (0,128):
                            thiSinh.NhanDienKhuonMat[k].append(j)
                            thiSinh.NhanDienKhuonMat[k][j] =  float(lstDacTrung[j])
                if(results[i][11] != None):
                    lstDSdacTrung = results[i][11].split(';')
                    for k in range (0, len(lstDSdacTrung)):
                        lstDacTrung = lstDSdacTrung[k].split(',')
                        thiSinh.NhanDienKhuonMatThem.append([])
                        if(len(lstDacTrung) == 128):
                            for j in range (0,128):
                                thiSinh.NhanDienKhuonMatThem[k].append(j)
                                thiSinh.NhanDienKhuonMatThem[k][j] =  float(lstDacTrung[j])

                thiSinh.MaDK = results[i][10]
                listThiSinh.append(thiSinh)
                del thiSinh   
            return listThiSinh

        if(self.tenBang == "LichSuDiemDanh"):
            lstLichSu = []
            for i in range(0, len(results)):
                lichSu = ThongTinLichSuDiemDanh()
                lichSu.IDThiSinh = results[i][0]
                lichSu.ThoiGian = results[i][1]
                lichSu.Anh = results[i][2]
                lstLichSu.append(lichSu)
                del lichSu
            return lstLichSu

        if(self.tenBang == "ThongTinKhoaThi"):
            lstKhoaThi = []
            for i in range(0, len(results)):
                khoaThi = ThongTinKhoaThi()
                khoaThi.IDKhoaThi = results[i][0]
                khoaThi.NgayTao = results[i][1]
                khoaThi.TenKhoaThi = results[i][2]
                khoaThi.DuongDanLuuAnh = results[i][3]
                lstKhoaThi.append(khoaThi)
                del khoaThi
            return lstKhoaThi

    def ghiDuLieu(self, thongTin):
        try:
            cursor = self.CSDL.cursor()
            if(self.tenBang == "ThongTinThiSinh"):
                sql = 'INSERT INTO `ThongTinThiSinh`(`ID`, `IDKhoaThi`, `SBD`, `HoVaTen`, `NgaySinh`, `SoCMTND`, `NgayDangKy`, `AnhDangKy`, `NhanDienKhuonMat`, `NhanDienVanTay`, `MaDK`) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", ?, "%s", "%s", "%s")'%(thongTin.ID, thongTin.IDKhoaThi, thongTin.SBD, thongTin.HoVaTen, thongTin.NgaySinh, thongTin.SoCMTND, thongTin.NgayDangKy, thongTin.NhanDienKhuonMatStr, thongTin.NhanDienVanTay, thongTin.MaDK)
                print(cursor.execute(sql, (sqlite3.Binary(thongTin.AnhDangKy), )))
                self.CSDL.commit()

            if(self.tenBang == "LichSuDiemDanh"):
                sql = 'INSERT INTO `LichSuDiemDanh`(`IDThiSinh`, `ThoiGian`, `Anh`) VALUES ("%s", "%s", ?)'%(thongTin.IDThiSinh, thongTin.ThoiGian)
                print(cursor.execute(sql, (sqlite3.Binary(thongTin.Anh), )))
                self.CSDL.commit()

            if(self.tenBang == "ThongTinKhoaThi"):
                sql = 'INSERT INTO `ThongTinKhoaThi`(`NgayTao`, `TenKhoaThi`, `ThuMucLuuAnh`) VALUES ("%s", "%s", "%s")'%(thongTin.NgayTao, thongTin.TenKhoaThi, thongTin.DuongDanLuuAnh)
                key = cursor.execute(sql).lastrowid
                self.CSDL.commit()
                return key

        except sqlite3.Error as e:
            print(e)
    
    def xoaBanGhi(self, dieuKien):
        try:
            cursor = self.CSDL.cursor();
            if(self.tenBang == "ThongTinThiSinh"):
                sql = 'DELETE FROM `ThongTinThiSinh` WHERE %s'%(dieuKien)

            if(self.tenBang == "ThongTinKhoaThi"):
                sql = 'DELETE FROM `ThongTinKhoaThi` WHERE %s'%(dieuKien)
                
            print(cursor.execute(sql))
            self.CSDL.commit()
            cursor.close()
        except sqlite3.Error as e:
            pass

class ThiSinhRepository(LayDuLieuTrongDataBase):
    def __init__(self, duongDanTepSqlite = "DatabaseAccess/Database"): 
        super().__init__(duongDanTepSqlite, "ThongTinThiSinh")
        return

class LichSuRepository(LayDuLieuTrongDataBase):
    def __init__(self, duongDanTepSqlite = "DatabaseAccess/Database"): 
        super().__init__(duongDanTepSqlite, "LichSuDiemDanh")
        return

class KhoaThiRepository(LayDuLieuTrongDataBase):
    def __init__(self, duongDanTepSqlite = "DatabaseAccess/Database"):
        super().__init__(duongDanTepSqlite, "ThongTinKhoaThi")
        return

class ThongTinLichSuDiemDanh:
    def __init__(self):
        self.IDThiSinh = ""
        self.ThoiGian = ""
        self.Anh = ""

class ThongTinKhoaThi:
    def __init__(self):
        self.IDKhoaThi = ""
        self.NgayTao = ""
        self.TenKhoaThi = ""
        self.DuongDanLuuAnh = ""

class ThongTinThiSinh:
    def __init__(self):
        self.HoVaTen = ""
        self.SBD = "" 
        self.NgaySinh = ""
        self.SoCMTND = ""
        self.NhanDienKhuonMat = []
        self.NhanDienKhuonMatStr = ""
        self.NhanDienVanTay = ""
        self.ID = ""
        self.MaDK = ""
        self.IDKhoaThi = ""
        self.NgayDangKy = ""
        self.AnhDangKy = ""
        self.NhanDienKhuonMatThem = []

class GetDataFromDatabase():
    def __init__(self):
        pass

    def GetListStudentNewest(self):
        khoaThiRepo =   KhoaThiRepository()
        lstKhoaThi = khoaThiRepo.layDanhSach( " 1 = 1 ")
        if(lstKhoaThi == None):
            return False,False
        if(len(lstKhoaThi) == 0):
            return False,False
        khoaThiMoiNhat = lstKhoaThi[0]
        for khoaThi in lstKhoaThi:
            if(khoaThi.IDKhoaThi > khoaThiMoiNhat.IDKhoaThi):
                khoaThiMoiNhat = khoaThi

        studentRepo = ThiSinhRepository()
        lstStudent = studentRepo.layDanhSach(" IDKhoaThi = %s"%(str(khoaThiMoiNhat.IDKhoaThi)))
        return khoaThiMoiNhat, lstStudent

# x = GetDataFromDatabase()
# y = x.GetListStudent()
# pass
