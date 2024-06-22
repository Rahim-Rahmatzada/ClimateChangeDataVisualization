# Climate Data Visualization

This project is a Python-based application for visualizing climate data retrieved from the Open-Meteo API. It provides a graphical user interface (GUI) that allows users to select date ranges and variables to generate interactive charts and graphs.

## Features

- Retrieves climate data from the Open-Meteo API based on latitude, longitude, start date, and end date
- Processes the retrieved data and extracts relevant fields such as temperature, precipitation, shortwave radiation, and terrestrial radiation
- Provides a user-friendly GUI built with Tkinter for selecting date ranges and variables
- Generates interactive line plots and bar charts using Matplotlib to visualize the selected climate data
- Supports customization of chart titles, axis labels, and plot styles
- Implements a custom button creation class for creating stylized buttons with hover effects
- Utilizes a custom font manager for loading and using custom fonts throughout the application
- Includes a custom title bar class for window dragging functionality and close/menu buttons

## Prerequisites

To run this project, you need to have the following dependencies installed:

- Python 3.x
- Tkinter
- Matplotlib
- Requests

You can install the required Python packages using pip

## Getting Started

1. Clone the repository

2. Navigate to the project directory

3. Run Main.py

## File Structure

- `main.py`: The main entry point of the application.
- `GUI/MenuUI.py`: Contains the `MenuUI` class for creating the main menu user interface.
- `GUI/ChartUI.py`: Contains the `ChartUI` class for creating the chart user interface.
- `GUI/ButtonCreation.py`: Contains the `ButtonCreation` class for creating custom buttons.
- `GUI/TitleBar.py`: Contains the `TitleBar` class for creating a custom title bar.
- `GUI/FontManager.py`: Contains the `FontManager` class for loading and managing custom fonts.
- `DataRetrieval/WeatherDataRetrieval.py`: Contains the `WeatherDataRetrieval` class for retrieving weather data from the API.
- `DataProcessing/WeatherDataProcessing.py`: Contains the `WeatherDataProcessing` class for processing the retrieved weather data.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for providing the weather data API.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Matplotlib](https://matplotlib.org/) for the data visualization library.