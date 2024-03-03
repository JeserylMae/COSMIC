
import tkinter as tk
from tkinter import font

class GUI:

    def create_text_title(self, parent, text):
        #Define font family, size and color
        custom_font = font.Font(family="Game of Squids", size=16)
        #Create label with specified font
        title_label = tk.Label(parent, text=text, font=custom_font, fg="black") #pakipalitan nalang ng color kung ano gagamitin

        title_label.pack()

    def create_text_body(self, parent, text):
        custom_font = font.Font(family="Roboto Mono", size=14)

        body_label = tk.Label(parent, text=text, font=custom_font, fg="white") #same din sa text color
        body_label.pack()

    def create_frame(self, parent, bg_color, bd_width, bd_color):
        """
        create a tk Frame
        Set the arguments as the elements of the Frame.
        :return: frame
        """

    def create_image_btn(self, parent, img):
        """

        :return: button
        """

    def create_file_dialog(self, parent):
        """
        create a Tk filedialog.
        set the default folder to be opened when the file dialog was opened
        :return: video_file
        """

    @staticmethod
    def create_window():
        """
        Create a window
        Set the window background
        Set the windows size
        :return: window
        """

    @staticmethod
    def count_cameras():
        """
        camNum = list()

        create a for-loop that will iterate 10 times.
        using opencv VideoCapture() get the boolean value of whether the camera i exists.
        if yes, append to list
        release cam

        :return: camNum
        """
