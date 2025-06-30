from singer_sdk.typing import (
    PropertiesList,
    Property,
    ArrayType,
    NumberType,
    StringType,
)

from tap_openweathermap.schemas.utils.custom_object import CustomObject


class WeatherObject(CustomObject):
    properties = ArrayType(
        PropertiesList(
            Property("id", NumberType),
            Property("main", StringType),
            Property("description", StringType),
            Property("icon", StringType),
        )
    )
