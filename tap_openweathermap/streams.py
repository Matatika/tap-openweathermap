"""Stream type classes for tap-openweathermap."""

from datetime import datetime
from typing import Any, Dict, Optional

from singer_sdk.streams import RESTStream

from tap_openweathermap.schemas.current_weather import CurrentWeatherObject
from tap_openweathermap.schemas.forecast_weather import ForecastWeatherObject


class _SyncedAtStream(RESTStream):
    """Define a synced at stream."""

    records_jsonpath = "$.[*]"

    synced_at = datetime.utcnow()

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """Apply synced at datetime to stream"""
        row = super().post_process(row, context)
        row["synced_at"] = self.synced_at
        return row


class _CurrentWeatherStream(_SyncedAtStream):
    """Define user top items stream."""

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["q"] = self.config["current_weather_city_name"]
        params["appid"] = self.config["api_key"]

        units = self.config.get("forecast_weather_units")
        if units:
            params["units"] = units

        return params


class _ForcastWeatherStream(_SyncedAtStream):
    """Define user top items stream."""

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        
        units = self.config.get("forecast_weather_units")
        if units:
            params["units"] = units
        
        params["lat"] = self.config["forecast_weather_lattitude"]
        params["lon"] = self.config["forecast_weather_longitude"]
        params["appid"] = self.config["api_key"]

        return params


class CurrentWeatherStream(_CurrentWeatherStream):
    """Define custom stream."""

    url_base = "https://api.openweathermap.org/data/2.5"
    name = "current_weather_stream"
    path = "/weather"
    schema = CurrentWeatherObject.to_dict()


class ForecastWeatherStream(_ForcastWeatherStream):
    """Define custom stream."""

    url_base = "https://api.openweathermap.org/data/3.0"
    name = "forecast_stream"
    path = "/onecall"
    extra_retry_statuses = ()
    schema = ForecastWeatherObject.to_dict()

    def response_error_message(self, response):
        return "\n".join(
            (
                super().response_error_message(response),
                response.json()["message"],
            )
        )
