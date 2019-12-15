import subprocess
import creatingDataSet as cds
import predictPrep as pp
import pandas as pd
import recordingVoice as rv

rv.recording()

subprocess.call(['./subprocess.sh',"./audio_received/*"])

audio=cds.splitXSecond(1000,500,"./audio_processed/*")

dfpred=pd.DataFrame(audio)

dfpred=cds.prepDf(dfpred)

result=pp.prediction(dfpred)
print(result)


#run(host='0.0.0.0', port=8080)