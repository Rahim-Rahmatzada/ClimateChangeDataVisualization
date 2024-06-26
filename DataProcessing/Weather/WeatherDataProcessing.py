import json


class WeatherDataProcessing:
    """
    A class for processing weather data obtained from the API response.
    It parses the JSON response and extracts the relevant data fields.
    The class provides methods to retrieve the data as lists of floats or access the raw JSON arrays.
    """

    def __init__(self, api_response):
        # Parse the JSON response
        obj = json.loads(api_response)
        daily = obj['daily']
        self.temperature_data = daily['temperature_2m_mean']
        self.precipitation_data = daily['precipitation_sum']

        hourly = obj['hourly']
        self.shortwave_radiation_data = hourly['shortwave_radiation']
        self.terrestrial_radiation_data = hourly['terrestrial_radiation']

    def get_temperature_data_as_list(self):
        return self._json_array_to_list(self.temperature_data)

    def get_precipitation_data_as_list(self):
        return self._json_array_to_list(self.precipitation_data)

    def get_shortwave_radiation_data_as_list(self):
        return self._json_array_to_list(self.shortwave_radiation_data)

    def get_terrestrial_radiation_data_as_list(self):
        return self._json_array_to_list(self.terrestrial_radiation_data)

    def _json_array_to_list(self, json_array):
        # Convert JSON array to a list of doubles (floats in Python)
        return [float(val) if val is not None else 0.0 for val in json_array]

    # If you need to retrieve the raw JSON arrays, you can add the following methods:
    def get_temperature_data(self):
        return self.temperature_data

    def get_precipitation_data(self):
        return self.precipitation_data

    def get_shortwave_radiation_data(self):
        return self.shortwave_radiation_data

    def get_terrestrial_radiation_data(self):
        return self.terrestrial_radiation_data



