
import tkinter as tk
from src.gui import GUI
from src.gui import ImageWindow
from src.homeGui import HomeGui


def main():
    app = tk.Tk()
    # Setting the properties of the window.
    screen_width, screen_height = GUI.set_window_attributes(app)

    # Create images.
    cosmic_img = ImageWindow(window=app, width=2, height=2, img_path="src/images/image-removebg-preview.png")
    video_img = ImageWindow(window=app, width=1, height=1, img_path="src/images/icons8-video-100.png")
    camera_img = ImageWindow(window=app, width=1, height=1, img_path="src/images/icons8-camera-100.png")

    # Creating the main frame for Home page.
    home = HomeGui(window=app, screen_width=screen_width, screen_height=screen_height,
                   video_img=video_img.resized_img, cam_img=camera_img.resized_img)
    home.display_home(cosmic_icon=cosmic_img.resized_img)

    # Display window.
    app.mainloop()


if __name__ == "__main__":
    main()



