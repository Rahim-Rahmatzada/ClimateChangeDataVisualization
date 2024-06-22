import requests


class WeatherDataRetrieval:
    """
    A class for retrieving weather data from the Open-Meteo API.
    It constructs the API URL based on the provided latitude, longitude, start date, and end date.
    The class fetches the data from the API and returns the response as text.
    """

    BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

    def __init__(self, latitude, longitude, start_date, end_date):
        self.latitude = latitude
        self.longitude = longitude
        self.start_date = start_date
        self.end_date = end_date

    def build_url(self):
        # Constructs the query parameters string
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "hourly": "shortwave_radiation,terrestrial_radiation",
            "daily": "temperature_2m_mean,precipitation_sum",
            "timezone": "Europe/London"
        }
        # Builds the full URL for the request
        return f"{self.BASE_URL}?{'&'.join(f'{key}={value}' for key, value in params.items())}"

    def fetch_data(self):
        # Fetches the data from the API
        built_url = self.build_url()
        response = requests.get(built_url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.text


# # Example usage:
# weather_retrieval = WeatherDataRetrieval("51.509865", "-0.118092", "2021-09-01", "2021-09-10")
# try:
#     data = weather_retrieval.fetch_data()
#     print(data)
# except Exception as e:
#     print(f"An error occurred: {e}")
