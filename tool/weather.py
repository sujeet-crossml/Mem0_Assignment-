"""
Weather Tool using OpenWeatherMap API
"""

import requests
from logs import setup_logger

from langchain.tools import tool

from cred import WEATHER_API_KEY


logger = setup_logger()

@tool
def get_weather(city: str) -> dict:
    """
    Summary:
        Retrieve current weather information for a given city.

    Args:
        city (str): Name of the city to fetch weather data for.

    Returns:
        dict: Dictionary containing temperature and weather condition,
              or an error message if the request fails.
    """
    
    """
    Fetches live weather data for a city.
    """
    logger.info(f"Fetching weather for: {city}")
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()
        result = {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
        logger.info(f"Weather result: {result}")
        return result
    except Exception as e:
        logger.error(f"Weather API error: {e}")
        return {"error": str(e)}
