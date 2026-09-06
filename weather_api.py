import requests
def get_weather(latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,"
        "wind_speed_10m,precipitation,cloud_cover,"
        "weather_code"
        "&daily=temperature_2m_max,temperature_2m_min,"
        "precipitation_probability_max,weather_code"
        "&forecast_days=10"
        "&timezone=auto"
    )
    response = requests.get(url)
    return response.json()