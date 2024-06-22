import tkinter as tk
from GUI.MenuUI import MenuUI
from GUI.FontManager import FontManager


class MainUI:
    """
    The main user interface class that manages the overall application window and its components.
    It creates instances of MenuUI and ChartUI, and handles the switching between them.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x700")

        # Initialize MenuUI and ChartUI without creating a TitleBar inside them
        self.menu_ui = MenuUI(self.root, self.close_application)

        # Start with showing the MenuUI
        self.menu_ui.pack(fill='both', expand=True)

        # Additional setup can go here...
        FontManager.load_custom_font('Fonts', 'w-95-sans-serif.ttf', 12)

        self.root.mainloop()

    def close_application(self):
        self.root.destroy()


# Running the MainUI if the script is executed
if __name__ == "__main__":
    app = MainUI()
