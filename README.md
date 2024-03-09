# WeatherSDK

WeatherSDK is a Python package that allows you to retrieve weather information for different cities using the OpenWeatherMap API. It provides two modes of operation: on-demand and polling.

## Installation

You can install the WeatherSDK package using pip: 

    pip install weather_sdk

## Usage

To use WeatherSDK in your Python code, follow these steps:

1. Import the WeatherSDK class:


    from weathersdk import WeatherSDK


2. To use the WeatherSDK package, you need to get an API key from OpenWeatherMap. Visit the [OpenWeatherMap website](https://openweathermap.org/) and sign up to get your API key.
3. Initialize an instance of the WeatherSDK class with your API key and the desired mode:


    api_key = "<your-api-key>"
    mode = 'on_demand' or 'polling'
    sdk = WeatherSDK(api_key=api_key, mode=mode)


4. Retrieve weather data for a specific city using the 'get_weather' method:


    city = 'New York'
    weather_data = sdk.get_weather(city=city)
    print(weather_data)

5. Delete an SDK instance by removing its key from storage using the 'delete' method.


    sdk = WeatherSDK(api_key=api_key, mode=mode)
    sdk.delete()


## Modes of Operation

WeatherSDK supports two modes of operation:

### On-demand Mode

In on-demand mode, the SDK retrieves weather information for a specific city only when requested. It caches the data for subsequent requests within a 10-minute timeframe.

    sdk = WeatherSDK(api_key=api_key, mode="on_demand")
    weather_data = sdk.get_weather(city=city)

### Polling Mode

In polling mode, the SDK automatically updates the weather information for all saved cities at regular intervals. The data for each city are refreshed every 10 minutes.
In this mode, the city name does not need to be transmitted, since the data are taken from existing data.

    sdk = WeatherSDK(api_key=api_key, mode="polling")
    weather_data = sdk.get_weather()

### General example


    from weathersdk import WeatherSDK

    api_key = "<your-api-key>"

    city = 'London'
    mode_1 = 'on_demand'
    sdk = WeatherSDK(api_key=api_key, mode=mode_1)
    weather_data_london = sdk.get_weather(city=city)
    print(weather_data_london)

    '''
    {
    'weather': {
                'main': 'Clouds', 
                'description': 
                'overcast clouds'
                }, 
    'temperature': {
                    'temp': 282.46, 
                    'feels_like': 280.78
                    }, 
    'visibility': 10000, 
    'wind': {
            'speed': 3.09
            }, 
    'datetime': 1710019683, 
    'sys': {
            'sunrise': 1709965652, 
            'sunset': 1710006877
            }, 
    'timezone': 0, 
    'name': 'London',
    }
    '''


    mode_2 = 'polling'
    sdk_2 = WeatherSDK(api_key=api_key, mode=mode_2)
    weather_data_all_city = sdk_2.get_weather()
    print(weather_data_all_city)
    
    '''
    {
    'London': {
                'data': {
                        'weather': {
                                    'main': 'Clouds', 
                                    'description': 
                                    'overcast clouds'}, 
                        'temperature': {
                                        'temp': 282.46, 
                                        'feels_like': 280.78
                                        }, 
                        'visibility': 10000, 
                        'wind': {
                                'speed': 3.09
                                }, 
                        'datetime': 1710019683, 
                        'sys': {
                                'sunrise': 1709965652, 
                                'sunset': 1710006877
                                }, 
                        'timezone': 0, 
                        'name': 'London',
                        }
                }
    }
    '''

    sdk.delete()
    sdk_2.delete()


## Documentation

For detailed documentation, including information about methods and parameters, refer to the [WeatherSDK Documentation](link-to-documentation).
