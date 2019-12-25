from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
import xml.etree.ElementTree as ET
import base64
from pgmagick import Image
# for child in root:
#     print (child.tag, child.attrib)
def uploadListName(pointer):
    if(pointer.fileName == ''):
        return 0
    else:
        tree = ET.parse(pointer.fileName)
        root = tree.getroot()
        i = 0
        for neighbor in root.iter('HO_VA_TEN'):
            item =QtWidgets.QListWidgetItem()
            pointer.listMembers.addItem(item) 
            item = pointer.listMembers.item(i)
            item.setText(neighbor.text)
            i = i+1

def updateInformation(pointer, loc):
    if(pointer.fileName == ''):
        return 0
    else:
        tree = ET.parse(pointer.fileName)
        root = tree.getroot()
        i = 0
        for neighbor in root.iter('HO_VA_TEN'):
            if(i  == loc):
                pointer.name.setText(neighbor.text)
                print(" i = ", i)
                break
            else:
                i = i+1
        i = 0
        for neighbor in root.iter('NGAY_SINH'):
            if(i  == loc):
                pointer.dateOfBird.setText(neighbor.text)
                break
            else:
                i = i+1
        i = 0
        for neighbor in root.iter('SO_HO_SO'):
            if(i  == loc):
                pointer.numberOfFile.setText(neighbor.text)
                break
            else:
                i = i+1
        i = 0
        for neighbor in root.iter('SO_BAO_DANH'):
            if(i  == loc):
                pointer.ID.setText(neighbor.text)
                break
            else:
                i = i+1
        i = 0
        for neighbor in root.iter('SO_CMT'):
            if(i  == loc):
                pointer.ICN.setText(neighbor.text)
                break
            else:
                i = i+1
        i = 0
        for neighbor in root.iter('HANG_GPLX'):
            if(i  == loc):
                pointer.rank.setText(neighbor.text)
                break
            else:
                i = i+1   

def base64Decode(pointer, loc):
    if(pointer.fileName == ''):
        return 0
    else:
        tree = ET.parse(pointer.fileName)
        root = tree.getroot()
        i = 0
        for neighbor in root.iter('ANH_CHAN_DUNG'):
            if(i  == loc):
                temp = base64.standard_b64decode(neighbor.text)
                file = open('tam.jp2', "wb")
                file.write(temp)
                file.close()
                img = Image('tam.jp2')
                img.write('tam.jpg')
                pixmap = QPixmap('tam.jpg')
                resizeImage = pixmap.scaled(170, 300, QtCore.Qt.KeepAspectRatio)
                pointer.photoID.setPixmap(resizeImage)
                break
            else:
                i = i+1
    