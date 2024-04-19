import pyaudio
import numpy as np
import librosa


class SoundDetector:
    def __init__(self, threshold=0.1, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=44100, max_record_time=30):
        #self.threshold = 0.1
        self.threshold = threshold
        self.chunk_size = chunk_size
        #self.chunk_size = 1024
        self.format = format
        #self.format = pyaudio.paInt16
        self.channels = channels
        #self.channels = 1
        #self.rate = 44100
        self.rate = rate
        self.max_record_time = max_record_time
        #self.max_record_time = 30
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.chunk_size)

    def detect_sound(self):
        try:
            print("Recording sound for 30 seconds...")
            recorded_frames = self.record_sound()
            print("Recording finished. Number of recorded frames: ", len(recorded_frames))
            sound_detected = False
            for data in recorded_frames:
                audio_data = np.frombuffer(data, dtype=np.int16)
                normalized_audio = audio_data / np.iinfo(np.int16).max
                if np.max(normalized_audio) > self.threshold:
               # if np.max(data) > self.threshold * np.iinfo(np.int16).max:
                    print("Sound detected!")
                    sound_detected = True
                    break
                else:
                    print("Silence")
            if not sound_detected:
                print("No sound detected during recording.")
        except KeyboardInterrupt:
            pass
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()

    def record_sound(self):
        frames = []
        max_record_frames = int(self.rate / self.chunk_size * self.max_record_time)
        try:
            for _ in range(max_record_frames):
                data = self.stream.read(self.chunk_size)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        return frames

    if __name__ == "__main__":
        #adjust threshold mas mababa ay mas sensitive daw
        threshold_level = 0.05
        detector = SoundDetector(threshold=threshold_level)
        detector.detect_sound()
    # def calculate_intensity(self, data):
    #    rms_amplitude = librosa.feature.rms(y=np.frombuffer(data, dtype=np.int16))[0]
    #     intensity_db = librosa.amplitude_to_db(rms_amplitude, ref=np.max)[0]
    #     return intensity_db


#
# if _name_ == "_main_":
#     detector = SoundDetector()
#     detector.detect_sound()
