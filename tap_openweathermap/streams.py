"""Stream type classes for tap-openweathermap."""

from datetime import datetime
from typing import Any, Dict, Optional
from urllib.parse import parse_qsl, urlsplit

from singer_sdk.typing import (
    PropertiesList,
    Property,
    NumberType,
    StringType,
    DateTimeType,
)
from singer_sdk.streams import RESTStream

from tap_openweathermap.schemas.forecast_weather import (
        ForecastCurrentObject,
        ForecastMinutelyObject,
        ForecastHourlyObject,
        ForecastDailyObject,
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


class WeatherStream(_SyncedAtStream):
    """Define custom stream."""
    url_base = "https://api.openweathermap.org/data/3.0"
    name = "weather_stream"
    path = "/onecall"

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

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["lat"] = self.config.get("weather_lattitude")
        params["lon"] = self.config.get("weather_longitude")
        params["appid"] = self.config.get("api_key")

        return params