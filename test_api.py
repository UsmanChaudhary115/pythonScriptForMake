"""
Sample test script for the Weather JSON to Text Converter API
"""

import requests
import json

# Sample weather data (from OpenWeatherMap 5-day forecast)
sample_data = {
    "city": {
        "name": "London",
        "country": "GB",
        "timezone": "GMT"
    },
    "list": [
        {
            "dt_txt": "2025-12-28 12:00:00",
            "main": {
                "temp": 5.2,
                "feels_like": 2.1,
                "humidity": 75
            },
            "clouds": {
                "all": 60
            },
            "weather": [
                {
                    "description": "partly cloudy"
                }
            ],
            "wind": {
                "speed": 4.5
            },
            "visibility": 10000,
            "rain": {
                "3h": 0.2
            }
        },
        {
            "dt_txt": "2025-12-28 15:00:00",
            "main": {
                "temp": 4.8,
                "feels_like": 1.5,
                "humidity": 80
            },
            "clouds": {
                "all": 80
            },
            "weather": [
                {
                    "description": "overcast clouds"
                }
            ],
            "wind": {
                "speed": 5.2
            },
            "visibility": 9000,
            "rain": {
                "3h": 1.5
            }
        }
    ]
}


def test_api():
    """Test the API endpoints"""
    
    api_url = "http://localhost:8000"
    
    # Test root endpoint
    print("=" * 50)
    print("Testing Root Endpoint")
    print("=" * 50)
    response = requests.get(f"{api_url}/")
    print(json.dumps(response.json(), indent=2))
    
    # Test /convert endpoint (with Pydantic validation)
    print("\n" + "=" * 50)
    print("Testing /convert Endpoint")
    print("=" * 50)
    response = requests.post(f"{api_url}/convert", json=sample_data)
    if response.status_code == 200:
        result = response.json()
        print("Status:", result["status"])
        print("\nConverted Text:\n")
        print(result["text"])
    else:
        print("Error:", response.json())
    
    # Test /convert-raw endpoint (with raw dict)
    print("\n" + "=" * 50)
    print("Testing /convert-raw Endpoint")
    print("=" * 50)
    response = requests.post(f"{api_url}/convert-raw", json=sample_data)
    if response.status_code == 200:
        result = response.json()
        print("Status:", result["status"])
        print("\nConverted Text:\n")
        print(result["text"])
    else:
        print("Error:", response.json())


if __name__ == "__main__":
    print("Make sure the API is running on http://localhost:8000")
    print("Run: python main.py")
    print("\n")
    
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Make sure it's running on http://localhost:8000")
