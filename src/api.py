from bottle import get,post,run
import mainPredict as mainPred
import mainCreateDS as mainCrea
import recordingVoice as rv

@get("/name")
def getName():
    '''returns name of the person speaking'''
    rv.recording(24000,1000,0,1)
    return

@post("/audio/<gender>/<name>/addaudio")
def postAudio(gender,name):
    '''updates dataset with audio from a new person'''
    '''calling function recording with rate=35000 and chunk=1000' (35 seconds)'''
    rv.recording(35000,1000,f'../input/{gender}{name}.wav',0)

    return f"audio from {name} added"

run(host='0.0.0.0', port=8080)
