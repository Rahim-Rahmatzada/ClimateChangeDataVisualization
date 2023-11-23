import tkinter as tk
from tkinter import font as tkFont
from PIL import ImageFont, Image
import os


class ButtonCreation(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg='black', **kwargs)
        self.custom_font = self.load_custom_font('Fonts', 'w-95-sans-serif.ttf', 12)

        self.command = None  # Add a command attribute to store the button's action

        # self.bind('<Enter>', self.on_hover)
        # self.bind('<Leave>', self.on_leave)

    def load_custom_font(self, font_folder, font_filename, size):
        # First, we register the custom font with the system

        font_path = os.path.join(os.path.dirname(__file__), 'Fonts', 'w-95-sans-serif.ttf')

        ImageFont.truetype(font_path, size=size)

        font_name = os.path.splitext('pix M 8pt')[0]
        return tkFont.Font(family=font_name, size=size)

    # self.custom_font = tkFont.Font(family='pix M 8pt', size=12)

    def create_button(self, text, bg_color, width, height):
        # Using the width and height parameters for button size
        # inner_frame = tk.Frame(self, bg='#c0c0c0', width=width, height=height)
        inner_frame = tk.Frame(self, bg=bg_color, width=width, height=height)

        inner_frame.pack_propagate(False)
        inner_frame.pack(expand=True, fill='both', padx=2, pady=2)

        white = '#ffffff'
        black = '#000000'

        self.left_border = tk.Frame(inner_frame, bg=white, width=2)
        self.left_border.pack(side='left', fill='y')

        self.right_border = tk.Frame(inner_frame, bg=black, width=2)
        self.right_border.pack(side='right', fill='y')

        self.top_border = tk.Frame(inner_frame, bg=white, height=2)
        self.top_border.pack(side='top', fill='x')

        self.bottom_border = tk.Frame(inner_frame, bg=black, height=2)
        self.bottom_border.pack(side='bottom', fill='x')

        # self.text_label = tk.Label(inner_frame, text=text, bg='#c0c0c0', fg='black', font=self.custom_font)
        self.text_label = tk.Label(inner_frame, text=text, bg=bg_color, fg='black', font=self.custom_font)
        self.text_label.pack(expand=True, fill='both', padx=10, pady=5)

        self.bind('<Enter>', self.on_hover)  # Bind the hover event
        self.bind('<Leave>', self.on_leave)  # Bind the leave event

        self.bind('<Button-1>', self.on_click)
        self.text_label.bind('<Button-1>', self.on_click)

    def on_hover(self, event):
        # Lighten the button's background color to simulate a translucent overlay
        self.configure(bg='#6699FF')  # A lighter shade of blue for hover effect

    def on_leave(self, event):
        # Revert the button's background color to its original state
        self.configure(bg='black')

    def create_dark_blue_rectangle(self, text, width, height):
        # Create a frame for the rectangle with the specified width and height
        rectangle_frame = tk.Frame(self, bg='dark blue', width=width, height=height)
        rectangle_frame.pack_propagate(False)  # Prevents the frame from shrinking to fit its contents
        rectangle_frame.pack(expand=True, fill='both')  # Expand the frame to fill the space allocated to it

        # Add a label with some text, using the same custom font
        label = tk.Label(rectangle_frame, text=text, bg='dark blue', fg='white', font=self.custom_font)
        label.pack(expand=True, fill='both', padx=10, pady=5)  # Center the label in the rectangle frame

    def on_click(self, event):
        if self.command:
            self.command()

    def create_boxes(self, bg_color, width, height):
        # Create a frame for the box with the specified width and height
        box_frame = tk.Frame(self, bg=bg_color, width=width, height=height)
        box_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        box_frame.pack(expand=True, fill='both', padx=2, pady=2)

        # Bevel effect
        left_border = tk.Frame(box_frame, bg='white', width=2)
        left_border.pack(side='left', fill='y')

        right_border = tk.Frame(box_frame, bg='black', width=2)
        right_border.pack(side='right', fill='y')

        top_border = tk.Frame(box_frame, bg='white', height=2)
        top_border.pack(side='top', fill='x')

        bottom_border = tk.Frame(box_frame, bg='black', height=2)
        bottom_border.pack(side='bottom', fill='x')

    def set_command(self, command):
        self.command = command
