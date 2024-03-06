
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
        frame = tk.Frame(parent, bg=bg_color, bd=bd_width, relief="solid", highlightbackground=bd_color)
        frame.pack(pady=10)
        return frame

    def create_image_btn(self, parent, img):
        button = tk.Button(parent, image=img, bg="white", command=lambda: print("Button clicked"))
        button.image = img
        button.pack(pady=10)
        return button

    def create_file_dialog(self, parent):
        video_file = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("video files", "*.mp4;*.avi;*.mkv"), ("all files", "*.*")))

        return video_file

    @staticmethod
    def create_window():
        window = tk.Tk()
        window.title("Video Processing App")
        window.geometry("800x600")
        window.configure(bg="white")
        return window

    @staticmethod
    def count_cameras():
        camNum = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                camNum.append(i)
                print(f"Camera {i} is available.")
            cap.release()
        return camNum
