import subprocess
import creatingDataSet as cds
import pandas as pd
import numpy as np
subprocess.call('./subprocess.sh')

audio_dict=cds.splitXSecond(1000,500,"./input_processed/*")

dfAudio=pd.DataFrame(audio_dict)

dfAudio['fft']=dfAudio['1SecArray'].apply(lambda x: cds.fftransform(x))

dfAudio['mfcc']=dfAudio['1SecArray'].apply(lambda x: cds.mfccTransform(x))
dfAudio['gender']=list(map(lambda x: 1 if x=='H' else 0,dfAudio['gender']))
dfAudio['fft+mfcc']=list(map(lambda x,y: np.concatenate((np.array(x),np.array(y))),dfAudio['fft'],dfAudio['mfcc']))
dfAudio.drop(columns=['fft','mfcc'],inplace=True)
dfAudio.to_pickle('./output/DataSetAudios.pkl')
