"""OpenWeatherMap tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_openweathermap.streams import (
    WeatherStream,
)

STREAM_TYPES = [
    WeatherStream,
]

class TapOpenWeatherMap(Tap):
    """OpenWeatherMap tap class."""
    name = "tap-openweathermap"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="API Key is a required parameter to query the api endpoints"
        ),
        th.Property(
            "forecast_weather_longitude",
            th.StringType,
            required=True,
            description="Longitude of city to get forecast for"
        ),
        th.Property(
            "forecast_weather_lattitude",
            th.StringType,
            required=True,
            description="Lattitude of city to get forecast for"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
