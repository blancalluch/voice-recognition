#import sounddevice as sd
#from scipy.io.wavfile import write

import pyaudio
import wave
import creatingDataSet as cds
import numpy as np
import predictPrep as pp

def recording():
    '''fs = 44100  # Sample rate
    seconds = 30  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./audio_received/MTesting.wav', fs, myrecording)  # Save as WAV file'''

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 24000
    CHUNK = 1536
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "./audio_received/MTesting.wav"
    
    audio = pyaudio.PyAudio()
    
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        d=np.frombuffer(data, dtype=np.int16)
        tot_array=treating(d)
        res = pp.prediction(tot_array)
        print(res)
        frames.append(data)
    print("finished recording")
    
    
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return None

def treating(data):

    fft=np.array(cds.fftransform(data))
    mfcc=np.array(cds.mfccTransform(data))

    return np.concatenate((fft,mfcc))