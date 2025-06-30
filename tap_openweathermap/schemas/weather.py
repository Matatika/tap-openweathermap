from singer_sdk import typing as th

WeatherObject = th.PropertiesList(
    th.Property("id", th.NumberType),
    th.Property("main", th.StringType),
    th.Property("description", th.StringType),
    th.Property("icon", th.StringType),
)
