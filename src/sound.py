import sounddevice as sd
import wave


class Sound:
    def __init__(self):
        self.__duration = 30
        self.__fs = 44100
        self.__recording = None

    def sound_detect(self):
        print("Recording..")
        self.__recording = sd.rec(int(self.__duration * self.__fs), samplerate=self.__fs,
                                  channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to finish
        print("Recording finished.")

    def save_audio_as_wav(self):
        filename = "recoding.wav"

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit PCM
            wf.setframerate(self.__fs)
            wf.writeframes(self.__recording.tobytes())
