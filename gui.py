# TODO: Create a gui for the programm

# imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class GUI:
    """This class implements gui for the image watermarking app"""

    def __init__(self):
        """Init gui when instance created"""
        # root initialization
        self.root = Tk()
        self.root.title("Watermarking App")
        self.root.minsize(640, 400)
        self.root.resizable(width=True, height=True)

        # frame widget - holds the contents of the gui
        self.mainframe = ttk.Frame(self.root, padding="9 9 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # button for uploading an image
        self.upload_image_button = ttk.Button(self.mainframe, )


        # main loop
        self.root.mainloop()


