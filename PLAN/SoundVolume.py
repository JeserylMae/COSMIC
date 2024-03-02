
import sounddevice as sd
import librosa

# Define parameters for recording
duration = 60  # Duration of recording in seconds
sample_rate = 44100  # Sample rate
channels = 1  # Number of audio channels (mono)

# Record audio from microphone
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
sd.wait()  # Wait until recording is finished

# Convert audio data to mono and flatten to 1D array
audio_data_mono = audio_data.flatten()

# Calculate loudness using librosa
loudness = librosa.amplitude_to_db(librosa.feature.rms(y=audio_data_mono), ref=1.0)[0][0]

print(f"Loudness: {loudness} dB")
