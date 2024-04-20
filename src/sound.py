import sounddevice as sd
import numpy as np
import librosa
import wave


class Sound:
    def __init__(self):
        self.__duration = 30
        self.__fs = 44100
        self.__recording = None
        self.__filename = "src/audio/recording.wav"
        self.__sound_intensity_dB = 0
        self.__max_sound_intensity = 35.0

    def sound_detect(self):
        print("Recording..")
        self.__recording = sd.rec(int(self.__duration * self.__fs), samplerate=self.__fs,
                                  channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to finish
        print("Recording finished.")

    def save_audio_as_wav(self):
        with wave.open(self.__filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit PCM
            wf.setframerate(self.__fs)
            wf.writeframes(self.__recording.tobytes())

    def calculate_sound_intensity(self):
        # Open the wave file
        with wave.open(self.__filename, 'rb') as wf:
            # Get the number of frames
            num_frames = wf.getnframes()
            # Read audio data as bytes
            audio_data = wf.readframes(num_frames)

            # Convert audio data to numpy array
            audio_array = np.frombuffer(audio_data, dtype=np.int16)

            # Calculate RMS amplitude
            rms_amplitude = np.sqrt(np.mean(np.square(audio_array)))

            # Convert RMS amplitude to decibels
            self.__sound_intensity_dB = 20 * np.log10(rms_amplitude)

    def trigger_alarm_message(self):  # >= 35
        filename = "src/audio/alert_message.wav"
        if self.__sound_intensity_dB >= self.__max_sound_intensity:
            data, fs = librosa.load(filename, sr=None)
            sd.play(data)
            sd.wait()
        else:
            return

