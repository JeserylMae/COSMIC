
import tkinter as tk
from tkinter import font


class ImageWindow:
    def __init__(self, window, img_path, width, height):
        self.window = window
        self.img_path = img_path
        self.image = tk.PhotoImage(file=self.img_path)
        self.resized_img = self.image.subsample(width, height)


class GUI:
    def __init__(self):
        self._gray = "#5C5C5C"
        self._black = "#161616"
        self._darker_gray = "#2E2E2E"
        self._light_gray = "#BFBFBF"
        self._orange = "#E77C05"
        self._white = "#FFFFFF"

    def create_text_title(self, parent, text, pos_x, pos_y):
        # Define font family, size and color
        custom_font = font.Font(family="Game of Squids", size=80)
        # Create label with specified font
        title_label = tk.Label(parent, text=text, font=custom_font, fg=self._white, bg=self._black)

        title_label.place(x=pos_x, y=pos_y)

    def create_text_body(self, parent, text, pos_x, pos_y):
        custom_font = font.Font(family="Roboto Mono", size=14)

        body_label = tk.Label(parent, text=text, font=custom_font, fg=self._white, bg=self._black)
        body_label.place(x=pos_x, y=pos_y)

    def create_frame(self, parent, height, width, pos_x, pos_y):
        frame = tk.Frame(parent, background=self._black, bd=0, width=width, height=height)
        frame.place(x=pos_x, y=pos_y)
        return frame

    def create_img_label(self, parent, img):
        label = tk.Label(parent, image=img, bg=self._black)
        return label

    @staticmethod
    def set_window_attributes(window):
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()
        bg_color = GUI().get_black()

        window.title("Cosmic")
        window.state('zoomed')
        window.config(width=window_width,
                      height=window_height,
                      bg=bg_color)
        window.resizable(False, False)
        window.iconbitmap("src/images/clipboard.ico")

        return window_width, window_height

    def get_black(self): return self._black
