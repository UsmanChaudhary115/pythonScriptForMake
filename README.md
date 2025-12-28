# Weather JSON to Text Converter API

A FastAPI application that converts OpenWeatherMap JSON data into formatted plain text suitable for feeding into LLMs (Large Language Models).

## Features

- **JSON to Text Conversion**: Converts weather forecast JSON into readable plain text format
- **FastAPI**: Modern, fast, and easy-to-use Python web framework
- **Input Validation**: Uses Pydantic for robust data validation
- **Error Handling**: Comprehensive error handling with meaningful error messages
- **Interactive Documentation**: Auto-generated API docs via Swagger UI

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd pythonScriptForMake
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the API server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Access the API Documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### 1. GET `/`
Root endpoint with API information.

**Response:**
```json
{
  "name": "Weather JSON to Text Converter",
  "version": "1.0.0",
  "endpoints": {
    "POST /convert": "Convert weather JSON to plain text"
  }
}
```

### 2. POST `/convert`
Convert weather JSON data to plain text (with Pydantic validation).

**Request Body:**
```json
{
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
    }
  ]
}
```

**Response:**
```json
{
  "text": "Location: London, GB\nTimezone: GMT\n\nTimestamp: 2025-12-28 12:00:00\nTemp: 5.2°C | Feels Like: 2.1°C\nHumidity: 75% | Clouds: 60%\nCondition: partly cloudy\nWind: 4.5 m/s | Visibility: 10000 m\nRain (3h): 0.2 mm\n--------------------------\n",
  "status": "success"
}
```

### 3. POST `/convert-raw`
Convert weather JSON data using raw dictionary (no strict validation).

**Request Body:** Same as `/convert`

**Response:** Same as `/convert`

## Usage Examples

### Using Python Requests

```python
import requests

data = {
    "city": {
        "name": "London",
        "country": "GB",
        "timezone": "GMT"
    },
    "list": [...]
}

response = requests.post("http://localhost:8000/convert", json=data)
result = response.json()
print(result["text"])
```

### Using cURL

```bash
curl -X POST "http://localhost:8000/convert" \
  -H "Content-Type: application/json" \
  -d @weather_data.json
```

### Running the Test Script

```bash
python test_api.py
```

This will test all endpoints with sample data.

## Project Structure

```
pythonScriptForMake/
├── main.py                 # FastAPI application
├── test_api.py             # Test script with sample data
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Output Format

The converter generates the following format:

```
Location: <City>, <Country>
Timezone: <Timezone>

Timestamp: <Date Time>
Temp: <Temperature>°C | Feels Like: <Feels Like>°C
Humidity: <Humidity>% | Clouds: <Cloud Coverage>%
Condition: <Weather Condition>
Wind: <Wind Speed> m/s | Visibility: <Visibility> m
Rain (3h): <Rainfall> mm
--------------------------
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- **400 Bad Request**: Missing required fields in JSON
- **500 Internal Server Error**: Unexpected errors during processing

Example error response:
```json
{
  "detail": "Missing required field in JSON: 'city'"
}
```

## Configuration

To run on a different host/port, modify the `main.py` file:

```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
```

## Dependencies

- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **python-multipart**: For form data handling

## Future Enhancements

- [ ] Support for batch conversion
- [ ] Caching for repeated requests
- [ ] Support for different output formats (CSV, JSON)
- [ ] Rate limiting
- [ ] Authentication/Authorization
- [ ] Database integration for logging

## License

MIT License

## Author

Created for weather data to LLM text conversion pipeline
