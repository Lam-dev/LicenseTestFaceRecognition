from        Outdoor.OutDoorUI    import Ui_Frame
from        PyQt5.QtCore    import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from        PyQt5           import QtWidgets, QtGui, QtCore
import      io

class OutDoor(QObject, Ui_Frame):
    SignalGoToDesktop = pyqtSignal()
    SignalHideExitScreen = pyqtSignal()

    def __init__(self, frame):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        self.setupUi(frame)
        frame.setGeometry((800 - frame.width())/2, (480 - frame.height())/2, frame.width(), frame.height())
        frame.show()
        self.pushButtonEnter.clicked.connect(self.__GoToDesktop)
        self.pushbutton_exit.clicked.connect(self.__HideExitScreen)

    def __GoToDesktop(self):
        if(self.lineEdit_inputNumber.text() == "210296"):
            self.SignalGoToDesktop.emit()

    def __HideExitScreen(self):
        self.SignalHideExitScreen.emit()
    
