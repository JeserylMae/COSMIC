import tkinter as tk
from tkinter import filedialog
from src.gui import GUI
from src.detect import Detect
from threading import Thread
from time import sleep


class HomeGui(GUI):
    def __init__(self, window, screen_width, screen_height, video_img, cam_img):
        super().__init__()
        self.__window = window
        self.__window_height = screen_height
        self.__window_width = screen_width
        self.__video_img = video_img
        self.__cam_img = cam_img
        self.__camera_list = list()
        self.__video_path = " "
        self.__selected_cam = -1

    def display_home(self, cosmic_icon):
        frame = self.create_frame(parent=self.__window, height=self.__window_height - 90,
                                  width=self.__window_width - 60, pos_x=(self.__window_width / 64),
                                  pos_y=(self.__window_width / 64))
        Thread(target=self.__get_camera_list).start()

        self.__display_icon_and_title(frame, cosmic_icon)
        sleep(0.002)
        self.__create_rectangle(frame)
        sleep(0.002)

        # Use camera button.
        self.__create_buttons(parent=frame, img=self.__video_img, color=self._darker_gray,
                              label="Open video", X=1.2, Y=3, bd=0,
                              cmd=self.__create_file_dialog)
        # Open a video button.
        self.__create_buttons(parent=frame, img=self.__cam_img, color=self._black,
                              label="Use camera", X=0.85, Y=3, bd=3,
                              cmd=lambda: self.__create_drop_menu(frame))

    def __display_icon_and_title(self, frame, cosmic_icon):
        img_frame = self.create_frame(parent=frame, height=(self.__window_height / 3),
                                      width=(self.__window_width / 2.8), pos_x=(self.__window_width / 80),
                                      pos_y=(self.__window_height / 3))

        img_label = self.create_img_label(parent=img_frame, img=cosmic_icon)
        img_label.place(x=200, y=0)

        # Add page title.
        text_position = 200
        self.create_text_title(parent=img_frame, text="S", pos_x=230, pos_y=text_position)
        self.create_text_title(parent=img_frame, text="co", pos_x=80, pos_y=text_position)
        self.create_text_title(parent=img_frame, text="mic", pos_x=350, pos_y=text_position)

    def __create_rectangle(self, parent):
        self.create_frame(parent=parent, height=(self.__window_height - 200), width=(self.__window_width / 1.9),
                          pos_y=(self.__window_height / 16), pos_x=(self.__window_width / 2.6)
                          ).config(bg=self._black, bd=2, relief='groove', highlightcolor=self._white)

    def __create_buttons(self, parent, img, color, label, X, Y, bd, cmd):
        def on_enter(e):
            button['background'] = self._gray

        def on_leave(e):
            button['background'] = color

        button = tk.Button(master=parent, bg=color, font=("Roboto Mono", 18), fg=self._white,
                           height=self.__window_height / 3.5, width=self.__window_height / 3.5,
                           bd=bd, relief='groove', image=img, text=label, compound="top",
                           highlightcolor=self._white, activebackground=color,
                           command=cmd)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.place(x=int(self.__window_height / X), y=int(self.__window_height / Y))

        return button

    def __get_camera_list(self):
        self.__camera_list = Detect.count_cameras()

    def __select_cam(self):
        self.__selected_cam = self.clicked.get()
        self.__selected_cam = int(self.__selected_cam[-1])
        print(f"Use Camera {self.__selected_cam}")

        cap = Detect.open_camera(self.__selected_cam)
        self.__insert_cv2_video_to_tkapp(cap)

    def __create_drop_menu(self, frame):
        self.clicked = tk.StringVar()
        self.clicked.set(self.__camera_list[0])

        drop_menu = tk.OptionMenu(frame, self.clicked, *self.__camera_list)
        drop_menu.place(x=int(self.__window_width / 2.1), y=(self.__window_height / 1.45))
        drop_menu.config(font=("Roboto Mono", 15), width=40, height=2, justify='center',
                         relief='flat', bg=self._black, highlightthickness=2,
                         highlightbackground=self._gray, fg=self._white)

        tk.Button(master=frame, bd=2, bg=self._darker_gray, font=("Roboto Mono", 14), fg=self._white, height=2,
                  width=10, text="Select", relief=tk.GROOVE, highlightcolor=self._white, command=self.__select_cam
                  ).place(x=(self.__window_width / 1.325), y=(self.__window_height / 1.45))

    def __create_file_dialog(self):
        video_file = filedialog.askopenfilename(
            initialdir="/", title="Select file",
            filetypes=(("video files", "*.mp4;*.avi;*.mkv;*.wav"), ("all files", "*.*"))
        )
        self.__video_path = video_file
        print(f"Video Path: {self.__video_path}\n")

        cap, sound = Detect.open_video_path(self.__video_path)
        self.__insert_cv2_video_to_tkapp(cap, sound)

    @staticmethod
    def __exit_cmd(cap, window):
        cap.release()
        window.destroy()

    def __insert_cv2_video_to_tkapp(self, cap, sound=None):
        width = self.__window_width - 60
        height = self.__window_height - 90

        new_window = self.create_frame(parent=self.__window, height=height, width=width,
                                       pos_x=(self.__window_width / 64), pos_y=(self.__window_width / 64))

        canvas = tk.Canvas(master=new_window, width=(self.__window_width - 60), height=(self.__window_height - 90),
                           bg=self._black)
        canvas.pack()

        detect = Detect(cap=cap, canvas=canvas, window=new_window, window_width=width - 250,
                        window_height=height, player=sound)
        detect.detect_video()

        tk.Button(master=new_window, bg=self._orange, font=("Roboto Mono", 18), relief=tk.SOLID,
                  fg=self._white, height=1, width=13, text="EXIT", command=lambda: HomeGui.__exit_cmd(cap, new_window)
                  ).place(x=(width-220), y=(height-80))
