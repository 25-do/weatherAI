import requests

# Note: Ensure 'requests' is installed (`pip install requests`)

WEATHER_API_URL = "https://api.weather-ai.co/v1/weather"

def get_weather_data(api_key, lat, lon):
    """
    Fetches weather data for given coordinates.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "days": 7,
        "ai": "true",
        "units": "metric",
        "lang": "en"
    }

    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Send the request via GET with URL parameters and Bearer token authorization
        response = requests.get(WEATHER_API_URL, params=params, headers=headers)
        
        # Debugging logs
        print(f"API Request URL: {response.request.url}")
        print(f"API Response Status: {response.status_code}")
        print(f"API Response Content: {response.text}")
        
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API Request Exception: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error Response Content: {e.response.text}")
        return None