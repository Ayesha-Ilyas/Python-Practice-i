import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample rate of what we are recording
second=10 #time span for which we are recording
#the audio you can change it to the 20 or 30 sec
print("recording......")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)#this is the main command used to record the sound. here sounddevice.rec is the device which we are using. second * fs will be an integer value. there are 3 parameters. i dont know about much.
#first of all we are recording the voice for 10 sec
sounddevice.wait()#sound intervoice class or recording to stop.
write("output.wav",fs,record_voice)#this this used here to write by write from scipy. because we want to store our recording in to output.wav file.