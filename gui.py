# TODO: Create a gui for the program

# imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os


# class block
class GUI:
    """This class implements gui for the image watermarking app"""

    def __init__(self):
        """Init gui when instance is created"""
        # root initialization
        self.root = Tk()
        self.root.title("Watermarking App")
        self.root.resizable(width=True, height=True)
        self.root.filename = None
        # self.root.iconbitmap("")

        # frame as a placeholder for the image
        self.image_frame = ttk.Frame(self.root, padding=10, borderwidth=2)
        self.image_frame.grid(column=0, row=0, columnspan=3, pady=10, padx=10, sticky=E + W)

        # buttons definition
        self.upload_button = ttk.Button(self.root, text="Upload Image", command=self.open_image)
        self.upload_button.grid(column=0, row=1, pady=10, padx=10)

        self.save_button = ttk.Button(self.root, text="Save the Image", command=lambda: self.display_watermarked_image())
        self.save_button.grid(column=2, row=1, pady=10, padx=10)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.grid(column=1, row=1, pady=10, padx=10)

        # root mainloop
        self.root.mainloop()

    def open_image(self):
        """Uploads am image to the GUI interface using tkinter.filedialog"""
        # for some reason(i really don't know why) it only works, if i make image global
        global image

        # get an image path
        self.root.filename = filedialog.askopenfilename(initialdir=f"{os.getcwd()}",
                                                        title="Upload Image",
                                                        filetypes=(("png files", "*.png"),
                                                                   ("jpeg files", "*.jpeg"),
                                                                   ("jpg files", "*.jpg")))

        # put the image into a label
        # image = ImageTk.PhotoImage(Image.open(self.root.filename).resize((450, 350), Image.ANTIALIAS))
        # label_for_the_image = ttk.Label(self.image_frame, image=image)
        # label_for_the_image.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

    def display_watermarked_image(self, image_path):
        """When the image is watermarked, this function displays it"""
        # create a global(again for some reason)
        global watermarked_image

        # open it up
        watermarked_image = ImageTk.PhotoImage(Image.open(image_path))

        # display the image
        label_for_the_watermarked_image = ttk.Label(self.image_frame, image=watermarked_image)
        label_for_the_watermarked_image.grid(column=0, row=0, columnspan=3, pady=10, padx=10, sticky=E+W)

