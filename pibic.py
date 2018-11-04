from __future__ import print_function
import numpy as np
import soundfile as sf
import librosa

# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()

# 1a. Get the file path to specific audio samples
# filename = 'C:\\TCC-master\\kalimba.mp3'
# filename = 'C:\\TCC-master\\harp.mp3'
# filename = 'C:\\TCC-master\\topgear.mp3'
# filename = 'C:\\TCC-master\\hadou.mp3'
filename = 'C:\\TCC-master\\music\\Woodlands.mp3'

# 1b. Get all audio files in a directory sub-tree
# files = librosa.util.find_files('~/Music')

# 1c. Read from an URL
# url = "https://raw.githubusercontent.com/librosa/librosa/master/tests/data/test1_44100.wav"
# y, sr = sf.read(io.BytesIO(urlopen(url).read()))

# 2. Load the audio as a waveform `y`, and store the sampling rate as `sr`
y, sr = librosa.load(filename)
# y, sr = sf.read(filename)

# 3a. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 3b. Get the tempo
# onset_env = librosa.onset.onset_strength(y, sr=sr)
# tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

# 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)

# First metric: duration
duration = librosa.get_duration(y)
print('Duration: {:.2f} seconds'.format(duration))

# Second metric: pace
if tempo < 52.0: pace = 'broadly slow'
else:
    if tempo < 76.0: pace = 'slow'
    else:
        if tempo < 100.0: pace = 'moderately slow'
        else:
            if tempo < 112.0: pace = 'somewhat fast'
            else:
                if tempo < 138.0: pace = 'fast'
                else:
                    if tempo < 143.0: pace = 'fast & lively'
                    else:
                        if tempo < 188.0: pace = 'very fast'
                        else: pace = 'broadly fast'
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
print('Pace: ', pace)

y_harmonic, y_percussive = librosa.effects.hpss(y, margin=5.0)
librosa.output.write_wav('C:\\TCC-master\\percussive.wav', y_percussive, sr)
librosa.output.write_wav('C:\\TCC-master\\harmonic.wav', y_harmonic, sr)

# Third metric: presence of percussive instruments
S = np.abs(librosa.stft(y_percussive))
array = librosa.power_to_db(S**2)
maxpower = array.max()
minpower = array.min()
print('Max power (in dB): ', maxpower)

if maxpower >= 30.0: percussion = 'featured'
else: percussion = 'absent'
print('Percussion: ', percussion)

# Testing queries
if pace == 'slow' and duration <= 180: print('Query 1: true')
else: print('Query 1: false')
if pace == 'fast' and percussion == 'featured': print('Query 2: true')
else: print('Query 2: false')
if percussion == 'absent' and duration >= 120: print('Query 3: true')
else: print('Query 3: false')
