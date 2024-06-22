import tkinter as tk
from GUI.ButtonCreation import ButtonCreation
from GUI.ChartUI import ChartUI
from GUI.TitleBar import TitleBar


class MenuUI(tk.Frame):
    """
    A user interface class representing the main menu.
    It creates and arranges various UI components such as buttons and rectangles.
    The class inherits from tk.Frame and uses instances of ButtonCreation and TitleBar.
    """

    def __init__(self, root, close_command):
        super().__init__(root, bg='#D4D0C8')
        self.root = root
        self.title_bar = TitleBar(self.root, "", close_command)

        self.root.geometry("1200x700")

        self.create_rectangle_frame()  # Define rectangle_frame before using it
        self.create_dark_blue_rectangle()  # Now rectangle_frame is defined, we can use it here

        self.create_button_frame()
        self.create_buttons()

        self.pack(fill='both', expand=True)

    def create_button_frame(self):
        self.button_frame = tk.Frame(self.root, bg='#D4D0C8')
        self.button_frame.place(relx=0.5, rely=0.6, anchor='center')

    def create_buttons(self):
        button_specs = [
            ("GRAPHS", '#c0c0c0', 250, 100),
            ("PIE CHARTS", '#c0c0c0', 250, 100),
            ("MAPS", '#c0c0c0', 250, 100)
        ]
        for text, bg_color, width, height in button_specs:
            button = ButtonCreation(self.button_frame)
            button.create_button(text, bg_color, width, height)  # Correct order of arguments
            button.pack(pady=10)
            # Set the command for each button
            if text == "GRAPHS":
                button.set_command(self.show_graph_ui)
            elif text == "PIE CHARTS":  # You might want to add specific commands for each button
                button.set_command(self.on_button_click)  # Placeholder for actual command
            elif text == "MAPS":
                button.set_command(self.on_button_click)  # Placeholder for actual command

    def show_graph_ui(self):
        self.title_bar.destroy()  # Destroy the current title bar
        self.pack_forget()  # Hide the MenuUI frame
        self.chart_ui = ChartUI(self.root, self, self.root.destroy)
        self.chart_ui.pack(fill='both', expand=True)

    def show_menu_ui(self):
        # Destroy any existing title bar and chart UI before recreating the menu UI
        if hasattr(self, 'title_bar'):
            self.title_bar.destroy()
        if hasattr(self, 'chart_ui'):
            self.chart_ui.destroy()

        # Recreate the title bar for the menu UI
        self.title_bar = TitleBar(self.root, "", self.root.destroy)
        self.title_bar.pack(side="top", fill="x")  # Make sure to pack the title bar

        self.pack(fill='both', expand=True)
        # Recreate the menu UI components as necessary

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
