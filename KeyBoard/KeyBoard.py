from KeyBoard.KeyBoardUI import Ui_ContainKeyBoard
from PyQt5.QtCore import pyqtSlot, pyqtSignal,QTimer, QDateTime, Qt, QObject, QPointF, QPropertyAnimation, pyqtProperty
from PyQt5 import QtWidgets, QtGui, QtCore
from pynput.keyboard import Key, Controller
import random

class KeyBoard(Ui_ContainKeyBoard, QObject):
    CloseKeyBoardSignal = pyqtSignal()
    def __init__(self, widgetTakeInput,frameContain):
        QObject.__init__(self)
        Ui_ContainKeyBoard.__init__(self)
        self.setupUi(frameContain)
        frameContain.setGeometry(0, 0, frameContain.width(), frameContain.height())
        self.frameContain = frameContain
        self.ShowKeyBoard()
        self.widgetTakeInput = widgetTakeInput
        self.stringEditting = self.widgetTakeInput.text()
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("icon/iconVietNamese.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        # self.pushButton_chooseLanguge.setIcon(icon)
        ##################for cursor alway focus to inputwidget#############
        self.pushButton_a.setFocusPolicy(Qt.NoFocus)
        self.pushButton_b.setFocusPolicy(Qt.NoFocus)
        self.pushButton_c.setFocusPolicy(Qt.NoFocus)
        self.pushButton_d.setFocusPolicy(Qt.NoFocus)
        self.pushButton_e.setFocusPolicy(Qt.NoFocus)
        self.pushButton_f.setFocusPolicy(Qt.NoFocus)
        self.pushButton_g.setFocusPolicy(Qt.NoFocus)
        self.pushButton_h.setFocusPolicy(Qt.NoFocus)
        self.pushButton_i.setFocusPolicy(Qt.NoFocus)
        self.pushButton_j.setFocusPolicy(Qt.NoFocus)
        self.pushButton_k.setFocusPolicy(Qt.NoFocus)
        self.pushButton_l.setFocusPolicy(Qt.NoFocus)
        self.pushButton_m.setFocusPolicy(Qt.NoFocus)
        self.pushButton_n.setFocusPolicy(Qt.NoFocus)
        self.pushButton_o.setFocusPolicy(Qt.NoFocus)
        self.pushButton_p.setFocusPolicy(Qt.NoFocus)
        self.pushButton_q.setFocusPolicy(Qt.NoFocus)
        self.pushButton_r.setFocusPolicy(Qt.NoFocus)
        self.pushButton_s.setFocusPolicy(Qt.NoFocus)
        self.pushButton_u.setFocusPolicy(Qt.NoFocus)
        self.pushButton_v.setFocusPolicy(Qt.NoFocus)

        self.pushButton_t.setFocusPolicy(Qt.NoFocus)
        self.pushButton_w.setFocusPolicy(Qt.NoFocus)
        self.pushButton_x.setFocusPolicy(Qt.NoFocus)
        self.pushButton_y.setFocusPolicy(Qt.NoFocus)
        self.pushButton_z.setFocusPolicy(Qt.NoFocus)
        self.pushButton_close.setFocusPolicy(Qt.NoFocus)
        self.pushButton_backSpace.setFocusPolicy(Qt.NoFocus)
        self.pushButton_shift.setFocusPolicy(Qt.NoFocus)
        self.pushButton_cap.setFocusPolicy(Qt.NoFocus)
        self.pushButton_space.setFocusPolicy(Qt.NoFocus)
        self.pushButton_enter1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_enter1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_chooseLanguge.setFocusPolicy(Qt.NoFocus)

        self.pushButton_dot.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_7.setFocusPolicy(Qt.NoFocus)
        self.pushButton_8.setFocusPolicy(Qt.NoFocus)
        self.pushButton_9.setFocusPolicy(Qt.NoFocus)
        self.pushButton_0.setFocusPolicy(Qt.NoFocus)
        self.pushButton_xo.setFocusPolicy(Qt.NoFocus)
        self.pushButton_acong.setFocusPolicy(Qt.NoFocus)

        ####################################################################

        self.keyboardObj = Controller()
        self.pushButton_a.clicked.connect(lambda:self.__ButtonAnphabetClick("a", self.pushButton_a))
        self.pushButton_b.clicked.connect(lambda:self.__ButtonAnphabetClick("b", self.pushButton_b))
        self.pushButton_c.clicked.connect(lambda:self.__ButtonAnphabetClick("c", self.pushButton_c))
        self.pushButton_d.clicked.connect(lambda:self.__ButtonAnphabetClick("d", self.pushButton_d))
        self.pushButton_e.clicked.connect(lambda:self.__ButtonAnphabetClick("e", self.pushButton_e))
        self.pushButton_f.clicked.connect(lambda:self.__ButtonAnphabetClick("f", self.pushButton_f))
        self.pushButton_g.clicked.connect(lambda:self.__ButtonAnphabetClick("g", self.pushButton_g))
        self.pushButton_h.clicked.connect(lambda:self.__ButtonAnphabetClick("h", self.pushButton_h))
        self.pushButton_i.clicked.connect(lambda:self.__ButtonAnphabetClick("i", self.pushButton_i))
        self.pushButton_j.clicked.connect(lambda:self.__ButtonAnphabetClick("j", self.pushButton_j))
        self.pushButton_k.clicked.connect(lambda:self.__ButtonAnphabetClick("k", self.pushButton_k))
        self.pushButton_l.clicked.connect(lambda:self.__ButtonAnphabetClick("l", self.pushButton_l))
        self.pushButton_m.clicked.connect(lambda:self.__ButtonAnphabetClick("m", self.pushButton_m))
        self.pushButton_n.clicked.connect(lambda:self.__ButtonAnphabetClick("n", self.pushButton_n))
        self.pushButton_o.clicked.connect(lambda:self.__ButtonAnphabetClick("o", self.pushButton_o))
        self.pushButton_p.clicked.connect(lambda:self.__ButtonAnphabetClick("p", self.pushButton_p))
        self.pushButton_q.clicked.connect(lambda:self.__ButtonAnphabetClick("q", self.pushButton_q))
        self.pushButton_r.clicked.connect(lambda:self.__ButtonAnphabetClick("r", self.pushButton_r))
        self.pushButton_s.clicked.connect(lambda:self.__ButtonAnphabetClick("s", self.pushButton_s))
        self.pushButton_t.clicked.connect(lambda:self.__ButtonAnphabetClick("t", self.pushButton_t))
        self.pushButton_u.clicked.connect(lambda:self.__ButtonAnphabetClick("u", self.pushButton_u))
        self.pushButton_v.clicked.connect(lambda:self.__ButtonAnphabetClick("v", self.pushButton_v))
        self.pushButton_w.clicked.connect(lambda:self.__ButtonAnphabetClick("w", self.pushButton_w))
        self.pushButton_x.clicked.connect(lambda:self.__ButtonAnphabetClick("x", self.pushButton_x))
        self.pushButton_y.clicked.connect(lambda:self.__ButtonAnphabetClick("y", self.pushButton_y))
        self.pushButton_z.clicked.connect(lambda:self.__ButtonAnphabetClick("z", self.pushButton_z))
        self.pushButton_dot.clicked.connect(lambda:self.__ButtonAnphabetClick(".", self.pushButton_dot))
        self.pushButton_1.clicked.connect(lambda:self.__ButtonAnphabetClick("1", self.pushButton_1))
        self.pushButton_2.clicked.connect(lambda:self.__ButtonAnphabetClick("2", self.pushButton_2))
        self.pushButton_3.clicked.connect(lambda:self.__ButtonAnphabetClick("3", self.pushButton_3))
        self.pushButton_4.clicked.connect(lambda:self.__ButtonAnphabetClick("4", self.pushButton_4))
        self.pushButton_5.clicked.connect(lambda:self.__ButtonAnphabetClick("5", self.pushButton_5))
        self.pushButton_6.clicked.connect(lambda:self.__ButtonAnphabetClick("6", self.pushButton_6))
        self.pushButton_7.clicked.connect(lambda:self.__ButtonAnphabetClick("7", self.pushButton_7))
        self.pushButton_8.clicked.connect(lambda:self.__ButtonAnphabetClick("8", self.pushButton_8))
        self.pushButton_9.clicked.connect(lambda:self.__ButtonAnphabetClick("9", self.pushButton_9))
        self.pushButton_0.clicked.connect(lambda:self.__ButtonAnphabetClick("0", self.pushButton_0))
        self.pushButton_xo.clicked.connect(lambda:self.__ButtonAnphabetClick('/', self.pushButton_xo))
        self.pushButton_acong.clicked.connect(lambda:self.__ButtonAnphabetClick("@", self.pushButton_acong))

        self.pushButton_close.clicked.connect(lambda:self.__ButtonControlClick("close", self.pushButton_close))
        self.pushButton_backSpace.clicked.connect(lambda:self.__ButtonControlClick("backspace", self.pushButton_backSpace))
        self.pushButton_shift.clicked.connect(lambda:self.__ButtonControlClick("shift",  self.pushButton_shift))
        self.pushButton_cap.clicked.connect(lambda:self.__ButtonControlClick("caplock", self.pushButton_cap))
        self.pushButton_space.clicked.connect(lambda:self.__ButtonControlClick("space",  self.pushButton_space))
        self.pushButton_enter1.clicked.connect(lambda:self.__ButtonControlClick("enter", self.pushButton_enter1))
        self.pushButton_enter2.clicked.connect(lambda:self.__ButtonControlClick("enter", self.pushButton_enter2))
        self.pushButton_chooseLanguge.clicked.connect(lambda:self.__ButtonControlClick("chooseLanguage", self.pushButton_chooseLanguge))
    """
    neu widget lay input bi che. Dat vi tri cua no len tren ban phim
    """
    def SetWidgetTakeInputPosAboveKeyboard(self, widgetTakeInput):

        if((self.widgetTakeInput.y() + self.widgetTakeInput.height()) > 220):
            self.oldPositon = self.widgetTakeInput.x()
            self.widgetTakeInput.setGeometry(self.widgetTakeInput.x(), (220 - self.widgetTakeInput.height() - 1), self.widgetTakeInput.width(), self.widgetTakeInput.height())


    def __ButtonAnphabetClick(self, character, button):
        if(not self.keyboardObj._caps_lock):
            self.keyboardObj.press(character)
            self.keyboardObj.release(character)
        else:
            self.keyboardObj.press(character.upper())
            self.keyboardObj.release(character.upper())
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        button.setStyleSheet("margin: 1px; padding: 7px;\nbackground-color: rgb(%s, %s, %s);\ncolor: rgba(0,190,255,255);\nborder-style: solid;\nborder-radius: 3px;\nborder-width: 1px;\nborder-color: rgba(0,140,255,255);\n"%(r, g, b)
)
        timer = QTimer(self)
        timer.timeout.connect(lambda:self.__ResetButtonStyle(button, timer))
        timer.start(500)

    def __ResetButtonStyle(self, button, timer):
        button.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        timer.stop()
        timer.deleteLater()
    def __ButtonControlClick(self, button, obj):
        if(button == "close"):
            self.CloseKeyBoard()
        if(button == "shift"):
            self.keyboardObj.press(Key.shift)
            self.keyboardObj.release(Key.shift)
        if(button == "caplock"):
            self.keyboardObj.press(Key.caps_lock)
            self.keyboardObj.release(Key.caps_lock)
        if(button == "space"):
            self.keyboardObj.press(Key.space)
            self.keyboardObj.release(Key.space)
        if(button == "enter"):
            self.keyboardObj.press(Key.enter)
            self.keyboardObj.release(Key.enter)
        if(button == "backspace"):
            self.keyboardObj.press(Key.backspace)
            self.keyboardObj.release(Key.backspace)
        if(button == "chooseLanguage"):
            self.keyboardObj.press(Key.ctrl)
            self.keyboardObj.press(Key.shift)
            self.keyboardObj.release(Key.ctrl)
            self.keyboardObj.release(Key.shift)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        obj.setStyleSheet("margin: 1px; padding: 7px;\nbackground-color: rgb(%s, %s, %s);\ncolor: rgba(0,190,255,255);\nborder-style: solid;\nborder-radius: 3px;\nborder-width: 1px;\nborder-color: rgba(0,140,255,255);\n"%(r, g, b)
)
        timer = QTimer(self)
        timer.timeout.connect(lambda:self.__ResetButtonStyle(obj, timer))
        timer.start(500)
    # def __ButtonAnphabetRelease(self, character):
    #     self.keyboardObj.release(character)


    # def __ButtonControlRelease(self, button):
    #     if(button == "close"):
    #         self.CloseKeyBoard()
    #     if(button == "shift"):
    #         self.keyboardObj.release(Key.shift)
    #     if(button == "caplock"):
    #         self.keyboardObj.release(Key.caps_lock)
    #     if(button == "space"):
    #         self.keyboardObj.release(Key.space)
    #     if(button == "enter"):
    #         self.keyboardObj.release(Key.enter)

    def ShowKeyBoard(self):
        self.frameContain.show()
        self.openAnim = QPropertyAnimation(self.frameContain, b"geometry")
        self.openAnim.setDuration(300)
        self.openAnim.setStartValue(QtCore.QRect(0 , 480 , self.frameContain.width(), self.frameContain.height()))
        self.openAnim.setEndValue(QtCore.QRect(0 , 480-self.frameContain.height(), self.frameContain.width(), self.frameContain.height()))
        self.openAnim.start()

    def CloseKeyBoard(self):
        self.CloseAnim = QPropertyAnimation(self.frameContain, b"geometry")
        self.CloseAnim.setDuration(300)
        self.CloseAnim.setEndValue(QtCore.QRect(0 , 480 , self.frameContain.width(), self.frameContain.height()))
        self.CloseAnim.setStartValue(QtCore.QRect(0 , 480-self.frameContain.height(), self.frameContain.width(), self.frameContain.height()))
        self.CloseAnim.start()
        self.CloseAnim.finished.connect(lambda:self.CloseKeyBoardSignal.emit())
        # self.frameContain.deleteLater()

    def __ChangeWidgetTakeInput(self, widgetTakeInput):
        self.widgetTakeInput = widgetTakeInput
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContainKeyBoard = QtWidgets.QFrame()
    textEdit = QtWidgets.QLineEdit(ContainKeyBoard)
    ui = KeyBoard(textEdit, ContainKeyBoard)
    ui.setupUi(ContainKeyBoard)
    ContainKeyBoard.show()
    sys.exit(app.exec_())