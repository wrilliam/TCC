from __future__ import print_function
import numpy as np
import soundfile as sf
import librosa
import time
import sys

START = int(round(time.time() * 1000))

filename = 'C:\\TCC-master\\music\\Music 25.mp3'
y, sr = librosa.load(filename)

LOADING = int(round(time.time() * 1000))

duration = librosa.get_duration(y)
#print('Duration: {:.2f} seconds'.format(duration))

TIME1 = int(round(time.time() * 1000))

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

TIME2 = int(round(time.time() * 1000))

y_harmonic, y_percussive = librosa.effects.hpss(y, margin=5.0)
librosa.output.write_wav('C:\\TCC-master\\percussive.wav', y_percussive, sr)
librosa.output.write_wav('C:\\TCC-master\\harmonic.wav', y_harmonic, sr)
S = np.abs(librosa.stft(y_percussive))
array = librosa.power_to_db(S**2)
maxpower = array.max()
if maxpower >= 30.0: percussion = 'true'
else: percussion = 'false'
#print('Percussion:', percussion)

TIME3 = int(round(time.time() * 1000))

loading = LOADING - START
timeDuration = TIME1 - LOADING
timePace = TIME2 - TIME1
timePercussion = TIME3 - TIME2

time1 = loading + timePace + timeDuration
time2 = loading + timePace + timePercussion
time3 = loading + timePercussion + timeDuration

print(time1, time2, time3)

input('Press ENTER to exit...')
sys.exit()
