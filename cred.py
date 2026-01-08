import os

from dotenv import load_dotenv

# Loading environment variable
load_dotenv()

# Getting gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

# Getting weather api key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")

# Getting mem0 api key
MEM0_API_KEY = os.getenv("MEM0_API_KEY", "")

if not gemini_api_key:
    raise EnvironmentError("Gemini API Key is not found!")

if not WEATHER_API_KEY:
    raise EnvironmentError("Weather API Key not found!")

if not MEM0_API_KEY:
    raise EnvironmentError("Mem0 API Key not found!")

USER_ID = "assigned_user"