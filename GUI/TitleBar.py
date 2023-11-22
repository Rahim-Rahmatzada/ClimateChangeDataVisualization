import tkinter as tk
from GUI.ButtonCreation import ButtonCreation


class TitleBar(tk.Frame):
    def __init__(self, root, title, close_command, menu_command=None, bg='darkblue', fg='white'):
        super().__init__(root, bg=bg)
        self.root = root
        self.pack(side="top", fill="x")

        # Title label
        self.title_label = tk.Label(self, text=title, bg=bg, fg=fg)
        self.title_label.pack(side="left", padx=10)

        # Close button
        self.close_button_creator = ButtonCreation(self)
        self.close_button_creator.set_command(close_command)
        self.close_button_creator.create_button('X', '#c0c0c0', width=50, height=50)  # Add 'darkblue' as the bg color
        self.close_button_creator.pack(side="right", padx=10)

        # Menu button (if provided)
        if menu_command:
            self.menu_button_creator = ButtonCreation(self)
            self.menu_button_creator.set_command(menu_command)
            self.menu_button_creator.create_button('MENU', '#c0c0c0', width=100, height=50)  # Add 'darkblue' as the bg color
            self.menu_button_creator.pack(side="right", padx=10)

            # Window dragging functionality
        self.bind('<Button-1>', self.get_pos)
        self.bind('<B1-Motion>', self.move_window)

    def get_pos(self, event):
        self.xwin = event.x
        self.ywin = event.y

    def move_window(self, event):
        self.root.geometry(f'+{event.x_root - self.xwin}+{event.y_root - self.ywin}')
