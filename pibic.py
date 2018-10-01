import librosa

ZERO = 100.0

# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()
filename = 'kalimba.mp3'

# 2. Load the audio as a waveform `y`, and store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

if tempo >= ZERO:
	mood = 'excited'
else:
	mood = 'calm'
print('Mood:',mood)

# 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)
