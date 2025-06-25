"""Stream type classes for tap-openweathermap."""

from datetime import datetime
from typing import Optional
from urllib.parse import parse_qsl, urlsplit

from singer_sdk.typing import (
    PropertiesList,
    Property,
    NumberType,
    StringType,
    DateTimeType,
)
from singer_sdk.streams import RESTStream

from tap_openweathermap.schemas.weather import WeatherObject
from tap_openweathermap.schemas.forecast_weather import (
        ForecastCurrentObject,
        ForecastMinutelyObject,
        ForecastHourlyObject,
        ForecastDailyObject,
)

from tap_openweathermap.schemas.current_weather import (
        CurrentWeatherCoordObject,
        CurrentWeatherCloudsObject,
        CurrentWeatherMainObject,
        CurrentWeatherRainObject,
        CurrentWeatherSysObject,
        CurrentWeatherWindObject,
)


class _SyncedAtStream(RESTStream):
    """Define a synced at stream."""

    records_jsonpath = "$.[*]"

    synced_at = datetime.utcnow()

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """Apply synced at datetime to stream"""
        row = super().post_process(row, context)
        row["synced_at"] = self.synced_at
        return row


class CurrentWeatherStream(_SyncedAtStream):
    """Define custom stream."""
    url_base = "https://api.openweathermap.org/data/2.5"
    name = "current_weather_stream"
    path = "/weather"

    schema = PropertiesList(
        Property("synced_at", DateTimeType),
        Property("coord", CurrentWeatherCoordObject),
        Property("weather", WeatherObject),
        Property("base", StringType),
        Property("main", CurrentWeatherMainObject),
        Property("visibility", NumberType),
        Property("wind", CurrentWeatherWindObject),
        Property("rain", CurrentWeatherRainObject),
        Property("clouds", CurrentWeatherCloudsObject),
        Property("dt", NumberType),
        Property("sys", CurrentWeatherSysObject),
        Property("timezone", NumberType),
        Property("id", NumberType),
        Property("name", StringType),
        Property("cod", NumberType),
        ).to_dict()

    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        params["appid"] = self.config["api_key"]

        if city_name := self.config.get("current_weather_city_name"):
            params["q"] = city_name
        else:
            params["lat"] = self.config["forecast_weather_lattitude"]
            params["lon"] = self.config["forecast_weather_longitude"]

        return params


class ForecastWeatherStream(_SyncedAtStream):
    """Define custom stream."""
    url_base = "https://api.openweathermap.org/data/3.0"
    name = "forecast_stream"
    path = "/onecall"
    extra_retry_statuses = ()
    schema = PropertiesList(
        Property("synced_at", DateTimeType),
        Property("lat", NumberType),
        Property("lon", NumberType),
        Property("timezone", StringType),
        Property("timezone_offset", NumberType),
        Property("current", ForecastCurrentObject),
        Property("minutely", ForecastMinutelyObject),
        Property("hourly", ForecastHourlyObject),
        Property("daily", ForecastDailyObject)
    ).to_dict()

    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        params["appid"] = self.config["api_key"]
        params["lat"] = self.config["forecast_weather_lattitude"]
        params["lon"] = self.config["forecast_weather_longitude"]

        return params

    def response_error_message(self, response):
        return "\n".join(
            (
                super().response_error_message(response),
                response.json()["message"],
            )
        )