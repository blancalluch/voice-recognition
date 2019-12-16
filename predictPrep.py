from joblib import load
import numpy as np
import creatingDataSet as cds
import json
from keras import models
from keras.models import model_from_json

def prediction(arr):

    with open('./models/Model_0.6007194519042969_16-20-44.h5.json','r') as f:
        model_json = json.load(f)

    model = model_from_json(model_json)
    model.load_weights('./models/Model_0.6007194519042969_16-20-44.h5.h5')
    print('Model loaded')
    X_test=np.hstack(arr)
    #X_test=np.expand_dims(arr,axis=0)
    print(X_test.shape,arr)
    #clf = load('./models/primer_nn.joblib')
    #res = clf.predict(X_test)
    res = model.predict(X_test)
    return res

def treating(data):

    fft=np.array(cds.fftransform(data))
    mfcc=np.array(cds.mfccTransform(data))
    return np.concatenate((fft,mfcc))

def predictData(audioData):
    tot_array=treating(audioData)
    res = prediction(tot_array)
    print(res)