import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
import tkinter as tk
from matplotlib.animation import FuncAnimation


class ChartCreator:
    """
    A class responsible for creating and animating charts using Matplotlib.
    It provides methods to animate line plots and bar charts with given data and labels.
    """

    def __init__(self, master, width, height, background_color='#D4D0C8'):
        self.master = master
        # Set the figsize to your desired dimensions
        self.figure = Figure(figsize=(width, height), dpi=100, facecolor= background_color)
        self.subplot = self.figure.add_subplot(111)

        # Set the face color for the subplot (axes) background
        self.subplot.set_facecolor(background_color)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.NONE, expand=False, pady=(10, 10))

        self.animation = None

    def animate_plot_data(self, data, dates, variable_type, x_label='Date', y_label='Value'):
        # Stop the previous animation if it's running
        if self.animation:
            self.animation.event_source.stop()
            self.animation = None

        # Clear the previous plot
        self.subplot.clear()

        # Initialize a line object on the plot, this will be updated by the animation function
        line, = self.subplot.plot([], [], color='#00008B')  # Use plot instead of plot_date

        # Function to initialize the plot's frame
        def init():
            # Set the initial limits and labels for the plot
            self.subplot.set_xlim(dates[0], dates[-1])
            self.subplot.set_ylim(min(data), max(data))
            self.subplot.set_xlabel(x_label)
            self.subplot.set_ylabel(y_label)
            self.subplot.grid(False)  # Optional: Add a grid for better readability
            return line,

        # Function to update the plot's frame
        def update(frame):
            # Update the line data for each frame
            line.set_data(dates[:frame + 1], data[:frame + 1])
            return line,

        # Create the animation
        self.animation = FuncAnimation(
            self.figure, update, init_func=init,
            frames=len(data), interval=100, blit=False, repeat=False
        )

        # Set the title and format the x-axis
        self.subplot.set_title(variable_type)
        self.figure.autofmt_xdate() 
        

        # Start the animation
        self.canvas.draw()

        # Function to call when the animation is done
        def on_animation_complete(i):
            self.animation = None

        # Attach the completion function to the animation event
        self.animation._on_repeat = on_animation_complete

    def animate_plot_bar_data(self, data, dates, variable_type, x_label='Date', y_label='Value'):
        # Check if an animation is in progress and avoid clearing the subplot
        if self.animation is not None:
            return

        # Clear the previous plot
        self.subplot.clear()

        # Set the title for the plot
        self.subplot.set_title(variable_type)

        # This will contain the bars of the bar chart
        bars = self.subplot.bar(dates, [0]*len(data), color='#00008B')  # Start with bars of height 0

        def init():
            self.subplot.set_xlim(dates[0], dates[-1])
            self.subplot.set_ylim(0, max(data))
            # Label the axes
            self.subplot.set_xlabel(x_label)
            self.subplot.set_ylabel(y_label)
            return bars

        def update(frame):
            # This function will be called for each new frame.
            # Update the height of the bars
            for bar, new_height in zip(bars, data[:frame]):
                bar.set_height(new_height)
            return bars

        # Create the animation
        self.animation = FuncAnimation(
            self.figure, update, init_func=init,
            frames=len(data), interval=100, blit=True, repeat=False
        )

        # Start the animation
        self.canvas.draw()

    def clear_graph(self):
        # Check if there is an animation running before trying to stop it
        if self.animation:
            if self.animation.event_source:
                self.animation.event_source.stop()
            self.animation = None

        # Clear the subplot
        self.subplot.clear()
        # Redraw the canvas after clearing
        self.canvas.draw()

