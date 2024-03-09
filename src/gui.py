
import tkinter as tk
from tkinter import font


class ImageWindow:
    def __init__(self, window, img_path, width, height):
        self.window = window
        self.img_path = img_path
        self.image = tk.PhotoImage(file=self.img_path)
        self.resized_img = self.image.subsample(width, height)


class GUI:
    # Member variables
    __gray = "#5C5C5C"
    __black = "#161616"
    __darker_gray = "#2E2E2E"
    __light_gray = "#BFBFBF"
    __orange = "#E77C05"
    __white = "#FFFFFF"

    def create_text_title(self, parent, text, pos_x, pos_y):
        # Define font family, size and color
        custom_font = font.Font(family="Game of Squids", size=80)
        # Create label with specified font
        title_label = tk.Label(parent, text=text, font=custom_font, fg=self.__white, bg=self.__black)

        title_label.place(x=pos_x, y=pos_y)

    def create_text_body(self, parent, text):
        custom_font = font.Font(family="Roboto Mono", size=14)

        body_label = tk.Label(parent, text=text, font=custom_font, fg="white")  # same din sa text color
        body_label.pack()

    def create_frame(self, parent, height, width, pos_x, pos_y):
        frame = tk.Frame(parent, background=self.__black, bd=0, width=width, height=height)
        frame.place(x=pos_x, y=pos_y)
        return frame

    def create_img_label(self, parent, img):
        label = tk.Label(parent, image=img, bg=self.__black)
        return label

    @staticmethod
    def set_window_attributes(window):
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()

        window.title("Cosmic")
        window.state('zoomed')
        window.config(width=window_width,
                      height=window_height,
                      bg=GUI.__black)
        window.resizable(False, False)
        window.iconbitmap("src/images/clipboard.ico")

        return window_width, window_height

    def get_black(self): return self.__black
    def get_white(self): return self.__white
    def get_gray(self): return self.__gray
    def get_darker_gray(self): return self.__darker_gray
