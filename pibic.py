from __future__ import print_function
import numpy as np
import soundfile as sf
import librosa

PACE = 110.0

# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()

# 1a. Get the file path to specific audio samples
# filename = 'C:\\TCC-master\\kalimba.mp3'
# filename = 'C:\\TCC-master\\harp.mp3'
# filename = 'C:\\TCC-master\\topgear.mp3'
# filename = 'C:\\TCC-master\\hadou.mp3'

# 1b. Get all audio files in a directory sub-tree
files = librosa.util.find_files('~/Music')

# 1c. Read from an URL
# url = "https://raw.githubusercontent.com/librosa/librosa/master/tests/data/test1_44100.wav"
# y, sr = sf.read(io.BytesIO(urlopen(url).read()))

# 2. Load the audio as a waveform `y`, and store the sampling rate as `sr`
y, sr = librosa.load(filename)
# y, sr = sf.read(filename)
# y, sr = librosa.load(files)

# 3a. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 3b. Get the tempo
onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

# 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)

# First metric: duration
duration = librosa.get_duration(y)
print('Duration (in seconds): ', duration)

# Second metric: pace
if tempo < 40: pace = 'larghissimo'
  else
  if tempo < 52: pace = 'largo'
  else
  if tempo < 60: pace = 'largo-lento'
  else
  if tempo < 61: pace = 'largo-lento-adagio'
  else
  if tempo < 69: pace = 'lento-adagio'
  else
  if tempo < 76: pace = 'adagio'
  else
  if tempo < 81: pace = 'adagio-andante'
  else
  if tempo < 88: pace = 'andante'
  else
  if tempo < 100: pace = 'andante-moderato'
  else
  if tempo < 101: pace = 'andante-moderato-allegretto'
  else
  if tempo < 112: pace = 'moderato-allegretto'
  else
  if tempo < 113: pace = 'moderato-allegretto-allegro'
  else
  if tempo < 129: pace = 'allegretto-allegro'
  else
  if tempo < 138: pace = 'allegro'
  else
  if tempo < 140: pace = 'allegro-vivace'
  else
  if tempo < 143: pace = 'allegro-vivace-presto'
  else
  if tempo < 161: pace = 'allegro-presto'
  else
  if tempo < 188: pace = 'presto'
  else
  if tempo < 201: pace = 'presto-prestissimo'
  else: pace = 'prestissimo'
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
print(array)
print('Max power (in dB): ', maxpower)
print('Min power (in dB): ', minpower)

if maxpower >= 30.0: percussion = 'featured'
else: percussion = 'absent'
print('Percussion: ', percussion)
