import logging
import time

import requests

logger = logging.getLogger("weather_sdk")


class WeatherSDK:
    instances = {}  # Dictionary for storing SDK instances by keys
    weather_data = {}  # Dictionary for storing weather data for different cities

    def __init__(self, key: str, api_key: str, mode: str):
        """
        Initialize an instance of the WeatherSDK class.

        Args:
            key (str): SDK Instance Key.
            api_key (str): The API key for accessing weather data.
            mode (str): The mode of operation for the SDK, can be 'on_demand' or 'polling'.

        """
        if key in WeatherSDK.instances:
            raise ValueError("An SDK instance with the specified key already exists.")

        self._key = key  # Key to create an instance
        self._api_key = api_key  # Your API key from OpenWeatherMap
        self._mode = mode  # SDK operation mode

        WeatherSDK.instances[key] = self  # Adding an SDK instance to the dictionary by key


    def get_weather(self, city: str = None) -> dict:
        """
        Get weather data for the specified city.

        Args:
            city (str): The city name.

        Returns:
            dict: Weather information for the specified city.

        Raises:
            ValueError: If invalid city name provided.
        """
        if city is not None:
            if not isinstance(city, str) or len(city) == 0:
                raise ValueError("Invalid city name provided.")

        if self._mode == "on_demand":
            return self._handle_on_demand_mode(city)

        elif self._mode == "polling":
            self._update_weather_data()
            return WeatherSDK.weather_data

    def delete(self):
        """
        Deletes an SDK instance by removing its key from storage.
        """
        del WeatherSDK.instances[self._key]


    def _handle_on_demand_mode(self, city: str) -> dict:
        """
        Handle the 'on_demand' mode.

        Args:
            city (str): The city name.

        Returns:
            dict: Weather information for the specified city.
        """
        if city in WeatherSDK.weather_data and (time.time() - WeatherSDK.weather_data[city]["data"]["datetime"]) < 600:
            return WeatherSDK.weather_data[city]["data"]

        result = self._get_data_weather(city=city, api_key=self._api_key)
        if city not in WeatherSDK.weather_data:
            if len(self.weather_data) < 10:
                WeatherSDK.weather_data[result["name"]] = {"data": result}
        else:
            WeatherSDK.weather_data[result["name"]] = {"data": result}

        return result

    def _update_weather_data(self):
        """
        Update weather data for all saved cities in 'polling' mode.
        """
        for city_in_dict in WeatherSDK.weather_data:
            if (time.time() - WeatherSDK.weather_data[city_in_dict]["data"]["datetime"]) >= 600:
                result = self._get_data_weather(city=city_in_dict, api_key=self._api_key)
                WeatherSDK.weather_data[city_in_dict]["data"] = result

    @staticmethod
    def _get_data_weather(city: str, api_key: str) -> dict:
        """
        Retrieves weather data for a specified city using the API.

        Args:
            city (str): City name.
            api_key (str): API key to access weather data.

        Returns:
            dict: Weather information for the specified city.

        Raises:
            requests.exceptions.HTTPError: If an HTTP error occurs during the request.
            requests.exceptions.RequestException: If an error occurs while executing the request.
        """
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
            response.raise_for_status()
            data = response.json()
            all_data = {
                "weather": {
                    "main": data["weather"][0]["main"],
                    "description": data["weather"][0]["description"]
                },
                "temperature": {
                    "temp": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"]
                },
                "visibility": data["visibility"],
                "wind": {
                    "speed": data["wind"]["speed"]
                },
                "datetime": data["dt"],
                "sys": {
                    "sunrise": data["sys"]["sunrise"],
                    "sunset": data["sys"]["sunset"]
                },
                "timezone": data["timezone"],
                "name": data["name"]
            }
            return all_data

        except requests.exceptions.HTTPError as http_err:
            logger.error("An HTTP error occurred during the request: %s", http_err)
            raise requests.exceptions.HTTPError("An HTTP error occurred during the request.") from http_err
        except requests.exceptions.RequestException as ex:
            logger.error("An error occurred while executing the request: %s", str(ex))
            raise requests.exceptions.RequestException("An error occurred while executing the request.") from ex


