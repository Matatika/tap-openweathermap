from singer_sdk.typing import (
    PropertiesList,
    Property,
    NumberType,
    StringType,
)

from tap_openweathermap.schemas.utils.custom_object import CustomObject


class CurrentWeatherCoordObject(CustomObject):

    properties = PropertiesList(
        Property("lon", NumberType),
        Property("lat", NumberType)
    )


class CurrentWeatherMainObject(CustomObject):

    properties = PropertiesList(
        Property("temp", NumberType),
        Property("feels_like", NumberType),
        Property("temp_min", NumberType),
        Property("temp_max", NumberType),
        Property("pressure", NumberType),
        Property("humidity", NumberType)
    )


class CurrentWeatherWindObject(CustomObject):

    properties = PropertiesList(
        Property("speed", NumberType),
        Property("deg", NumberType),
        Property("gust", NumberType)
    )


class CurrentWeatherRainObject(CustomObject):

    properties = PropertiesList(
        Property("1h", NumberType)
    )


class CurrentWeatherCloudsObject(CustomObject):

    properties = PropertiesList(
        Property("all", NumberType)
    )


class CurrentWeatherSysObject(CustomObject):

    properties = PropertiesList(
        Property("type", NumberType),
        Property("id", NumberType),
        Property("country", StringType),
        Property("sunrise", NumberType),
        Property("sunset", NumberType)
    )

