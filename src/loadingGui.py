import tkinter as tk
from src.gui import GUI
from time import sleep


class LoadingGui(GUI):
    def __init__(self, window, window_height, window_width, dot_img1, dot_img2, barcode_img, logo_img):
        super().__init__()
        self.__window = window
        self.__window_height = window_height
        self.__window_width = window_width
        self.__dot_img1 = dot_img1
        self.__dot_img2 = dot_img2
        self.__barcode_img = barcode_img
        self.__logo_img = logo_img

    def display_loading_animation(self):
        frame = self.create_frame(parent=self.__window, height=self.__window_height,
                                  width=self.__window_width, pos_x=0,
                                  pos_y=0)

        barcode_label = self.create_img_label(parent=frame, img=self.__barcode_img)
        barcode_label.place(x=self.__window_width / 2.25, y=self.__window_height / 8)

        self.__display_logo_title(frame)

        cosmic_meaning = "Corridor Occupancy Sound Monitoring And Identification System"
        self.create_text_body(parent=frame, text=cosmic_meaning, pos_x=(self.__window_width / 3.25),
                              pos_y=(self.__window_height / 2))

        self.__display_loading_animation(parent=frame)

        frame.destroy()

    def __display_logo_title(self, frame):
        title_logo_frame = self.create_frame(parent=frame, height=(self.__window_height / 4),
                                             width=(self.__window_width / 1.4), pos_x=(self.__window_width / 8),
                                             pos_y=(self.__window_height / 5))
        title_logo_frame.config(bd=(self.__window_width / 48), highlightcolor=self._gray, relief=tk.SUNKEN)

        # Add application logo.
        logo_img_label = self.create_img_label(parent=title_logo_frame, img=self.__logo_img)
        logo_img_label.place(x=(self.__window_width / 6.15), y=(self.__window_height / 40))

        # Add page title.
        text_position = (self.__window_height / 4) / 7
        x_text_position = (self.__window_width / 4.05)
        self.create_text_title(parent=title_logo_frame, text="S", pos_x=(x_text_position + 150), pos_y=text_position)
        self.create_text_title(parent=title_logo_frame, text="co", pos_x=x_text_position, pos_y=text_position)
        self.create_text_title(parent=title_logo_frame, text="mic", pos_x=(x_text_position + 270), pos_y=text_position)

    def __display_loading_animation(self, parent):
        self.__dot_img_label1 = self.create_img_label(parent=parent, img=self.__dot_img1)
        self.__dot_img_label2 = self.create_img_label(parent=parent, img=self.__dot_img2)
        self.__dot_img_label3 = self.create_img_label(parent=parent, img=self.__dot_img2)

        self.__x_position = self.__window_width / 2.1
        self.__y_position = self.__window_height / 1.25

        for i in range(4):
            self.__animate(parent)

    def __animate(self, parent):
        for i in range(3):
            if i == 0:
                self.__dot_img_label1.place(x=self.__x_position - 40, y=self.__y_position)
                self.__dot_img_label2.place(x=self.__x_position, y=self.__y_position)
                self.__dot_img_label3.place(x=self.__x_position + 40, y=self.__y_position)

            elif i == 1:
                self.__dot_img_label2.place(x=self.__x_position - 40, y=self.__y_position)
                self.__dot_img_label1.place(x=self.__x_position, y=self.__y_position)
                self.__dot_img_label3.place(x=self.__x_position + 40, y=self.__y_position)

            elif i == 2:
                self.__dot_img_label2.place(x=self.__x_position - 40, y=self.__y_position)
                self.__dot_img_label3.place(x=self.__x_position, y=self.__y_position)
                self.__dot_img_label1.place(x=self.__x_position + 40, y=self.__y_position)

            parent.update_idletasks()
            sleep(0.5)
