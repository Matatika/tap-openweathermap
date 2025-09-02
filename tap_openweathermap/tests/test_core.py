"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_tap_test_class

from tap_openweathermap.tap import TapOpenWeatherMap

SAMPLE_CONFIG = {
    "current_weather_city_name": "london",
    "forecast_weather_longitude": "-0.1257",
    "forecast_weather_lattitude": "51.5085",
}


# Run standard built-in tap tests from the SDK:
TestTapFeefo = get_tap_test_class(
    tap_class=TapOpenWeatherMap,
    config=SAMPLE_CONFIG,
)
