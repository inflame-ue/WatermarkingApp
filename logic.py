# TODO: Create a gui for the program

# imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from constants import *
import os

# global variable for the watermarked_image
watermarked_image = None


# class block
class WatermarkingApp:
    """This class implements functionality for the image watermarking app"""

    def __init__(self):
        """Init gui when instance is created"""
        # some variables for the gui
        self.path_for_watermarked_image = None
        self.image = None
        self.image_name = None
        self.watermark_name = None
        self.image_extension = None
        self.image_filename = None

        # root initialization
        self.root = Tk()
        self.root.title("Watermarking App")
        self.root.resizable(width=True, height=True)
        self.root.iconbitmap("assets/icons/play.ico")

        # style for the application
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # main frame
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=N+E+W+S)

        # frame as a placeholder for the image
        self.image_frame = ttk.Frame(self.mainframe, padding=10, borderwidth=2)
        self.image_frame.grid(column=0, row=0, columnspan=3, pady=10, padx=10, sticky=E + W)

        # buttons definition
        self.upload_button = ttk.Button(self.mainframe, text="Upload Image", command=self.open_image)
        self.upload_button.grid(column=0, row=1, pady=10, padx=10)

        self.watermark_button = ttk.Button(self.mainframe, text="Watermark", command=self.create_a_watermark)
        self.watermark_button.grid(column=1, row=1, pady=10, padx=10)

        self.display_button = ttk.Button(self.mainframe, text="Display", command=self.display_watermarked_image)
        self.display_button.grid(column=2, row=1, pady=10, padx=10)

        self.exit_button = ttk.Button(self.mainframe, text="Exit", command=self.root.quit)
        self.exit_button.grid(column=1, row=2, pady=10, padx=10)

        # root mainloop
        self.root.mainloop()

    def open_image(self):
        """Uploads am image to the GUI interface using tkinter.filedialog"""
        # get an image path
        self.image_name = filedialog.askopenfilename(initialdir=f"{os.getcwd()}",
                                                     title="Upload Image",
                                                     filetypes=(("png files", "*.png"),
                                                                ("jpeg files", "*.jpeg"),
                                                                ("jpg files", "*.jpg")))

    def display_watermarked_image(self):
        """When the image is watermarked, this function displays it"""
        global watermarked_image

        try:
            # open it up
            watermarked_image = ImageTk.PhotoImage(
                Image.open(self.path_for_watermarked_image).resize((1200, 800), Image.ANTIALIAS))
        except AttributeError:
            # give an error message box to the user, if user tries to display the image without uploading it
            messagebox.showerror("No Such Image",
                                 "Image wasn't uploaded or it doesn't exist in the specified directory.")

        # display the image
        label_for_the_watermarked_image = ttk.Label(self.image_frame, image=watermarked_image)
        label_for_the_watermarked_image.grid(column=0, row=0, columnspan=3, pady=10, padx=10, sticky=E + W)

    def create_a_watermark(self):
        """
        This method puts a watermark on the image.
        :return: nothing to return
        """
        # images and information needed for watermarking
        self.image = Image.open(self.image_name)
        self.image_filename = os.path.splitext(self.image_name)[0].split("/")[-1]
        self.image_extension = os.path.splitext(self.image_name)[1]

        # copy an image, doing this to not mess up any important images
        copied_image = self.image.copy()

        # draw a text watermark on it
        draw = ImageDraw.ImageDraw(copied_image)
        watermark_font = ImageFont.truetype("arial.ttf", 50)
        draw.text((0, 0), 'watermark', (255, 255, 255), font=watermark_font)

        # return the path for the image
        self.path_for_watermarked_image = f"{SAVE_DIRECTORY}//{self.image_filename}." \
                                          f"{'jpeg' if self.image_extension == 'jpeg' else 'png'}"

        # save the image to the save directory specified by the user
        copied_image.save(self.path_for_watermarked_image)

        # tel the use that image was saved successfully
        messagebox.showinfo(title="Success", message="Watermarked Image was saved successfully")
