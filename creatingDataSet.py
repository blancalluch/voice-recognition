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
        audio_arr=np.array(audio.get_array_of_samples()).astype("float64")
        chunks=librosa.effects.split(audio_arr, top_db=40, frame_length=2048, hop_length=512)
        for c in list(chunks):
            Fm=int((audio.frame_rate)/1000)
            length_audio=int((c[1]-c[0])/Fm)
            if length_audio>=x:
                for l in range(0,length_audio,overlap):
                    if max(audio_arr[l*Fm:(l+x)*Fm])>62:
                        a={}
                        print(Fm,l)
                        a['name']=word[1:]
                        a['gender']=word[0]
                        silence_filter = array.array('h')
                        silence_filter.fromlist(list(map(int,audio_arr[l*Fm:(l+x)*Fm])))
                        a['1SecArray']=silence_filter
                        audios.append(a)
    return audios

def fftransform(array):
    '''fft to all the array (column in this case)'''
    return np.abs(fft(array,512))

def mfccTransform(arr):
    '''mfcc to all the array (column in this case)'''
    mfc=librosa.feature.mfcc(y=np.array(arr).astype('float64'),sr=48000,n_mfcc=256)
    return np.mean(mfc,axis=1)

def prepDf(dfAudio):
    '''applies fft and mfcc to 1SecArray column, concatenates them and drops fft and mccf.'''
    dfAudio['fft']=dfAudio['1SecArray'].apply(lambda x: fftransform(x))
    dfAudio['mfcc']=dfAudio['1SecArray'].apply(lambda x: mfccTransform(x))
    dfAudio['gender']=list(map(lambda x: 1 if x=='H' else 0,dfAudio['gender']))
    dfAudio['fft+mfcc']=list(map(lambda x,y: np.concatenate((np.array(x),np.array(y))),dfAudio['fft'],dfAudio['mfcc']))
    dfAudio.drop(columns=['fft','mfcc'],inplace=True)

    return dfAudio


