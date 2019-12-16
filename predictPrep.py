from joblib import load
import numpy as np
import creatingDataSet as cds
import json
from keras import models
from keras.models import model_from_json
import neuralN as nn

def prediction(arr):

    X_test=np.vstack(arr)
    #X_test=np.expand_dims(arr,axis=0)
    print(X_test.shape,arr)
    #clf = load('./models/primer_nn.joblib')
    #res = clf.predict(X_test)
    res=nn.nn_model(X_test)
    #res = model.predict(X_test)
    return res

def treating(data):

    fft=np.array(cds.fftransform(data))
    mfcc=np.array(cds.mfccTransform(data))
    return np.concatenate((fft,mfcc))

def predictData(audioData):
    tot_array=treating(audioData)
    res = prediction(tot_array)
    print(res)