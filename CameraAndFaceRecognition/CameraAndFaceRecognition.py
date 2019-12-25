import cv2
import face_recognition
import threading
from   PyQt5.QtCore     import pyqtSlot, pyqtSignal,QTimer, QDateTime,Qt, QObject
from   PyQt5.QtGui      import QPixmap,QColor
from   PyQt5            import QtCore, QtGui
import time

Camera_Number = 0
Camera_Object = cv2.VideoCapture(Camera_Number)
frame = False
FaceLocationInImage = False
NumberFrameNotFace = 0

class GetImageFromCamera(QObject):
    CanNotConnectCamera = pyqtSignal()
    PixmapFromCamera = pyqtSignal(QPixmap)
    SignalHideCamera = pyqtSignal()

    def __init__(self, frameCut = ((180, 460), (0, 480)), size = (300, 300), scale = 0.4, time = 50, labelObject = ""):
        super().__init__()
        self.cameraObj = Camera_Object
        self.frameCut = frameCut
        self.scale = scale
        self.time = time
        self.toBeReadImage = False
        self.timerReadImage = QTimer(self)
        self.timerReadImage.timeout.connect(self.__GetImageFromCamera)
        self.labelObject = labelObject
        # self.StartReadImage()

    def __ThreadReadCamera(self):
        threadReadCam = threading.Thread(target= self.__GetImageFromCamera, args=(), daemon=True)
        threadReadCam.start()

    def __GetImageFromCamera(self):
        global frame
        global FaceLocationInImage
        global NumberFrameNotFace
        # while True:
        ret, frame = self.cameraObj.read()
        if(NumberFrameNotFace == 2):
            self.SignalHideCamera.emit()
            return
        if(not ret):
            self.CanNotConnectCamera.emit()
            time.sleep(1000)
        else:
            frame = frame[self.frameCut[1][0]:self.frameCut[1][1], self.frameCut[0][0]:self.frameCut[0][1]]
            frame = cv2.resize(frame, (0, 0), fx = self.scale, fy = self.scale)
            if(type(FaceLocationInImage) is not bool):
                # for (top, right, bottom, left) in FaceLocationInImage[0]:
                top = FaceLocationInImage[0][0]
                right = FaceLocationInImage[0][1]
                bottom = FaceLocationInImage[0][2]
                left = FaceLocationInImage[0][3]
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 0), 1)
            
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                            QtGui.QImage.Format_RGB888)
            convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
            pixmap = QPixmap(convertToQtFormat)
            resizeImage = pixmap.scaled(280, 480, QtCore.Qt.KeepAspectRatio)
            # self.PixmapFromCamera.emit(resizeImage)
            # time.sleep(0.05)
            # if(not self.toBeReadImage):
            #     return
            self.labelObject.setPixmap(resizeImage)
      
    def StopReadImage(self):
        self.timerReadImage.stop()

    def StartReadImage(self):
        self.timerReadImage.start(60)
        
        # if(not self.toBeReadImage):
        #     self.toBeReadImage = True
        #     self.threadGetImageFromCamera = threading.Thread(target= self.__GetImageFromCamera, args=(), daemon=True)
        #     self.threadGetImageFromCamera.start()
        

