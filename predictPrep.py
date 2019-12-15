from joblib import load

def prediction(df):

    X_test=list(map(lambda x: x,df['fft+mfcc']))
    clf = load('./models/modeli4.joblib')
    res = clf.predict(X_test)
    
    return res