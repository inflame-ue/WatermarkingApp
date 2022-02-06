# TODO: Create a watermark logic for the program

# imports
import os
import concurrent.futures
import time
from PIL import Image, ImageFilter
from constants import *


# classes block
class Watermark:
    """This class implements watermarking capabilities of the watermarking app"""

    def __init__(self, image_filename, watermark_filename):
        """
        Loads up the image from the directory.
        :param image_filename: If image is in the current working directory just specify the name, otherwise specify the full
        path.
        """
        self.image = Image.open(image_filename)
        self.watermark = Image.open(watermark_filename)
        self.image_filename = os.path.splitext(image_filename)[0].split("/")[2]
        self.image_extension = os.path.splitext(image_filename)[1]
        self.watermark_filename = os.path.splitext(watermark_filename)[0].split("/")[2]

        # resize watermark image
        self.watermark.thumbnail((500, 500))

    def __repr__(self):
        return f"Watermark({self.image_filename}, {self.watermark_filename})"

    def __str__(self):
        return self.image_filename

    def create_a_watermark(self, coordinates: tuple):
        """
        This method puts a watermark on the image.
        :param coordinates: x and y, that will specify where to place the watermark
        :return: nothing to return
        """
        # copy an image, doing this to not mess up any important images
        copied_image = self.image.copy()
        copied_image.paste(self.watermark, coordinates)  # merge watermark with the copied image
        copied_image.save(f"{SAVE_DIRECTORY}/{self.image_filename}.{'jpeg' if self.image_extension == 'jpeg' else 'png'}")
