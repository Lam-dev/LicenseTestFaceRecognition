import base64
from pgmagick import Image
from PyQt5.QtGui    import QPixmap

def ConvertImageInXMLToJpegData(imageString):
    binFromBase64 = base64.standard_b64decode(imageString)
    file = open('tam.jp2', "wb")
    file.write(binFromBase64)
    file.close()
    img = Image('tam.jp2')
    img.write('tam.jpg')
    file = open('tam.jpg', "rb")
    jpgData = file.read()
    return jpgData

def ConvertImageInXMLToBitmapData(imageString):
    binFromBase64 = base64.standard_b64decode(imageString)
    file = open('tam.jp2', "wb")
    file.write(binFromBase64)
    file.close()
    img = Image('tam.jp2')
    img.write('tam.jpg')
    pixmap = QPixmap('tam.jpg')
    return pixmap