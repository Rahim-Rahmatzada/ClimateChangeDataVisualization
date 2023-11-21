from GUI.MenuUI import MenuUI
import tkinter as tk


class MainUI:

    def __init__(self):
        # Initialize the main application window
        self.root = tk.Tk()


        # Initialize MenuUI
        self.menu_ui = MenuUI(self.root)  # Pass the main application window to the MenuUI

        # Additional setup can go here...

        # Start the GUI loop
        self.root.mainloop()


# Running the MainUI if the script is executed
if __name__ == "__main__":
    app = MainUI()