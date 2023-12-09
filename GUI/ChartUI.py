import tkinter as tk
from datetime import date, timedelta
from tkinter import messagebox
from DataProcessing.Weather.WeatherDataProcessing import WeatherDataProcessing
from DataRetrieval.Weather.WeatherDataRetrieval import WeatherDataRetrieval
from GUI.ButtonCreation import ButtonCreation
from GUI.TitleBar import TitleBar
from GUI.ChartCreator import ChartCreator
from tkcalendar import Calendar
from tkinter import messagebox, Listbox


from tkinter import Toplevel
from datetime import datetime


class ChartUI(tk.Frame):
    def __init__(self, parent, menu_ui_instance, close_command):
        super().__init__(parent, bg='#D4D0C8')  # Set the background color
        self.menu_ui = menu_ui_instance
        self.root = parent

        self.title_bar = TitleBar(self.root, "", close_command, self.show_menu_ui)
        self.pack(fill="both", expand=True)

        self.chart_creator = ChartCreator(self, width=15, height=3, background_color='#D4D0C8')

        self.start_date_str = tk.StringVar()
        self.end_date_str = tk.StringVar()

        # Separate frames for each calendar
        self.from_cal_frame = tk.Frame(self)
        self.to_cal_frame = tk.Frame(self)

        # Create Entry widgets for dates
        self.from_date_entry = tk.Entry(self, textvariable=self.start_date_str)
        self.from_date_entry.pack(pady=10)
        self.from_date_entry.place(x=250, y=35)

        self.to_date_entry = tk.Entry(self, textvariable=self.end_date_str)
        self.to_date_entry.pack(pady=10)
        self.to_date_entry.place(x=250, y=80)

        # Calendar widget for selecting the start date
        self.from_cal = Calendar(self.from_cal_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.from_cal.pack()

        self.to_cal = Calendar(self.to_cal_frame, selectmode='day', date_pattern='yyyy-mm-dd')
        self.to_cal.pack()

        # Create Buttons that will show the calendar for date selection
        self.from_date_button = tk.Button(self, text='Select Start Date', command=self.popup_from_calendar)
        self.from_date_button.pack(pady=10)
        self.from_date_button.place(x=400, y=35)

        self.to_date_button = tk.Button(self, text='Select End Date', command=self.popup_to_calendar)
        self.to_date_button.pack(pady=10)
        self.to_date_button.place(x=400, y=80)

        # Create an instance of the ButtonCreation class for the generate button
        self.generate_graph_button = ButtonCreation(self)
        self.generate_graph_button.create_button(text="Generate Graph", bg_color='#c0c0c0', width=200, height=50)
        self.generate_graph_button.set_command(self.generate_graph_with_variable)
        self.generate_graph_button.place(x=990,y=10)

        # Call the create_boxes method and position it at the top-left corner
        self.create_boxes()

        # Add a Listbox for variable selection
        self.variable_selection = Listbox(self, selectmode="single")
        for variable in ["Temperature", "Precipitation", "Shortwave Radiation", "Terrestrial Radiation"]:
            self.variable_selection.insert(tk.END, variable)
        self.variable_selection.place(x=20, y=35)  # Adjust the position as needed

        self.from_cal.bind("<<CalendarSelected>>", lambda e: self.get_from_date())
        self.to_cal.bind("<<CalendarSelected>>", lambda e: self.get_to_date())

    def generate_graph_with_variable(self):
        selected_variable = self.variable_selection.get(self.variable_selection.curselection())
        if not selected_variable:
            messagebox.showinfo("Info", "Please select a variable.")
            return

        start_date = self.from_date_entry.get()
        end_date = self.to_date_entry.get()

        try:
            weather_data_retrieval = WeatherDataRetrieval("51.509865", "-0.118092", start_date, end_date)
            weather_data_json = weather_data_retrieval.fetch_data()
            weather_data = WeatherDataProcessing(weather_data_json)

            self.chart_creator.clear_graph()

            # Assuming the time starts at 00:00
            start_datetime = datetime.fromisoformat(start_date + "T00:00:00")
            # Assuming the end time is the end of the day
            end_datetime = datetime.fromisoformat(end_date + "T23:59:59")

            # Determine if the data is hourly or daily
            is_hourly_data = selected_variable in ["Shortwave Radiation", "Terrestrial Radiation"]

            if is_hourly_data:
                # Calculate the number of hours between start and end datetime for hourly data
                delta_hours = int((end_datetime - start_datetime).total_seconds() // 3600) + 1  # Include the last hour
                dates = [start_datetime + timedelta(hours=i) for i in range(delta_hours)]
            else:
                # Generate a list of dates for daily data
                delta_days = (end_datetime - start_datetime).days + 1
                dates = [start_datetime + timedelta(days=i) for i in range(delta_days)]

            print(f"Start datetime: {start_datetime}, End datetime: {end_datetime}, Dates generated: {len(dates)}")

            variable_methods = {
                "Temperature": weather_data.get_temperature_data_as_list,
                "Precipitation": weather_data.get_precipitation_data_as_list,
                "Shortwave Radiation": weather_data.get_shortwave_radiation_data_as_list,
                "Terrestrial Radiation": weather_data.get_terrestrial_radiation_data_as_list
            }

            if selected_variable in variable_methods:
                data = variable_methods[selected_variable]()
                print(f"Data length for {selected_variable}: {len(data)}")

                if len(data) != len(dates):
                    raise ValueError(f"Mismatched data lengths. Dates: {len(dates)}, Data: {len(data)}")

                self.chart_creator.plot_data(data, dates, selected_variable)
            else:
                messagebox.showerror("Error", f"No data retrieval method defined for {selected_variable}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            raise e  # Re-raise the exception for debugging purposes

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
        # Only toggle the from_cal_frame
        if self.from_cal_frame.winfo_ismapped():
            self.from_cal_frame.pack_forget()
        else:
            self.from_cal_frame.pack()
            self.to_cal_frame.pack_forget()  # Ensure the other calendar is hidden

    def popup_to_calendar(self):
        # Only toggle the to_cal_frame
        if self.to_cal_frame.winfo_ismapped():
            self.to_cal_frame.pack_forget()
        else:
            self.to_cal_frame.pack()
            self.from_cal_frame.pack_forget()  # Ensure the other calendar is hidden

    def get_from_date(self):
        # Update the start_date_str with the selected date and hide the calendar frame
        self.start_date_str.set(self.from_cal.get_date())
        self.from_cal_frame.pack_forget()

    def get_to_date(self):
        # Update the end_date_str with the selected date and hide the calendar frame
        self.end_date_str.set(self.to_cal.get_date())
        self.to_cal_frame.pack_forget()
