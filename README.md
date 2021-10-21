# tap-openweathermap

`tap-openweathermap` is a Singer tap for OpenWeatherMap.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
pipx install tap-openweathermap
```

## Configuration

#### Expected Env Vars
```bash
TAP_OPENWEATHERMAP_API_KEY=1234567890
TAP_OPENWEATHERMAP_CURRENT_WEATHER_CITY_NAME=london
TAP_OPENWEATHERMAP_FORECAST_WEATHER_LONGITUDE=-0.1257
TAP_OPENWEATHERMAP_FORECAST_WEATHER_LATTITUDE=51.5085
```

`api_key` is required for authentication, see the "Source Authentication and Authorization" section for how to get one.

`current_weather_city_name` is required, and the api will return current weather data for the supplied city name.

`forecast_weather_longitude` is required, you need to provide this to get forecast data.

`forecast_weather_lattitude` is required, you need to provide this to get forecast data.

You can get the longitude and lattitude of a city by requesting its current weather, setting the city name to the `current_weather_city_name` setting.
The longitude and lattidue will be returned as part of the current_weather_stream. To get the values for your first call just google "city_name" coords.
 
### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the tap.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-openweathermap --about
```

### Source Authentication and Authorization

To use this tap you require an API key from [https://openweathermap.org/])(https://openweathermap.org/). 

Sign up for a free account and under your profile you will find your default API Key.

The API Key is required to be passed as a parameter to the API the authenticate your request.

## Usage

You can easily run `tap-openweathermap` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-openweathermap --version
tap-openweathermap --help
tap-openweathermap --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_openweathermap/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-openweathermap` CLI interface directly using `poetry run`:

```bash
poetry run tap-openweathermap --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-openweathermap
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-openweathermap --version
# OR run a test `elt` pipeline:
meltano elt tap-openweathermap target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
