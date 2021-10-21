from singer_sdk.typing import (
    PropertiesList,
    Property,
    ArrayType,
    NumberType,
)

from tap_openweathermap.schemas.utils.custom_object import CustomObject
from tap_openweathermap.schemas.weather import WeatherObject

class ForecastCurrentObject(CustomObject):

    properties = PropertiesList(
        Property("dt", NumberType),
        Property("sunrise", NumberType),
        Property("sunset", NumberType),
        Property("temp", NumberType),
        Property("feels_like", NumberType),
        Property("pressure", NumberType),
        Property("humidity", NumberType),
        Property("dew_point", NumberType),
        Property("uvi", NumberType),
        Property("clouds", NumberType),
        Property("visibility", NumberType),
        Property("wind_speed", NumberType),
        Property("wind_deg", NumberType),
        Property("wind_gust", NumberType),
        Property("weather", WeatherObject)
    )


class ForecastMinutelyObject(CustomObject):

    properties = ArrayType(PropertiesList(
        Property("dt", NumberType),
        Property("precipitation", NumberType))
    )


class ForecastHourlyObject(CustomObject):

    properties = ArrayType(PropertiesList(
        Property("dt", NumberType),
        Property("temp", NumberType),
        Property("feels_like", NumberType),
        Property("pressure", NumberType),
        Property("humidity", NumberType),
        Property("dew_point", NumberType),
        Property("uvi", NumberType),
        Property("clouds", NumberType),
        Property("visibility", NumberType),
        Property("wind_speed", NumberType),
        Property("wind_deg", NumberType),
        Property("wind_gust", NumberType),
        Property("weather", WeatherObject),
        Property("pop", NumberType))
    )


class ForecastTempObject(CustomObject):

    properties = PropertiesList(
        Property("day", NumberType),
        Property("min", NumberType),
        Property("max", NumberType),
        Property("night", NumberType),
        Property("eve", NumberType),
        Property("morn", NumberType)
    )


class ForecastFeelsLikeObject(CustomObject):

    properties = PropertiesList(
        Property("day", NumberType),
        Property("night", NumberType),
        Property("eve", NumberType),
        Property("morn", NumberType)
    )


class ForecastDailyObject(CustomObject):

    properties = ArrayType(PropertiesList(
        Property("dt", NumberType),
        Property("sunrise", NumberType),
        Property("sunset", NumberType),
        Property("moonrise", NumberType),
        Property("moonset", NumberType),
        Property("moonphase", NumberType),
        Property("temp", ForecastTempObject),
        Property("feels_like", ForecastFeelsLikeObject),
        Property("pressure", NumberType),
        Property("humidity", NumberType),
        Property("dew_point", NumberType),
        Property("wind_speed", NumberType),
        Property("wind_deg", NumberType),
        Property("wind_gust", NumberType),
        Property("weather", WeatherObject),
        Property("clouds", NumberType),
        Property("pop", NumberType),
        Property("rain", NumberType),
        Property("uvi", NumberType))
    )
