import unittest
from weather_sdk import WeatherSDK

api_key = "apy_key_openweathermap"


class WeatherSDKTests(unittest.TestCase):
    def test_instances(self):
        """
        Test the creation and deletion of SDK instances.
        """
        sdk_test = WeatherSDK(key="asd", api_key=api_key, mode="on_demand")
        sdk_test_2 = WeatherSDK(key="qwe", api_key=api_key, mode="on_demand")
        self.assertIn("asd", WeatherSDK.instances)
        self.assertIn("qwe", WeatherSDK.instances)

        sdk_test.delete()
        self.assertNotIn("asd", WeatherSDK.instances)
        self.assertIn("qwe", WeatherSDK.instances)

        sdk_test_2.delete()
        self.assertNotIn("qwe", WeatherSDK.instances)


    def test_get_weather(self):
        """
        Test the 'get_weather' method of WeatherSDK.
        """
        sdk_test = WeatherSDK(key="dfg", api_key=api_key, mode="on_demand")

        # Test for invalid city name
        with self.assertRaises(ValueError):
            sdk_test.get_weather(city=123)
            sdk_test.get_weather()

        # Test for valid city name
        result = sdk_test.get_weather(city="Minsk")
        self.assertEqual(result["name"], "Minsk")
        self.assertEqual(result["timezone"], 10800)

        # Test for polling mode
        sdk_test_polling = WeatherSDK(key="qwe", api_key=api_key, mode="polling")
        result_polling = sdk_test_polling.get_weather()

        self.assertEqual(result_polling["Minsk"]["data"]["name"], "Minsk")
        self.assertEqual(result_polling["Minsk"]["data"]["timezone"], 10800)

        sdk_test.delete()
        sdk_test_polling.delete()


if __name__ == '__main__':
    unittest.main()
