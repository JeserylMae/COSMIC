import pyaudio
import numpy as np

class SoundDetector:
    def __init__(self, threshold=0.1, chunk_size=1024, format=pyaudio.paInt16, channels=1, rate=44100, max_record_time=30):
        self.threshold = threshold
        self.chunk_size = chunk_size
        self.format = format
        self.channels = channels
        self.rate = rate
        self.max_record_time = max_record_time
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer=self.chunk_size)

    def detect_sound(self):
        try:
            recorded_frames = self.record_sound()
            sound_detected = False
            for data in recorded_frames:
                if np.max(data) > self.threshold * np.iinfo(np.int16).max:
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

if _name_ == "_main_":
    detector = SoundDetector()
    detector.detect_sound()
