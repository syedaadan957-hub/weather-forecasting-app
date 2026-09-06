from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .weather_api import get_weather
from .alerts_ai import generate_alerts
from .farming_ai import generate_farming_tips
import json

def home(request):
    return render(request, "home.html")

def location(request):
    return render(request, "location.html")

def current_weather(request):
    return render(request, "weather.html")

def forecast(request):
    return render(request, "forecast.html")

def alerts(request):
    return render(request, "alerts.html")

def farming(request):
    return render(request, "farming.html")

@csrf_exempt
def weather(request):
    if request.method == "POST":
        body = json.loads(request.body)
        latitude = body["latitude"]
        longitude = body["longitude"]
        data = get_weather(latitude, longitude)
        return JsonResponse(data)
@csrf_exempt
def alerts_api(request):
    if request.method == "POST":
        body = json.loads(request.body)
        lat = body["latitude"]
        lon = body["longitude"]
        weather = get_weather(lat, lon)
        alerts = generate_alerts(weather)
        return JsonResponse({
            "alerts": alerts,
            "count": len(alerts)
        })
@csrf_exempt
def farming_api(request):
    if request.method == "POST":
        body = json.loads(request.body)
        latitude = body["latitude"]
        longitude = body["longitude"]
        weather = get_weather(latitude, longitude)
        crop = body["crop"]
        tips = generate_farming_tips(weather, crop)
        return JsonResponse({
            "tips": tips
        })