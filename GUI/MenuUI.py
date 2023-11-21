import tkinter as tk
from GUI.ButtonCreation import ButtonCreation
from GUI.ChartUI import ChartUI


class MenuUI:
    def __init__(self, root):
        self.root = root
        # self.root.overrideredirect(True)
        self.create_custom_titlebar("")

        self.root.configure(bg='#D4D0C8')
        self.root.geometry("1200x700")

        self.create_rectangle_frame()  # Define rectangle_frame before using it
        self.create_dark_blue_rectangle()  # Now rectangle_frame is defined, we can use it here

        self.create_button_frame()
        self.create_buttons()

    def create_custom_titlebar(self, title):
        title_bar = tk.Frame(self.root, bg='darkblue', relief='raised', bd=2)
        title_bar.pack(side="top", fill="x")
        title_label = tk.Label(title_bar, text=title, bg='darkblue', fg='white')
        title_label.pack(side="left", padx=10)

        # Assuming create_button is a method from ButtonCreation class that creates a button
        # Here we're creating a new ButtonCreation instance just for the close button
        close_button_creator = ButtonCreation(title_bar)
        # Setting command for close button to destroy the window
        close_button_creator.set_command(self.root.destroy)
        # Now we use the create_button method to create the close button
        close_button_creator.create_button('X', width=50, height=50)  # Width and height in text units
        close_button_creator.pack(side="right", padx=10)

        # Allow the window to be moved by dragging the title bar
        title_bar.bind('<Button-1>', self.get_pos)
        title_bar.bind('<B1-Motion>', self.move_window)

    def get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def move_window(self, event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')

    def create_button_frame(self):
        self.button_frame = tk.Frame(self.root, bg='#D4D0C8')
        self.button_frame.place(relx=0.5, rely=0.6, anchor='center')

    def create_buttons(self):
        button_specs = [("GRAPHS", 250, 100), ("PIE CHARTS", 250, 100), ("MAPS", 250, 100)]
        for text, width, height in button_specs:
            button = ButtonCreation(self.button_frame)
            if text == "GRAPHS":
                button.set_command(self.show_graph_ui)  # Set the command for the GRAPHS button
            else:
                button.set_command(self.on_button_click)  # You can define different commands for each button
            button.create_button(text, width, height)
            button.pack(pady=10)

    def show_graph_ui(self):
        # This method gets called when the GRAPHS button is clicked
        # It will create an instance of the ChartUI class
        ChartUI(self.root)  # Pass the root window as the parent of ChartUI

    def create_rectangle_frame(self):
        self.rectangle_frame = tk.Frame(self.root, bg='#D4D0C8')
        self.rectangle_frame.place(relx=0.5, rely=0.25, anchor='center')

    def create_dark_blue_rectangle(self):
        # This should be inside the rectangle_frame, not the button_frame
        rectangle = ButtonCreation(self.rectangle_frame)
        rectangle.create_dark_blue_rectangle("DATA VISUALIZATION", 500, 80)
        rectangle.pack(pady=10)

    def on_button_click(self):
        # Placeholder for other buttons' commands
        print("Another button clicked")
