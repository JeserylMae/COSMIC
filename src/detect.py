
import cv2
import tkinter as tk
from PIL import Image, ImageTk


class Detect:
    def __init__(self, cap, canvas, window, window_width, window_height):
        self.__cap = cap
        self.__canvas = canvas
        self.__window = window
        self.__window_width = window_width
        self.__window_height = window_height

    def detect_video(self):
        success, frame = self.__cap.read()

        if success:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = img.resize(size=(self.__window_width, self.__window_height))

            img = ImageTk.PhotoImage(image=img)

            self.__canvas.img = img
            self.__canvas.create_image(0, 0, anchor=tk.NW, image=img)

            self.__window.after(10, self.detect_video)
        else:
            self.__cap.release()
            self.__window.destroy()

    @staticmethod
    def open_video_path(path):
        cap = cv2.VideoCapture(path)

        return cap

    @staticmethod
    def open_camera(cam_id):
        cap = cv2.VideoCapture(cam_id)
        cap.set(3, 1280)
        cap.set(4, 720)

        return cap

    @staticmethod
    def count_cameras():
        cam_num = list()
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                cam_num.append(f"Camera {i}")
                print(f"Camera {i} is available...")
            else:
                break

            cap.release()
        return cam_num
