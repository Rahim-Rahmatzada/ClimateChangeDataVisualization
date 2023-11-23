import tkinter as tk
from datetime import date
from tkinter import messagebox
from DataProcessing.Weather.WeatherDataProcessing import WeatherDataProcessing
from DataRetrieval.Weather.WeatherDataRetrieval import WeatherDataRetrieval
from GUI.ButtonCreation import ButtonCreation
from GUI.TitleBar import TitleBar
from GUI.ChartCreator import ChartCreator
from tkcalendar import Calendar
from tkinter import Toplevel


class ChartUI(tk.Frame):
    def __init__(self, parent, menu_ui_instance, close_command):
        super().__init__(parent, bg='#D4D0C8')  # Set the background color
        self.menu_ui = menu_ui_instance
        self.root = parent

        self.title_bar = TitleBar(self.root, "", close_command, self.show_menu_ui)
        self.pack(fill="both", expand=True)

        self.chart_creator = ChartCreator(self, width=15, height=3, background_color='#D4D0C8')

        self.from_date_button = tk.Button(self, text='Select Start Date', command=self.popup_from_calendar)
        self.from_date_button.pack(pady=10)
        self.to_date_button = tk.Button(self, text='Select End Date', command=self.popup_to_calendar)
        self.to_date_button.pack(pady=10)

        self.from_date_label = tk.Label(self, text='Start Date: None')
        self.from_date_label.pack(pady=10)
        self.to_date_label = tk.Label(self, text='End Date: None')
        self.to_date_label.pack(pady=10)

        # Create an instance of the ButtonCreation class for the generate button
        self.generate_graph_button = ButtonCreation(self)
        self.generate_graph_button.create_button(text="Generate Graph", bg_color='#c0c0c0', width=200, height=50)
        self.generate_graph_button.set_command(self.generate_graph)  # Set the command for the button
        self.generate_graph_button.pack(pady=10)  # Pack the button with some vertical padding

        # Call the create_boxes method and position it at the top-left corner
        self.create_boxes()

    def generate_graph(self):
        # Convert input to date
        start_date = self.from_date_input.get()
        end_date = self.to_date_input.get()

        try:
            # Fetch and process weather data
            weather_data_retrieval = WeatherDataRetrieval("51.509865", "-0.118092", start_date, end_date)
            weather_data_json = weather_data_retrieval.fetch_data()
            weather_data = WeatherDataProcessing(weather_data_json)

            temperature_data = weather_data.get_temperature_data_as_list()
            date_range = range(date.fromisoformat(start_date).toordinal(), date.fromisoformat(end_date).toordinal() + 1)

            # Check if the data lists are empty or have different lengths
            if not temperature_data or not date_range or len(temperature_data) != len(date_range):
                messagebox.showerror("Error", "The temperature data and date range must have the same number of elements and cannot be empty.")
                return

            # Plot the data
            self.chart_creator.plot_data(temperature_data, date_range, "Temperature", background_color='#D4D0C8')

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def create_boxes(self):
        # Assuming that the dimensions and bg_color are given
        box_width = 200
        box_height = 300
        bg_color = 'white'
        bevel_box = ButtonCreation(self)
        bevel_box.create_boxes(bg_color, box_width, box_height)
        bevel_box.place(x=25, y=25)  # Top-left corner

    def show_menu_ui(self):
        self.title_bar.destroy()  # Destroy the ChartUI's title bar
        self.pack_forget()  # Hide the ChartUI
        self.menu_ui.show_menu_ui()

    def popup_from_calendar(self):
        self.from_cal_window = Toplevel(self)
        self.from_cal = Calendar(self.from_cal_window, selectmode='day', date_pattern='y-mm-dd')
        self.from_cal.pack()
        tk.Button(self.from_cal_window, text="Ok", command=self.get_from_date).pack()

    def popup_to_calendar(self):
        self.to_cal_window = Toplevel(self)
        self.to_cal = Calendar(self.to_cal_window, selectmode='day', date_pattern='y-mm-dd')
        self.to_cal.pack()
        tk.Button(self.to_cal_window, text="Ok", command=self.get_to_date).pack()

    def get_from_date(self):
        self.from_date_label.config(text=f"Start Date: {self.from_cal.get_date()}")
        self.from_cal_window.destroy()

    def get_to_date(self):
        self.to_date_label.config(text=f"End Date: {self.to_cal.get_date()}")
        self.to_cal_window.destroy()
