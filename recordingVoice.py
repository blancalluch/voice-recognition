import pyaudio
import wave
import numpy as np
import predictPrep as pp

def recording():
    
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 24000
    CHUNK = 1000
    
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")

    frames = []
    while True:
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))
        if len(frames) > (RATE/CHUNK)-1:
            toPredict = np.concatenate(frames)
            print(toPredict.shape)
            waveFile = wave.open('./audio.wav', 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()
            pp.predictData(toPredict)
            frames=[]

        
    print("finished recording")
    
    # stop Recording
    stream.stop_stream()
    stream.close()

    return None
