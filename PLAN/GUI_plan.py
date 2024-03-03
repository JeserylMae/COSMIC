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

class LoadingGui(GUI):
    def display_loading_animation(self):
    """
    contains the main window for loading page.
    
    Dito ica-call yong mga functions from GUI, 
    para mabuo yong designs ng loading page.
    (Ang template ay nasa figma).
    """

class HomeGui(GUI):

    def display_home(self):
    """
    contains the main window for home page
    Ica-call lang din mga GUI functions dito
    para mabuo yong home page. The yong choice
    ng user about kung anong gusto nyang gamitin 
    (video or camera ba) ay ipi-print na lang muna
    console.
    """
    def create_buttons(self, parent):
    """
    Set the default elements ng button.
    :return: button
    """
    def create_drop_menu(self, parent):
        """
        Set the default elements of drop
        down menu
        :return: drop_menu
        """
