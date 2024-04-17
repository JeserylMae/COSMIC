import cv2
import cvzone
import win32gui
import win32con
import numpy as np
import tkinter as tk
from math import ceil
from ultralytics import YOLO
from ffpyplayer.player import MediaPlayer


class Detect:
    def __init__(self, cap, window, window_width, window_height, player_path=None):
        self.__window_name = "YOLOV8"
        self.__shall_break = False
        self.__cap = cap
        self.__window = window
        self.__window_width = window_width
        self.__window_height = window_height
        self.__player_path = player_path
        self.__person_count = 0  # Initialize person count

        if self.__player_path is not None:
            self.__model = YOLO("../Yolo-Weights/yolov8n.pt")
        else:
            self.__model = YOLO("../Yolo-Weights/yolov8s.pt")

    def detect_video(self):
        self.__configure_cv2_window()
        self.__create_button()  # For exit button.

        # Display the video with object detection.
        if self.__player_path is None:
            self.__display_camera_video_to_window()
        else:
            self.__display_recorded_video_to_window()
            MediaPlayer.close_player(self.__player)

        # Close the MediaPlayer and go back to the home window.
        self.__cap.release()
        cv2.destroyAllWindows()
        self.__window.quit()

    def __display_camera_video_to_window(self):
        while self.__cap.isOpened() and not self.__shall_break:
            success, frame = self.__cap.read()
            results = self.__model(frame, stream=True)

            if success:
                self.__person_count = 0  # Reset person count for each frame
                self.__plot_cv_points(results, frame)
                self.__display_with_person_count(frame)  # Display with person count
                cv2.waitKey(1)
            else:
                break

    def __display_recorded_video_to_window(self):
        self.__player = MediaPlayer(self.__player_path)

        while True and not self.__shall_break:
            frame, success = self.__player.get_frame()

            if success == 'eof':
                break
            elif frame is not None:
                # Extract frame data and shape
                video_frame = frame[0]
                frame_w, frame_h = video_frame.get_size()

                # Convert frame data to a bytes object
                frame_bytes = video_frame.to_bytearray()[0]

                # Decode the bytes object to a NumPy array
                np_arr = np.frombuffer(frame_bytes, np.uint8).reshape(frame_h, frame_w, 3)

                # Convert color format from RGB to BGR
                np_arr_bgr = cv2.cvtColor(np_arr, cv2.COLOR_RGB2BGR)

                results = self.__model(np_arr_bgr, stream=True)

                # Display the frame
                self.__person_count = 0  # Reset person count for each frame
                self.__plot_cv_points(results, np_arr_bgr)
                self.__display_with_person_count(np_arr_bgr)  # Display with person count
                cv2.waitKey(100)  # Adjust frame rate as needed

    def __configure_cv2_window(self):
        # Create a window with a border
        cv2.namedWindow(self.__window_name, cv2.WINDOW_NORMAL)
        # cv2.resizeWindow(self.__window_name, self.__window_width, self.__window_height)

        # Set the screen position of the window
        hwnd = win32gui.FindWindow(None, self.__window_name)
        win32gui.MoveWindow(hwnd, 45, 85, self.__window_width - 50, self.__window_height - 45, True)

        # Modify the window style to remove the maximizable button
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        style &= ~win32con.WS_CAPTION  # Remove title bar
        style &= ~win32con.WS_THICKFRAME  # Remove sizing border
        style &= ~win32con.WS_SYSMENU  # Remove system menu
        style &= ~win32con.WS_MINIMIZEBOX  # Remove minimize button
        style &= ~win32con.WS_MAXIMIZEBOX  # Remove maximize button
        style &= ~win32con.WS_BORDER  # Remove window border
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

        # Set the window position to be on top of all other windows
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def __exit_cmd(self):
        self.__shall_break = True

    def __create_button(self):
        bbb = tk.Button(master=self.__window, bg="#E77C05", font=("Roboto Mono", 18), relief=tk.SOLID,
                        fg="#FFFFFF", height=1, width=15, text="EXIT",
                        command=self.__exit_cmd)
        bbb.place(x=(self.__window_width - 8), y=(self.__window_height - 85))

    @staticmethod
    def open_video_path(path):
        cap = cv2.VideoCapture(path)
        sound = path

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

    def __plot_cv_points(self, results, frame):  # Adjusted to instance method
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

                # Increment person count if a person is detected
                if classNames[cls] == "person":
                    self.__person_count += 1  # Accessing instance attribute

                # Display Confidence level and class name of detected object.
                cvzone.putTextRect(frame, f'{classNames[cls]} - {conf}',
                                   (max(0, x1), max(35, y1)),
                                   1.5, 2)

    def __display_with_person_count(self, frame):
        # Display the frame
        cv2.putText(frame, f'Persons detected: {self.__person_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(self.__window_name, frame)

# Example usage:
if __name__ == "__main__":
    # Example: Open camera
    cam_id = 0  # Change this according to your camera id
    cap = cv2.VideoCapture(cam_id)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Example: Create Tkinter window
    window_width, window_height = 800, 600
    root = tk.Tk()
    root.title("YOLO Object Detection")
    root.geometry(f"{window_width}x{window_height}")

    # Create Detect object and start detection
    detect_obj = Detect(cap, root, window_width, window_height)
    detect_obj.detect_video()

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "sofa", "potted plant", "bed", "dining table", "toilet", "tv monitor", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush", "pen"
]
