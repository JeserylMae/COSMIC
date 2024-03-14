from src.gui import GUI


class ImageWindow:
    def __init__(self, window, img_path, width, height):
        self.window = window
        self.img_path = 'src/images/image-removebg-preview.png'
        self.image = tk.PhotoImage(file=self.img_path)
        self.resized_img = self.image.subsample(width, height)

        img_label = tk.Label(window, image=self.resized_img, bg="black")
        img_label.place(x=0, y=0)


class LoadingGui(GUI):
    def display_loading_animation(self):
        window_width, window_height = self.set_window_attributes(self.window)

        loading_img_path = 'src/images/image-removebg-preview.png'
        loading_img = ImageWindow(self.window, loading_img_path, 16, 16)

        loading_text = "LOADING COSMIC\nCORRIDOR OCCUPANCY SOUND MONITORING AND IDENTIFICATION SYSTEM"
        self.create_text_title(self.window, loading_text, window_width // 2 - 350, window_height // 2 - 200)

        version_text = "Version 1.0.0"
        self.create_text_body(self.window, version_text)
