import requests

from config.settings import (
    OPENWEATHER_API_KEY,
    OPENWEATHER_BASE_URL,
)


def get_weather(city: str) -> dict:
    """
    Fetch current weather information for a city.
    """

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(
            OPENWEATHER_BASE_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return {
            "success": True,
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }

    except requests.exceptions.HTTPError:
        return {
            "success": False,
            "error": "City not found or invalid API key.",
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": str(error),
        }