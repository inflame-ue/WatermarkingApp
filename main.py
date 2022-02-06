# TODO: Create a watermaking image desktop app using a GUI library and Pillow

# imports
from logic import Watermark
from gui import GUI

# initialization
if __name__ == "__main__":
    # initializing the application
    gui = GUI()
    watermark = Watermark(gui.root.filename, "assets/watermarks/original.png")

    # manipulate the image
    watermark.create_a_watermark((200, 200))

