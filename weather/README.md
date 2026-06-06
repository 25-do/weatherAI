# WeatherAI Dashboard

A Django-based web application that acts as your personal weather assistant. It fetches and displays the current weather, provides a chronological hourly forecast, and includes a smart "Should I Go Outside?" decision tool based on local weather conditions.

## Features

- **Current Weather**: View real-time temperature, condition, humidity, wind speed, and "feels like" metrics based on customizable coordinates.
- **Hourly Forecast**: Scroll through a visual timeline of predicted hourly temperatures and conditions.
- **Outdoor Activity Advice**: Evaluates the current weather (e.g., checking for rain or extreme heat) to advise you on whether it's a good time for outdoor activities.
- **Dashboard Inputs**: Easily input your WeatherAI API key, latitude, and longitude directly from the user interface.

## Technology Stack

- **Backend**: Python, Django 5.2
- **External APIs**: [WeatherAI API](https://api.weather-ai.co/) (using the `requests` library)
- **Frontend**: HTML, Bootstrap (CSS framework), Alpine.js (for lightweight interactivity)

## Prerequisites

- Python 3.8+
- `pip` (Python package manager)

## Setup Instructions

1. **Navigate to the project directory:**
   Open your terminal and navigate to the directory containing `manage.py`.
   ```bash
   cd /path/to/weatherAI/weather
   ```

2. **Create a virtual environment (Recommended):**
   It is best practice to use a virtual environment to manage your dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   Install Django and the required `requests` library.
   ```bash
   pip install django requests
   ```

4. **Run database migrations:**
   Set up the default SQLite database.
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## How It Works

1. **User Input (`index.html`)**: The user provides their WeatherAI API Key, Latitude, and Longitude through a form on the dashboard.
2. **View Processing (`views.py`)**: 
   - Django intercepts the GET/POST request and extracts the input values.
   - If an API key is provided, the backend requests weather data via the service module.
3. **API Integration (`services.py`)**: 
   - The `get_weather_data` function uses the `requests` library to securely call the WeatherAI API.
   - It passes the API key as a Bearer token in the `Authorization` header and the required parameters (coordinates, days, units) as URL query strings.
4. **Decision Engine (`views.py`)**: 
   - The `get_outdoor_advice` helper function evaluates the API response, specifically checking for rain or temperatures over 30°C, and generates a tailored recommendation.
5. **Rendering (`index.html`)**: The application renders the weather data and advice to the dashboard using Django's templating engine, enhanced with Bootstrap styling and Alpine.js for interactive elements (like toggling the advice panel).

## License

This project is open-source and available for personal or educational use.