"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests

from tap_openweathermap.tap import TapOpenWeatherMap

SAMPLE_CONFIG = {
    "current_weather_city_name": "london",
    "forecast_weather_longitude": "-0.1257",
    "forecast_weather_lattitude": "51.5085",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapOpenWeatherMap, config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
