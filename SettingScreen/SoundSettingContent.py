from SettingScreen.SoundSettingScreenContentUI import Ui_Widget_ContainSoundSettingContent
from PyQt5.QtCore import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty
from PyQt5 import QtWidgets, QtGui

class SoundSettingContent(Ui_Widget_ContainSoundSettingContent, QObject):
    def __init__(self):
        QObject.__init__(self)
        Ui_Widget_ContainSoundSettingContent.__init__(self)
        self.scrollAreaContent = QtWidgets.QWidget()
        self.setupUi(self.scrollAreaContent)
        self.comboBox_ForChooseYesOrNoSilent.addItems(("Yes", "No"))
        self.comboBox_forChoseYesOrNoPlaySoundMessage.addItems(("Yes", "No"))
        self.label_iconVolume.setPixmap(QtGui.QPixmap("icon/iconVolume.png"))
        
    def GetWidgetContent(self):
        return self.scrollAreaContent
    
    def SaveSetting(self):
        pass