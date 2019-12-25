import threading
import time
import simpleaudio as sa
import wave
fileMoiTSlenXe = 'Sound/AudioFile/xinMoiTSLenXe.wav'
fileTSkhongTrungKhop = 'Sound/AudioFile/tsKhongTrungKhop.wav'
fileChucBanKetQuaCao = 'Sound/AudioFile/chucBanKetQuaCao.wav'

class Sound():

    def __init__(self):
        self.waveMoiTsLenXe = sa.WaveObject.from_wave_file(fileMoiTSlenXe)
        self.waveTSkhongTrungKhop = sa.WaveObject.from_wave_file(fileTSkhongTrungKhop)
        self.waveChucBanKetQuaCao = sa.WaveObject.from_wave_file(fileChucBanKetQuaCao)

    def __PlayTSkhongTrungKhop(self):
        playSound = self.waveTSkhongTrungKhop.play()
        playSound.wait_done()

    def __PlayMoiTSlenXe(self):
        playSound = self.waveMoiTsLenXe.play()
        playSound.wait_done()

    def __PlayChucBanKetQuaCao(self):
        playSound = self.waveChucBanKetQuaCao.play()
        playSound.wait_done()

    def ThreadPlayTSkhongTrungKhop(self):
        thread = threading.Thread(target=self.__PlayTSkhongTrungKhop, args=(), daemon=True)
        thread.start()

    def ThreadPlayMoiTSlenXe(self):
        thread = threading.Thread(target = self.__PlayMoiTSlenXe, args = (), daemon = True)
        thread.start()

    def ThreadPlayChucBanKetQuaCao(self):
        thread = threading.Thread(target = self.__PlayChucBanKetQuaCao, args = (), daemon = True)
        thread.start()