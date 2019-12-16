from joblib import load
import numpy as np

def prediction(arr):

    X_test=np.expand_dims(arr,axis=0)
    clf = load('./models/modeli6.joblib')
    res = clf.predict(X_test)
    
    return res