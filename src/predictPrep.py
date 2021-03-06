from joblib import load
import numpy as np
import creatingDataSet as cds
import json
from keras import models
from keras.models import model_from_json
import neuralN as nn
import os
from sklearn import preprocessing
from scipy import signal

def prediction(arr):
    '''predicting X_test'''

    X_test=np.vstack([arr])
    res=nn.nn_prediction(X_test)

    '''if we want to predict with randomforest model'''
    '''X_test=np.expand_dims(arr,axis=0)
    clf = load('../models/modelo4.joblib')
    res = clf.predict(X_test)'''
    return res

def treating(data):
    '''treating data applying fft and mfcc'''

    '''low filter butterworth'''
    b, a = signal.butter(3, 4000/24000,'lowpass')
    data=signal.filtfilt(b, a, data)

    fft=np.array(cds.fftransform(data))
    mfcc=np.array(cds.mfccTransform(data))
    #con todo
    arr=np.array(data)
    #return np.concatenate((fft,mfcc))
    return np.concatenate((arr,fft,mfcc))

def predictData(audioData):
    '''prediction results'''

    tot_array=treating(audioData)
    res = prediction(tot_array)
    print(tot_array.shape)
    '''prediction with 1secarray'''
    #res = prediction(audioData)
    x=sorted(list(res[0]),reverse=True)[:5]
    le = preprocessing.LabelEncoder()
    le.classes_ = np.load('./class_names/class_names11.npy',allow_pickle=True)
    topResults = []
    for e in x:
        topResults.append(le.inverse_transform([list(res[0]).index(e)])[0])
    #topResultsStr = ','.join(topResults[1:])
    print(f'TOP: {topResults[:3]}')
    
    '''if with randomforest'''
    #print(res[:5])
    #os.system('clear')
    print('topresults',topResults)
    return  topResults
