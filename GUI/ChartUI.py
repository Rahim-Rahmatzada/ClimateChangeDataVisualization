import tkinter as tk
from GUI.ButtonCreation import ButtonCreation
from GUI.TitleBar import TitleBar


class ChartUI(tk.Frame):
    def __init__(self, parent, menu_ui_instance, close_command):
        super().__init__(parent, bg='#D4D0C8')  # Set the background color
        self.menu_ui = menu_ui_instance
        self.root = parent

        self.title_bar = TitleBar(self.root, "", close_command, self.show_menu_ui)
        self.pack(fill="both", expand=True)

    def show_menu_ui(self):
        self.title_bar.destroy()  # Destroy the ChartUI's title bar
        self.pack_forget()  # Hide the ChartUI
        self.menu_ui.show_menu_ui()
