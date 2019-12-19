import pyaudio
import wave
import numpy as np
import predictPrep as pp

def recording(RATE,CHUNK,WAVE_OUTPUT_FILENAME,pred,num_frames):
    '''recording and predicting each second recorded'''
    #rv.recording(24000,1000,0,1,40)
    #rv.recording(84000,1000,f'../input/{combo.get()}{txt1.get()+txt2.get()}.wav',0,1)

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
    f=0
    fram=[]
    res=[]
    while f<num_frames:
        data = stream.read(CHUNK, exception_on_overflow = False)
        frames.append(np.frombuffer(data, dtype=np.int16))
        if len(frames) >= WINDOW_SAMPLE:
            f+=1
            toPredict = np.concatenate(frames)
            fram.append(toPredict)
            if pred:
                res.append(pp.predictData(toPredict))
                frames=[]
    if WAVE_OUTPUT_FILENAME:
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(fram))
        waveFile.close()
    
    # stop Recording
    stream.stop_stream()
    stream.close()
    print(res)
    print("finished recording")

    return res
