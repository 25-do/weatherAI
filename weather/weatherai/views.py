from django.shortcuts import render
from . import services

def get_outdoor_advice(weather_data):
    """Generate outdoor advice based on weather data."""
    if not weather_data:
        return "Could not retrieve weather data."

    current = weather_data.get('current', {})
    condition = current.get('condition_code', '').lower()
    temperature = current.get('temperature')

    if 'rain' in condition:
        return "No, rain expected. Stay indoors."
    
    if temperature is not None and temperature > 30:
        return "Hot weather. Stay hydrated."

    return "Good conditions for outdoor activities."


def index(request):
    """
    Main view for the weather dashboard.
    - Fetches and displays weather.
    - Provides an outdoor activity recommendation.
    """
    api_key = request.POST.get('api_key') or request.GET.get('api_key')
    
    try:
        lat = float(request.POST.get('lat') or request.GET.get('lat') or -1.2921)
        lon = float(request.POST.get('lon') or request.GET.get('lon') or 36.8219)
    except (ValueError, TypeError):
        lat = -1.2921
        lon = 36.8219

    weather_data = None
    error_message = None

    if api_key:
        weather_data = services.get_weather_data(api_key, lat, lon)
        if not weather_data:
            error_message = "Could not retrieve weather data."
    else:
        error_message = "Please provide an API key."

    outdoor_advice = get_outdoor_advice(weather_data)

    context = {'weather': weather_data, 'lat': lat, 'lon': lon, 'api_key': api_key, 'error': error_message, 'advice': outdoor_advice}
    return render(request, 'index.html', context)