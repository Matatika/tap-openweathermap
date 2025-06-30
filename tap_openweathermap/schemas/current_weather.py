from singer_sdk import typing as th

from tap_openweathermap.schemas.weather import WeatherObject

CurrentWeatherObject = th.PropertiesList(
    th.Property("synced_at", th.DateTimeType),
    th.Property(
        "coord",
        th.ObjectType(
            th.Property("lon", th.NumberType),
            th.Property("lat", th.NumberType),
        ),
    ),
    th.Property("weather", th.ArrayType(WeatherObject)),
    th.Property("base", th.StringType),
    th.Property(
        "main",
        th.ObjectType(
            th.Property("temp", th.NumberType),
            th.Property("feels_like", th.NumberType),
            th.Property("temp_min", th.NumberType),
            th.Property("temp_max", th.NumberType),
            th.Property("pressure", th.NumberType),
            th.Property("humidity", th.NumberType),
        ),
    ),
    th.Property("visibility", th.NumberType),
    th.Property(
        "wind",
        th.ObjectType(
            th.Property("speed", th.NumberType),
            th.Property("deg", th.NumberType),
            th.Property("gust", th.NumberType),
        ),
    ),
    th.Property(
        "rain",
        th.ObjectType(
            th.Property("1h", th.NumberType),
        ),
    ),
    th.Property(
        "clouds",
        th.ObjectType(
            th.Property("all", th.NumberType),
        ),
    ),
    th.Property("dt", th.NumberType),
    th.Property(
        "sys",
        th.ObjectType(
            th.Property("type", th.NumberType),
            th.Property("id", th.NumberType),
            th.Property("country", th.StringType),
            th.Property("sunrise", th.NumberType),
            th.Property("sunset", th.NumberType),
        ),
    ),
    th.Property("timezone", th.NumberType),
    th.Property("id", th.NumberType),
    th.Property("name", th.StringType),
    th.Property("cod", th.NumberType),
)
