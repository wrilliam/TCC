from __future__ import print_function
import numpy as np
import soundfile as sf
import librosa
import time
import sys

START = int(round(time.time() * 1000))

# 1. Get the file path to the included audio example
#filename = librosa.util.example_audio_file()

# 1a. Get the file path to specific audio samples
filename = 'C:\\TCC-master\\music\\Music 25.mp3'

# 1b. Get all audio files in a directory sub-tree
#files = librosa.util.find_files('~/Music')

# 1c. Read from an URL
#url = "https://raw.githubusercontent.com/librosa/librosa/master/tests/data/test1_44100.wav"
#y, sr = sf.read(io.BytesIO(urlopen(url).read()))

# 2. Load the audio as a waveform `y`, and store the sampling rate as `sr`
y, sr = librosa.load(filename)
#y, sr = sf.read(filename)
LOADING = int(round(time.time() * 1000))

# First metric: duration
duration = librosa.get_duration(y)
#print('Duration: {:.2f} seconds'.format(duration))
#time1 = time.time_ns()
TIME1 = int(round(time.time() * 1000))

# 3a. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#time2 = time.time_ns()
TIME2 = int(round(time.time() * 1000))

# 3b. Get the tempo
#onset_env = librosa.onset.onset_strength(y, sr=sr)
#tempo1 = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
#print('Estimated tempo: ', tempo1, ' beats per minute')

# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#print('Saving output to beat_times.csv')
#librosa.output.times_csv('beat_times.csv', beat_times)

# Second metric: pace
#if tempo < 52.0: pace = 'broadly slow'
#else:
#    if tempo < 76.0: pace = 'slow'
#    else:
#        if tempo < 100.0: pace = 'moderately slow'
#        else:
#            if tempo < 112.0: pace = 'somewhat fast'
#            else:
#                if tempo < 138.0: pace = 'fast'
#                else:
#                    if tempo < 143.0: pace = 'fast & lively'
#                    else:
#                        if tempo < 188.0: pace = 'very fast'
#                        else: pace = 'broadly fast'
#print('Pace: ', pace)

# Third metric: presence of percussive instruments
y_harmonic, y_percussive = librosa.effects.hpss(y, margin=5.0)
librosa.output.write_wav('C:\\TCC-master\\percussive.wav', y_percussive, sr)
librosa.output.write_wav('C:\\TCC-master\\harmonic.wav', y_harmonic, sr)
S = np.abs(librosa.stft(y_percussive))
array = librosa.power_to_db(S**2)
maxpower = array.max()
#minpower = array.min()
#print('Max power (in dB): ', maxpower)

if maxpower >= 30.0: percussion = 'true'
else: percussion = 'false'
#print('Percussion:', percussion)
#time3 = time.time_ns()
TIME3 = int(round(time.time() * 1000))

loading = LOADING - START
time1 = TIME1 - START
time2 = TIME2 - TIME1 + loading
time3 = TIME3 - TIME2 + loading
#print(START)
#print(LOADING, loading)
#print(TIME1, time1)
#print(TIME2, time2)
#print(TIME3, time3)
print(time1, time2, time3)

input('Press ENTER to exit...')
sys.exit()
