DEMO_MODE = True  # Set to False for real-life weather data
def generate_farming_tips(weather, crop):
    tips = []
    current = weather["current"]
    daily = weather["daily"]
    temp = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    rain = daily["precipitation_probability_max"][0]
    crop = crop.lower()
    # ==========================
    # WHEAT
    # ==========================
    if DEMO_MODE:
        crop = crop.lower()
        if crop == "wheat":
            return [
                {
                    "title":"🌾 Wheat Recommendation",
                    "message":"Today's weather is hot. Irrigate wheat before sunrise and avoid fertilizer application."
                },
                {
                    "title":"🌧 Rain Alert",
                    "message":"Rain is expected tomorrow. Improve field drainage."
                }
            ]
        elif crop == "rice":
            return [
                {
                    "title":"🌾 Rice Recommendation",
                    "message":"Maintain 5–7 cm water level in the paddy field."
                },
                {
                    "title":"💧 Irrigation",
                    "message":"Reduce irrigation because rainfall is expected."
                }
            ]
        elif crop == "maize":
            return [
                {
                    "title":"🌽 Maize Recommendation",
                    "message":"Support young maize plants due to strong winds."
                },
                {
                    "title":"☀ Heat Stress",
                    "message":"Water maize early in the morning."
                }
            ]
        elif crop == "cotton":
            return [
                {
                    "title":"🌱 Cotton Recommendation",
                    "message":"High humidity may increase pest attacks. Inspect your crop today."
                },
                {
                    "title":"🧪 Spraying",
                    "message":"Delay pesticide spraying until evening."
                }
            ]
        elif crop == "tomato":
            return [
                {
                    "title":"🍅 Tomato Recommendation",
                    "message":"Avoid overhead irrigation to reduce fungal diseases."
                },
                {
                    "title":"🔥 Heat Protection",
                    "message":"Provide shade during peak afternoon temperatures."
                }
            ]
        elif crop == "potato":
            return [
                {
                    "title":"🥔 Potato Recommendation",
                    "message":"Maintain soil moisture for healthy tuber development."
                },
                {
                    "title":"🌱 Soil Care",
                    "message":"Remove weeds around potato plants."
                }
            ]
        elif crop == "mango":
            return [
                {
                    "title":"🥭 Mango Recommendation",
                    "message":"Harvest ripe mangoes before tomorrow's rain."
                },
                {
                    "title":"💨 Wind Alert",
                    "message":"Support weak branches to prevent damage."
                }
            ]
    #===========================
    # REAL-LIFE
    #===========================
    if crop == "wheat":
        if temp >= 35:
            tips.append({
                "title": "🌾 Wheat - Heat Stress",
                "message": "High temperatures may reduce wheat yield. Irrigate during early morning and avoid fertilizer application today."
            })
        if rain >= 60:
            tips.append({
                "title": "🌧 Wheat - Rain Alert",
                "message": "Heavy rainfall may cause waterlogging. Improve field drainage and harvest mature wheat if possible."
            })
    # ==========================
    # RICE
    # ==========================
    elif crop == "rice":
        if temp >= 35:
            tips.append({
                "title": "🌾 Rice",
                "message": "Maintain sufficient water level in paddy fields during hot weather."
            })
        if rain >= 70:
            tips.append({
                "title": "🌧 Rice",
                "message": "Reduce irrigation because rainfall will provide enough water."
            })
    # ==========================
    # MAIZE
    # ==========================
    elif crop == "maize":
        if temp >= 34:
            tips.append({
                "title": "🌽 Maize",
                "message": "Water maize early in the morning to reduce heat stress."
            })
        if wind >= 25:
            tips.append({
                "title": "💨 Maize",
                "message": "Support young maize plants against strong winds."
            })
    # ==========================
    # COTTON
    # ==========================
    elif crop == "cotton":
        if humidity >= 80:
            tips.append({
                "title": "🌱 Cotton",
                "message": "High humidity increases pest and fungal risks. Inspect crops carefully."
            })
        if rain >= 70:
            tips.append({
                "title": "🌧 Cotton",
                "message": "Delay pesticide spraying until rainfall has passed."
            })
    # ==========================
    # TOMATO
    # ==========================
    elif crop == "tomato":
        if humidity >= 75:
            tips.append({
                "title": "🍅 Tomato",
                "message": "High humidity may cause fungal diseases. Avoid overhead irrigation."
            })
        if temp >= 35:
            tips.append({
                "title": "🔥 Tomato",
                "message": "Provide shade if possible and irrigate during cooler hours."
            })
    # ==========================
    # POTATO
    # ==========================
    elif crop == "potato":
        if temp >= 32:
            tips.append({
                "title": "🥔 Potato",
                "message": "High temperatures may reduce tuber quality. Maintain soil moisture."
            })
    # ==========================
    # MANGO
    # ==========================
    elif crop == "mango":
        if wind >= 30:
            tips.append({
                "title": "🥭 Mango",
                "message": "Strong winds may damage branches. Harvest ripe fruits early."
            })
        if rain >= 70:
            tips.append({
                "title": "🌧 Mango",
                "message": "Ensure good drainage around mango trees."
            })
    # ==========================
    # General Advice
    # ==========================
    if len(tips) == 0:
        tips.append({
            "title": "✅ Good Farming Conditions",
            "message": f"Current weather is favorable for {crop.title()} farming. Continue routine farming activities."
        })
    return tips