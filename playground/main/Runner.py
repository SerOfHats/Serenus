import threading
import visualise, playAudio


def live():
    # set data stream to audio input and pass to visualise and playAudio
    visualise.graph("live", "")

def from_file(filename):
    # get file as stream and pass to visualise and playAudio
    t1 = threading.Thread(target=visualise.graph, args=("file", filename,))
    t1.start()
    t2 = threading.Thread(target=playAudio.play, args=(filename,))
    t2.start()

    
# Visualise real time data
live()

# Visualise data from .wav and play it
#from_file("80s.wav")