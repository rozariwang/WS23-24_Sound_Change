import subprocess
import os

def convert(file):
    tokens = file.split('.')
    filename = tokens[0]
    command = "ffmpeg -i ./data/audio/" + file + " -ab 160k -ac 2 -ar 44100 -vn ./data/wav/" + filename + ".wav"
    #command = "ffmpeg -i ./data/audio/" + file + " " + filename + ".wav"
    #"ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    print(command)
    subprocess.call(command, shell=True)

directory = os.fsencode('./data/audio')

# for audio in os.listdir(directory):
#     file = os.fsdecode(audio)
#     convert(file)