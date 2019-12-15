import sounddevice as sd
from scipy.io.wavfile import write

def recording():
    fs = 44100  # Sample rate
    seconds = 30  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./audio_received/MTesting.wav', fs, myrecording)  # Save as WAV file

    return None