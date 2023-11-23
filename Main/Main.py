import tkinter as tk
from GUI.MenuUI import MenuUI


class MainUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x700")

        # Initialize MenuUI and ChartUI without creating a TitleBar inside them
        self.menu_ui = MenuUI(self.root, self.close_application)

        # Start with showing the MenuUI
        self.menu_ui.pack(fill='both', expand=True)

        # Additional setup can go here...

        self.root.mainloop()

    def close_application(self):
        self.root.destroy()


# Running the MainUI if the script is executed
if __name__ == "__main__":
    app = MainUI()
