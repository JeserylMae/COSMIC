
import cv2
import cvzone
import win32gui
import win32con
import tkinter as tk
from math import ceil
from ultralytics import YOLO
from ffpyplayer.player import MediaPlayer

classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]


class Detect:
    def __init__(self, cap, canvas, window, window_width, window_height, player=None):
        self.__model = YOLO("../Yolo-Weights/yolov8n.pt")
        self.__window_name = "YOLOV8"
        self.__shall_break = False
        self.__cap = cap
        self.__canvas = canvas
        self.__window = window
        self.__window_width = window_width
        self.__window_height = window_height
        self.__player = player

    def detect_video(self):
        self.__configure_cv2_window()
        self.__create_button()  # For exit button.

        # Display the video with object detection.
        self.__display_video_to_window()

        # Close the MediaPlayer and go back to the home window.
        self.__cap.release()
        cv2.destroyAllWindows()
        self.__window.destroy()
        MediaPlayer.close_player(self.__player)

    def __display_video_to_window(self):
        while self.__cap.isOpened() and not self.__shall_break:
            success, frame = self.__cap.read()
            results = self.__model(frame, stream=True)

            if self.__player is not None:
                audio_frame, val = MediaPlayer.get_frame(self.__player)
                if val == 'eof' and self.__player is not None:
                    success = False

            if success:
                Detect.__plot_cv_points(results, frame)
                cv2.imshow(self.__window_name, frame)
                cv2.waitKey(1)

            else:
                break

    def __configure_cv2_window(self):
        # Create a window with a border
        cv2.namedWindow(self.__window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.__window_name, 800, 600)

        # Set the screen position of the window
        hwnd = win32gui.FindWindow(None, self.__window_name)
        win32gui.MoveWindow(hwnd, 60, 60, 800, 600, True)

        # Modify the window style to remove the maximizable button
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        style &= ~win32con.WS_CAPTION       # Remove title bar
        style &= ~win32con.WS_THICKFRAME    # Remove sizing border
        style &= ~win32con.WS_SYSMENU       # Remove system menu
        style &= ~win32con.WS_MINIMIZEBOX   # Remove minimize button
        style &= ~win32con.WS_MAXIMIZEBOX   # Remove maximize button
        style &= ~win32con.WS_BORDER        # Remove window border
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

        # Set the window position to be on top of all other windows
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def __exit_cmd(self):
        self.__shall_break = True

    def __create_button(self):
        width = self.__window_width - 60
        height = self.__window_height - 90
        bbb = tk.Button(master=self.__window, bg="#E77C05", font=("Roboto Mono", 18), relief=tk.SOLID,
                        fg="#FFFFFF", height=1, width=13, text="EXIT",
                        command=self.__exit_cmd)
        bbb.place(x=(width - 220), y=(height - 80))

    @staticmethod
    def open_video_path(path):
        cap = cv2.VideoCapture(path)
        sound = MediaPlayer(path)

        return cap, sound

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
            else:
                break

            cap.release()
        return cam_num

    @staticmethod
    def __plot_cv_points(results, frame):
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get points of the detected object (Bounding Box).
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1

                # Draw rectangles for the detected object.
                cvzone.cornerRect(frame, (x1, y1, w, h))

                # Get confidence level of detection.
                conf = ceil(box.conf[0] * 100) / 100

                # Get class name.
                cls = int(box.cls[0])

                # Display Confidence level and class name of detected object.
                cvzone.putTextRect(frame, f'{classNames[cls]} - {conf}', (max(0, x1), max(35, y1)),
                                   1, 1)
