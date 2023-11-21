import tkinter as tk

class ChartUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Add widgets for the graph display here
        self.label = tk.Label(self, text="This is where the graph will be displayed.")
        self.label.pack(pady=20)

        # Add a back button to return to the main menu
        self.back_button = tk.Button(self, text="Back to Menu", command=self.show_menu_ui)
        self.back_button.pack(pady=20)

    def show_menu_ui(self):
        self.pack_forget()  # Hide the ChartUI
        self.show_menu_ui()  # Show the MenuUI