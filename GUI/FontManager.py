import tkinter as tk
from tkinter import font as tkFont
import os


class FontManager:
    """
    A class for managing and loading custom fonts.
    It provides methods to load a custom font from a file and retrieve the loaded font.
    """

    # Class variable to store the custom font
    custom_font = None

    @classmethod
    def load_custom_font(cls, font_folder, font_filename, size):
        # First, we register the custom font with the system
        font_path = os.path.join(os.path.dirname(__file__), font_folder, font_filename)

        # We assume that 'w-95-sans-serif.ttf' is a TrueType font file
        # Now we create a font object using the tkFont library
        cls.custom_font = tkFont.Font(family="w-95-sans-serif", size=size)

        # Here you can register the font with tkinter if necessary
        # This step depends on how you plan to use the font within your application

    @classmethod
    def get_custom_font(cls):
        # Return the custom font
        if cls.custom_font is None:
            raise ValueError("Custom font has not been loaded.")
        return cls.custom_font
