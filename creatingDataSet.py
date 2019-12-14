from pydub import AudioSegment
import numpy as np
from scipy.fftpack import fft
import pydub
from scipy import signal
import array
import glob
import re
import pandas as pd
import librosa

def splitXSecond(x,overlap,path):
    '''splits audios in x=1000 ms from path= "./input_processed/*" with an overlap of 500 ms'''
    audios=[]
    for file in glob.iglob(path):
        print(file)
        a={}
        word=re.findall('[H,M]\w+',file)[0]
        audio=AudioSegment.from_file(file,format='wav')
        audio_arr=np.array(audio.get_array_of_samples()).astype("float32")
        chunks=librosa.effects.split(audio_arr, top_db=40, frame_length=2048, hop_length=512)
        for c in list(chunks):
            Fm=int((audio.frame_rate)/1000)
            length_audio=int((c[1]-c[0])/Fm)
            if length_audio>=x:
                for l in range(0,length_audio,overlap):
                    a={}
                    a['name']=word[1:]
                    a['gender']=word[0]
                    silence_filter = array.array('h')
                    silence_filter.fromlist(list(map(int,audio_arr[l*Fm:(l+x)*Fm])))
                    a['1SecArray']=silence_filter
                    audios.append(a)
    return audios

def fftransform(array):
    return np.abs(fft(array,512))

def mfccTransform(arr):
    mfc=librosa.feature.mfcc(y=np.array(arr).astype('float64'),sr=48000,n_mfcc=256)
    return np.mean(mfc,axis=1)

