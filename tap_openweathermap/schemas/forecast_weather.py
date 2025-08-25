from singer_sdk import typing as th

from tap_openweathermap.schemas.weather import WeatherObject

ForecastWeatherObject = th.PropertiesList(
    th.Property("synced_at", th.DateTimeType),
    th.Property("location_name", th.StringType),
    th.Property("lat", th.NumberType),
    th.Property("lon", th.NumberType),
    th.Property("timezone", th.StringType),
    th.Property("timezone_offset", th.NumberType),
    th.Property(
        "current",
        th.ObjectType(
            th.Property("dt", th.NumberType),
            th.Property("sunrise", th.NumberType),
            th.Property("sunset", th.NumberType),
            th.Property("temp", th.NumberType),
            th.Property("feels_like", th.NumberType),
            th.Property("pressure", th.NumberType),
            th.Property("humidity", th.NumberType),
            th.Property("dew_point", th.NumberType),
            th.Property("uvi", th.NumberType),
            th.Property("clouds", th.NumberType),
            th.Property("visibility", th.NumberType),
            th.Property("wind_speed", th.NumberType),
            th.Property("wind_deg", th.NumberType),
            th.Property("wind_gust", th.NumberType),
            th.Property("weather", th.ArrayType(WeatherObject)),
        ),
    ),
    th.Property(
        "minutely",
        th.ArrayType(
            th.ObjectType(
                th.Property("dt", th.NumberType),
                th.Property("precipitation", th.NumberType),
            )
        ),
    ),
    th.Property(
        "hourly",
        th.ArrayType(
            th.ObjectType(
                th.Property("dt", th.NumberType),
                th.Property("temp", th.NumberType),
                th.Property("feels_like", th.NumberType),
                th.Property("pressure", th.NumberType),
                th.Property("humidity", th.NumberType),
                th.Property("dew_point", th.NumberType),
                th.Property("uvi", th.NumberType),
                th.Property("clouds", th.NumberType),
                th.Property("visibility", th.NumberType),
                th.Property("wind_speed", th.NumberType),
                th.Property("wind_deg", th.NumberType),
                th.Property("wind_gust", th.NumberType),
                th.Property("weather", th.ArrayType(WeatherObject)),
                th.Property("pop", th.NumberType),
            )
        ),
    ),
    th.Property(
        "daily",
        th.ArrayType(
            th.ObjectType(
                th.Property("dt", th.NumberType),
                th.Property("sunrise", th.NumberType),
                th.Property("sunset", th.NumberType),
                th.Property("moonrise", th.NumberType),
                th.Property("moonset", th.NumberType),
                th.Property("moonphase", th.NumberType),
                th.Property("summary", th.StringType),
                th.Property(
                    "temp",
                    th.ObjectType(
                        th.Property("day", th.NumberType),
                        th.Property("min", th.NumberType),
                        th.Property("max", th.NumberType),
                        th.Property("night", th.NumberType),
                        th.Property("eve", th.NumberType),
                        th.Property("morn", th.NumberType),
                    ),
                ),
                th.Property(
                    "feels_like",
                    th.ObjectType(
                        th.Property("day", th.NumberType),
                        th.Property("night", th.NumberType),
                        th.Property("eve", th.NumberType),
                        th.Property("morn", th.NumberType),
                    ),
                ),
                th.Property("pressure", th.NumberType),
                th.Property("humidity", th.NumberType),
                th.Property("dew_point", th.NumberType),
                th.Property("wind_speed", th.NumberType),
                th.Property("wind_deg", th.NumberType),
                th.Property("wind_gust", th.NumberType),
                th.Property("weather", th.ArrayType(WeatherObject)),
                th.Property("clouds", th.NumberType),
                th.Property("pop", th.NumberType),
                th.Property("rain", th.NumberType),
                th.Property("uvi", th.NumberType),
            )
        ),
    ),
    th.Property(
        "alerts",
        th.ArrayType(
            th.ObjectType(
                th.Property("sender_name", th.StringType),
                th.Property("event", th.StringType),
                th.Property("start", th.NumberType),
                th.Property("end", th.NumberType),
                th.Property("description", th.StringType),
                th.Property("tags", th.ArrayType(th.StringType)),
            )
        ),
    ),
)
