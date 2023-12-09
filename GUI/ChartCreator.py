import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
import tkinter as tk


class ChartCreator:
    def __init__(self, master, width, height, background_color='#D4D0C8'):
        self.master = master
        # Set the figsize to your desired dimensions
        self.figure = Figure(figsize=(width, height), dpi=100, facecolor= background_color)
        self.subplot = self.figure.add_subplot(111)

        # Set the face color for the subplot (axes) background
        self.subplot.set_facecolor(background_color)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.NONE, expand=False, pady=10)

    def plot_data(self, data, dates, variable_type, background_color='#D4D0C8'):
        # Clear the previous plot
        self.subplot.clear()
        self.subplot.set_facecolor(background_color)

        # Plot the data
        self.subplot.plot(dates, data, 'o-')  # 'o-' for a line plot with circles

        # Set the title for the plot
        self.subplot.set_title(variable_type)

        # Format the x-axis to show dates properly
        self.figure.autofmt_xdate()

        # Redraw the canvas
        self.canvas.draw()

    def clear_graph(self):
        self.subplot.clear()
        self.canvas.draw()
