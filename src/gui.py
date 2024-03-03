
import tkinter as tk

class GUI:

    def create_text_title(self, parent, text):
        """
        create a Tk label
        set The default font family to "Game of Squids" btw install the font "Game of Squids" in your computer
        set the default font size, color
        :return: none
        """

    def create_text_body(self, parent, text):
        """
        create a Tk Label
        set the default font family to "Roboto Mono" btw install the font "Game of Squids" from Google Fonts.
        set the default font size, color
        :return: none
        """

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
