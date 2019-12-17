import pyaudio
import wave
import numpy as np
import predictPrep as pp

def recording(RATE,CHUNK,WAVE_OUTPUT_FILENAME,pred):
    '''recording and predicting each second recorded'''
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    WINDOW_SAMPLE = (RATE/CHUNK) / 2
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")

    frames = []
    while True:
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(np.frombuffer(data, dtype=np.int16))
        if len(frames) >= WINDOW_SAMPLE:
            toPredict = np.concatenate(frames)
            if pred:
                pp.predictData(toPredict)
                frames=[]
            if WAVE_OUTPUT_FILENAME:
                waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                waveFile.setnchannels(CHANNELS)
                waveFile.setsampwidth(audio.get_sample_size(FORMAT))
                waveFile.setframerate(RATE)
                waveFile.writeframes(b''.join(frames))
                waveFile.close()

        
    print("finished recording")
    
    # stop Recording
    stream.stop_stream()
    stream.close()

    return None
