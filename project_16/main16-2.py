from gpiozero import Button
import time
import pyaudio
import wave
import datetime

swPin = 14

button = Button(swPin)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 60

def saveVoice():
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start to record the audio.")
    
    frames = []
    
    now = datetime.datetime.now()
    fileName = now.strftime('%Y-%m-%d %H:%M:%S')
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        
    print("Recording is finished.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(fileName + '.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

button.when_pressed = saveVoice

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
