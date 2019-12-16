import subprocess
import creatingDataSet as cds
import pandas as pd
import numpy as np

subprocess.call(['./subprocess.sh',"./input/*"])

audio_dict=cds.splitXSecond(1000,500,"./input_processed/*")

dfAudio=pd.DataFrame(audio_dict)

dfAudio=cds.prepDf(dfAudio)

dfAudio.to_pickle('./output/DataSetAudios.pkl')
