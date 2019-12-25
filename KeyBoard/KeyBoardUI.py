# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BanPhimUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContainKeyBoard(object):
    def setupUi(self, ContainKeyBoard):
        ContainKeyBoard.setObjectName("ContainKeyBoard")
        ContainKeyBoard.resize(800, 272)
        ContainKeyBoard.setStyleSheet("background-color: rgb(255, 242, 210);")
        ContainKeyBoard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ContainKeyBoard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pushButto_ctr = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButto_ctr.setGeometry(QtCore.QRect(8, 218, 61, 51))
        self.pushButto_ctr.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButto_ctr.setObjectName("pushButto_ctr")
        self.pushButton_chooseLanguge = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_chooseLanguge.setGeometry(QtCore.QRect(74, 218, 63, 51))
        self.pushButton_chooseLanguge.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_chooseLanguge.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../iconVietNamese.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_chooseLanguge.setIcon(icon)
        self.pushButton_chooseLanguge.setIconSize(QtCore.QSize(50, 32))
        self.pushButton_chooseLanguge.setObjectName("pushButton_chooseLanguge")
        self.pushButton_space = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_space.setGeometry(QtCore.QRect(204, 218, 391, 51))
        self.pushButton_space.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_space.setObjectName("pushButton_space")
        self.pushButton_close = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_close.setGeometry(QtCore.QRect(666, 218, 127, 51))
        self.pushButton_close.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_shift = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_shift.setGeometry(QtCore.QRect(8, 164, 99, 51))
        self.pushButton_shift.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_shift.setObjectName("pushButton_shift")
        self.pushButton_z = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_z.setGeometry(QtCore.QRect(114, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_z.setFont(font)
        self.pushButton_z.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_z.setObjectName("pushButton_z")
        self.pushButton_x = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_x.setGeometry(QtCore.QRect(176, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_x.setFont(font)
        self.pushButton_x.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_x.setObjectName("pushButton_x")
        self.pushButton_v = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_v.setGeometry(QtCore.QRect(298, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_v.setFont(font)
        self.pushButton_v.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_v.setObjectName("pushButton_v")
        self.pushButton_c = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_c.setGeometry(QtCore.QRect(236, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_m = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_m.setGeometry(QtCore.QRect(482, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_m.setObjectName("pushButton_m")
        self.pushButton_n = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_n.setGeometry(QtCore.QRect(422, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_n.setFont(font)
        self.pushButton_n.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_n.setObjectName("pushButton_n")
        self.pushButton_b = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_b.setGeometry(QtCore.QRect(360, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_b.setFont(font)
        self.pushButton_b.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_b.setObjectName("pushButton_b")
        self.pushButton_ = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_.setGeometry(QtCore.QRect(544, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_.setFont(font)
        self.pushButton_.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_.setObjectName("pushButton_")
        self.pushButton_h = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_h.setGeometry(QtCore.QRect(386, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_h.setFont(font)
        self.pushButton_h.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_h.setObjectName("pushButton_h")
        self.pushButton_d = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_d.setGeometry(QtCore.QRect(200, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_d.setFont(font)
        self.pushButton_d.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_d.setObjectName("pushButton_d")
        self.pushButton_g = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_g.setGeometry(QtCore.QRect(324, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_g.setFont(font)
        self.pushButton_g.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_g.setObjectName("pushButton_g")
        self.pushButton_k = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_k.setGeometry(QtCore.QRect(508, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_k.setFont(font)
        self.pushButton_k.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_k.setObjectName("pushButton_k")
        self.pushButton_a = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_a.setGeometry(QtCore.QRect(78, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_a.setFont(font)
        self.pushButton_a.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_a.setObjectName("pushButton_a")
        self.pushButton_s = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_s.setGeometry(QtCore.QRect(140, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_s.setFont(font)
        self.pushButton_s.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_s.setObjectName("pushButton_s")
        self.pushButton_f = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_f.setGeometry(QtCore.QRect(262, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_f.setFont(font)
        self.pushButton_f.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_f.setObjectName("pushButton_f")
        self.pushButton_j = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_j.setGeometry(QtCore.QRect(446, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_j.setFont(font)
        self.pushButton_j.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_j.setObjectName("pushButton_j")
        self.pushButton_l = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_l.setGeometry(QtCore.QRect(570, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_l.setFont(font)
        self.pushButton_l.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_l.setObjectName("pushButton_l")
        self.pushButton_u = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_u.setGeometry(QtCore.QRect(402, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_u.setFont(font)
        self.pushButton_u.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_u.setObjectName("pushButton_u")
        self.pushButton_i = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_i.setGeometry(QtCore.QRect(464, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_i.setFont(font)
        self.pushButton_i.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_i.setObjectName("pushButton_i")
        self.pushButton_w = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_w.setGeometry(QtCore.QRect(96, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_w.setFont(font)
        self.pushButton_w.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_w.setObjectName("pushButton_w")
        self.pushButton_r = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_r.setGeometry(QtCore.QRect(218, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_r.setFont(font)
        self.pushButton_r.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_r.setObjectName("pushButton_r")
        self.pushButton_y = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_y.setGeometry(QtCore.QRect(342, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_y.setFont(font)
        self.pushButton_y.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_y.setObjectName("pushButton_y")
        self.pushButton_q = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_q.setGeometry(QtCore.QRect(34, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_q.setFont(font)
        self.pushButton_q.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_q.setObjectName("pushButton_q")
        self.pushButton_e = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_e.setGeometry(QtCore.QRect(156, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_e.setFont(font)
        self.pushButton_e.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_e.setObjectName("pushButton_e")
        self.pushButton_o = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_o.setGeometry(QtCore.QRect(526, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_o.setFont(font)
        self.pushButton_o.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_o.setObjectName("pushButton_o")
        self.pushButton_t = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_t.setGeometry(QtCore.QRect(280, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_t.setFont(font)
        self.pushButton_t.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_t.setObjectName("pushButton_t")
        self.pushButton_cap = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_cap.setGeometry(QtCore.QRect(8, 110, 65, 51))
        self.pushButton_cap.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_cap.setObjectName("pushButton_cap")
        self.pushButton_p = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_p.setGeometry(QtCore.QRect(588, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_p.setFont(font)
        self.pushButton_p.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_p.setObjectName("pushButton_p")
        self.pushButton_dot = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_dot.setGeometry(QtCore.QRect(606, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_enter1 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_enter1.setGeometry(QtCore.QRect(692, 110, 101, 51))
        self.pushButton_enter1.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"border-bottom-right-radius:0px\n"
"")
        self.pushButton_enter1.setObjectName("pushButton_enter1")
        self.pushButton_enter2 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_enter2.setGeometry(QtCore.QRect(734, 158, 59, 57))
        self.pushButton_enter2.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"border-top-width:0px;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px\n"
"\n"
"")
        self.pushButton_enter2.setText("")
        self.pushButton_enter2.setObjectName("pushButton_enter2")
        self.pushButto = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButto.setGeometry(QtCore.QRect(632, 110, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButto.setFont(font)
        self.pushButto.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButto.setText("")
        self.pushButto.setObjectName("pushButto")
        self.pushButton_doubleDot = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_doubleDot.setGeometry(QtCore.QRect(670, 164, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_doubleDot.setFont(font)
        self.pushButton_doubleDot.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_doubleDot.setObjectName("pushButton_doubleDot")
        self.pushButton_number = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_number.setGeometry(QtCore.QRect(602, 218, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_number.setFont(font)
        self.pushButton_number.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_number.setObjectName("pushButton_number")
        self.pushButton_backSpace = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_backSpace.setGeometry(QtCore.QRect(630, 2, 165, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_backSpace.setFont(font)
        self.pushButton_backSpace.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_backSpace.setObjectName("pushButton_backSpace")
        self.pushButton_multiCharac = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_multiCharac.setGeometry(QtCore.QRect(142, 218, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_multiCharac.setFont(font)
        self.pushButton_multiCharac.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_multiCharac.setObjectName("pushButton_multiCharac")
        self.pushButton_0 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_0.setGeometry(QtCore.QRect(568, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_8 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_8.setGeometry(QtCore.QRect(444, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_7.setGeometry(QtCore.QRect(382, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_1 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_1.setGeometry(QtCore.QRect(14, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_4 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_4.setGeometry(QtCore.QRect(198, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_2.setGeometry(QtCore.QRect(76, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_6.setGeometry(QtCore.QRect(322, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_9.setGeometry(QtCore.QRect(506, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_3 = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_3.setGeometry(QtCore.QRect(136, 2, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_acong = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_acong.setGeometry(QtCore.QRect(708, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_acong.setFont(font)
        self.pushButton_acong.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_acong.setObjectName("pushButton_acong")
        self.pushButton_xo = QtWidgets.QPushButton(ContainKeyBoard)
        self.pushButton_xo.setGeometry(QtCore.QRect(648, 56, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_xo.setFont(font)
        self.pushButton_xo.setStyleSheet("margin: 1px; padding: 7px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgba(0,190,255,255);\n"
"border-style: solid;\n"
"border-radius: 3px;\n"
"border-width: 1px;\n"
"border-color: rgba(0,140,255,255);\n"
"")
        self.pushButton_xo.setObjectName("pushButton_xo")

        self.retranslateUi(ContainKeyBoard)
        QtCore.QMetaObject.connectSlotsByName(ContainKeyBoard)

    def retranslateUi(self, ContainKeyBoard):
        _translate = QtCore.QCoreApplication.translate
        ContainKeyBoard.setWindowTitle(_translate("ContainKeyBoard", "Frame"))
        self.pushButto_ctr.setText(_translate("ContainKeyBoard", "CTR"))
        self.pushButton_space.setText(_translate("ContainKeyBoard", "Space"))
        self.pushButton_close.setText(_translate("ContainKeyBoard", "Close"))
        self.pushButton_shift.setText(_translate("ContainKeyBoard", "SHIFT"))
        self.pushButton_z.setText(_translate("ContainKeyBoard", "Z"))
        self.pushButton_x.setText(_translate("ContainKeyBoard", "X"))
        self.pushButton_v.setText(_translate("ContainKeyBoard", "V"))
        self.pushButton_c.setText(_translate("ContainKeyBoard", "C"))
        self.pushButton_m.setText(_translate("ContainKeyBoard", "M"))
        self.pushButton_n.setText(_translate("ContainKeyBoard", "N"))
        self.pushButton_b.setText(_translate("ContainKeyBoard", "B"))
        self.pushButton_.setText(_translate("ContainKeyBoard", ","))
        self.pushButton_h.setText(_translate("ContainKeyBoard", "H"))
        self.pushButton_d.setText(_translate("ContainKeyBoard", "D"))
        self.pushButton_g.setText(_translate("ContainKeyBoard", "G"))
        self.pushButton_k.setText(_translate("ContainKeyBoard", "K"))
        self.pushButton_a.setText(_translate("ContainKeyBoard", "A"))
        self.pushButton_s.setText(_translate("ContainKeyBoard", "S"))
        self.pushButton_f.setText(_translate("ContainKeyBoard", "F"))
        self.pushButton_j.setText(_translate("ContainKeyBoard", "J"))
        self.pushButton_l.setText(_translate("ContainKeyBoard", "L"))
        self.pushButton_u.setText(_translate("ContainKeyBoard", "U"))
        self.pushButton_i.setText(_translate("ContainKeyBoard", "I"))
        self.pushButton_w.setText(_translate("ContainKeyBoard", "W"))
        self.pushButton_r.setText(_translate("ContainKeyBoard", "R"))
        self.pushButton_y.setText(_translate("ContainKeyBoard", "Y"))
        self.pushButton_q.setText(_translate("ContainKeyBoard", "Q"))
        self.pushButton_e.setText(_translate("ContainKeyBoard", "E"))
        self.pushButton_o.setText(_translate("ContainKeyBoard", "O"))
        self.pushButton_t.setText(_translate("ContainKeyBoard", "T"))
        self.pushButton_cap.setText(_translate("ContainKeyBoard", "CAP"))
        self.pushButton_p.setText(_translate("ContainKeyBoard", "P"))
        self.pushButton_dot.setText(_translate("ContainKeyBoard", "."))
        self.pushButton_enter1.setText(_translate("ContainKeyBoard", "ENTER"))
        self.pushButton_doubleDot.setText(_translate("ContainKeyBoard", ":"))
        self.pushButton_number.setText(_translate("ContainKeyBoard", "NUM"))
        self.pushButton_backSpace.setText(_translate("ContainKeyBoard", "Back Space"))
        self.pushButton_multiCharac.setText(_translate("ContainKeyBoard", "?,%..."))
        self.pushButton_0.setText(_translate("ContainKeyBoard", "0"))
        self.pushButton_8.setText(_translate("ContainKeyBoard", "8"))
        self.pushButton_7.setText(_translate("ContainKeyBoard", "7"))
        self.pushButton_5.setText(_translate("ContainKeyBoard", "5"))
        self.pushButton_1.setText(_translate("ContainKeyBoard", "1"))
        self.pushButton_4.setText(_translate("ContainKeyBoard", "4"))
        self.pushButton_2.setText(_translate("ContainKeyBoard", "2"))
        self.pushButton_6.setText(_translate("ContainKeyBoard", "6"))
        self.pushButton_9.setText(_translate("ContainKeyBoard", "9"))
        self.pushButton_3.setText(_translate("ContainKeyBoard", "3"))
        self.pushButton_acong.setText(_translate("ContainKeyBoard", "@"))
        self.pushButton_xo.setText(_translate("ContainKeyBoard", "\\"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContainKeyBoard = QtWidgets.QFrame()
    ui = Ui_ContainKeyBoard()
    ui.setupUi(ContainKeyBoard)
    ContainKeyBoard.show()
    sys.exit(app.exec_())