class FaceRecognition(QObject):
    NoFace = pyqtSignal()
    StudentRecognized = pyqtSignal(object, object)
    StudentNotRecognized = pyqtSignal(object, object)
    SignalAddFaceEncoding = pyqtSignal(str, list)
    def __init__(self ,lstStudent = ""):
        self.lstStudent = lstStudent
        super().__init__()
        self.cameraObj = Camera_Object 
        self.timerForFaceRecognition = QTimer(self)
        self.timerForFaceRecognition.timeout.connect(self.__StartThreadFaceRecognize)
        self.imageDetectFace = ""
        self.FRthreshold = 0.4
        self.timerFaceTracking = QTimer(self)
        self.timerFaceTracking.timeout.connect(self.__StartThreadFaceTracking)
        self.numberFaceRecognize = 0
        self.licenseTestMode = True
        self.addFaceEncoding = False
        self.faceEncodingForAdd = []

    def SetListStudent(self, lstStudent):
        self.faceEncodingForAdd = []
        self.lstStudent = lstStudent

    def StartFaceRecognize(self):
        self.numberFaceRecognize = 0
        self.timerForFaceRecognition.start(1000)
    
    def StopFaceRecognize(self):
        self.timerForFaceRecognition.stop()
    
    def StartFaceTracking(self):
        self.timerFaceTracking.start(1000)

    def StopFaceTracking(self):
        self.timerFaceTracking.stop()

    def __StartThreadFaceTracking(self):
        threadFaceTracking = threading.Thread(target= self.FaceTracking, args= (), daemon= True)
        threadFaceTracking.start()

    def __StartThreadFaceRecognize(self):
        threadFaceRecognize = threading.Thread(target = self.FaceRecognition, args=(), daemon = True)
        threadFaceRecognize.start()


    def __DetectFaceInImage(self, image):
        faceLocInImage = face_recognition.face_locations(image)
        if(len(faceLocInImage) == 0):
            self.NoFace.emit()
            return False
        else:
            return faceLocInImage

    def FaceTracking(self):
        global frame
        global FaceLocationInImage
        global NumberFrameNotFace
        if(type(frame) is bool):
            return
        localFrame = frame
        # self.imageDetectFace = localFrame[:, :, ::-1]
        FaceLocationInImage = self.__DetectFaceInImage(localFrame)

        if(type(FaceLocationInImage) is bool):
            if(NumberFrameNotFace < 2):
                NumberFrameNotFace += 1
            return
        NumberFrameNotFace = 0
        
        # self.FaceRecognition()

    def __FaceRecognition(self, image):
        
        faceLocInImages = self.__DetectFaceInImage(image)
        if(type(faceLocInImages) is bool):
            return
        
        faceEncodings = face_recognition.face_encodings(image, faceLocInImages)
        i = 0
        for student in self.lstStudent:
            i = i + 1
            for encoding in faceEncodings:
                match = face_recognition.compare_faces(student.NhanDienKhuonMat, encoding, self.FRthreshold)
                
                if(self.licenseTestMode):
                    match.extend(face_recognition.compare_faces(student.NhanDienKhuonMatThem, encoding, self.FRthreshold))
                else:
                    self.faceEncodingForAdd.append(encoding)
                if True in match:
                    ret, jpgData = cv2.imencode(".jpg", image)
                    jpgData = jpgData.tobytes()
                    self.StudentRecognized.emit(student, jpgData)
                    return True
                
        self.numberFaceRecognize += 1
        if(self.numberFaceRecognize == 4):
            ret, jpgData = cv2.imencode(".jpg", image)
            self.numberFaceRecognize = 0
            jpgData = jpgData.tobytes()
            if(not self.licenseTestMode):
                self.SignalAddFaceEncoding.emit(self.lstStudent[0].MaDK, self.faceEncodingForAdd)
            
            self.StudentNotRecognized.emit(self.lstStudent[0], jpgData)
        
    def FaceRecognition(self):
        global frame
        localFrame = frame
        #rgb_small_frame = localFrame[:, :, ::-1]
        self.__FaceRecognition(localFrame)
            

class GetFaceEncodingFromImage():
    
    def __init__(self):
        pass
    
    def __GetFaceEncoding(self, image):
        faceLocInImages = face_recognition.face_locations(image)
        if(len(faceLocInImages) == 0):
            return False
        else:
            faceEncodings = face_recognition.face_encodings(image, faceLocInImages)
            return faceEncodings

    def GetFaceEncodingStr(self, image):
        faceEncodings = self.__GetFaceEncoding(image)
        faceEncodeStr = ",".join(str(elem) for elem in faceEncodings[0])
        return faceEncodeStr

    def GetFaceEncodingFromImageFile(self, fileName):
        try:
            image = face_recognition.load_image_file(fileName)
            faceEncodings = self.__GetFaceEncoding(image)
            if(len(faceEncodings) == 1):
                faceEncodeStr = ",".join(str(elem) for elem in faceEncodings[0])
                return faceEncodings[0], faceEncodeStr
            else:
                return False, False
        except:
            pass
    
