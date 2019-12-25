from        UpdateScreen.UpdateScreenUI    import Ui_Frame
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5.QtGui     import QPixmap
from        PyQt5           import QtWidgets, QtGui, QtCore
from        PIL             import Image, ImageQt
import      io

class UpdateScreen(QObject, Ui_Frame):
    SignalUpdateSuccess = pyqtSignal
    def __init__(self, frame):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        self.numberStudentInXMLFile = 0
        self.setupUi(frame)
        frame.setGeometry((800 - frame.width())/2, (480 - frame.height())/2, frame.width(), frame.height())
        frame.show()
    
    def ShowNumberUpdate(self, number, all):
        string = "Đã cập nhật: %s/%s thí sinh"%(str(number), str(all))
        self.label_daXuLy.setText(string)

    def UpdateSuccess(self):
        self.SignalUpdateSuccess.emit()