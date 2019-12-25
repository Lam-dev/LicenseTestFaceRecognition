import pyaudio
import wave


filename = '/home/lam/StudentRecognize/Sound/AudioFile/khongNhanDienDuoc.wav'
fileVLC = '/home/lam/StudentRecognize/Sound/AudioFile/vuiLongCho.wav'
data = b''
p = pyaudio.PyAudio()
# Set chunk size of 1024 samples per data frame
# Open the sound file 
wf = wave.open(filename, 'rb')
numFrame = wf.getnframes()
data += wf.readframes(numFrame)


wf = wave.open('/home/lam/StudentRecognize/Sound/AudioFile/NGUYỄN.wav', 'rb')
numFrame = wf.getnframes()
data += wf.readframes(numFrame)

wf = wave.open('/home/lam/StudentRecognize/Sound/AudioFile/HỒNG.wav', 'rb')
numFrame = wf.getnframes()
data += wf.readframes(numFrame)

wf = wave.open('/home/lam/StudentRecognize/Sound/AudioFile/LÂM.wav', 'rb')
numFrame = wf.getnframes()
data += wf.readframes(numFrame)





# Create an interface to PortAudio
# wf = wave.open(fileVLC, 'rb')
# numFrame = wf.getnframes()
# data += wf.readframes(numFrame)

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks

stream.write(data)


# Play the sound by writing the audio data to the stream
# while data != '':
#     stream.write(data)
#     data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()
