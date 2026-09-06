def generate_alerts(weather):
    alerts = []
    daily = weather["daily"]
    current = weather["current"]
    days_to_check = min(2, len(daily["time"]))
    for i in range(days_to_check):
        date = daily["time"][i]
        max_temp = daily["temperature_2m_max"][i]
        rain = daily["precipitation_probability_max"][i]
        code = daily["weather_code"][i]
        wind = current["wind_speed_10m"]
        # 🔥 Heatwave
        if max_temp >= 40:
            alerts.append({
                "severity":"High",
                "type":"Heatwave",
                "icon":"🔥",
                "date":date,
                "title":"Heatwave Warning",
                "message":f"Temperature may reach {max_temp}°C.",
                "recommendation":[
                    "Water crops before sunrise.",
                    "Increase irrigation.",
                    "Avoid fertilizer application.",
                    "Protect livestock from direct sunlight."
                ]
            })
        # 🌧 Heavy Rain
        if rain >= 90 and code in [63, 65, 81, 82]:
            alerts.append({
                "severity":"Medium",
                "type":"Heavy Rain",
                "icon":"🌧",
                "date":date,
                "title":"Heavy Rain Warning",
                "message":f"Rain probability is {rain}%",
                "recommendation":[
                    "Harvest mature crops.",
                    "Improve field drainage.",
                    "Protect stored grains."
                ]
            })
        # 💨 Strong Wind
        if wind >= 35:
            alerts.append({
                "severity":"Medium",
                "type":"Strong Wind",
                "icon":"💨",
                "date":date,
                "title":"Strong Wind Warning",
                "message":f"Wind speed may reach {wind} km/h.",
                "recommendation":[
                    "Support young plants.",
                    "Delay pesticide spraying."
                ]
            })
        # ⛈ Thunderstorm
        if code in [95, 96, 99]:
            alerts.append({
                "severity":"High",
                "type":"Thunderstorm",
                "icon":"⛈",
                "date":date,
                "title":"Thunderstorm Warning",
                "message":"Thunderstorm expected.",
                "recommendation":[
                    "Avoid field work.",
                    "Protect farm equipment.",
                    "Stay indoors during lightning."
                ]
            })
    # ===== DEMO MODE =====
# If no alerts, Add demo alerts for demonstration purposes , Comment this demo part if wanna check real-life alerts
        alerts = [
            {
                "severity": "High",
                "type": "Heatwave",
                "icon": "🔥",
                "date": daily["time"][0],
                "title": "Heatwave Warning",
                "message": "Demo Alert: Temperature may reach 42°C.",
                "recommendation": [
                    "Water crops before sunrise.",
                    "Increase irrigation.",
                    "Avoid fertilizer application."
                ]
            },
            {
                "severity": "Medium",
                "type": "Heavy Rain",
                "icon": "🌧",
                "date": daily["time"][1],
                "title": "Heavy Rain Warning",
                "message": "Demo Alert: Heavy rainfall expected tomorrow.",
                "recommendation": [
                    "Harvest mature crops.",
                    "Improve field drainage.",
                    "Protect stored grains."
                ]
            }
            ]
        return alerts