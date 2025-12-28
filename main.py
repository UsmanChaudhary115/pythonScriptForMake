from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI(
    title="Weather JSON to Text Converter",
    description="Convert weather JSON data to plain text format suitable for LLMs",
    version="1.0.0"
)


class WeatherData(BaseModel):
    """Weather data model based on OpenWeatherMap 5-day forecast format"""
    city: dict
    list: list


@app.get("/")
def read_root():
    """Root endpoint with API information"""
    return {
        "name": "Weather JSON to Text Converter",
        "version": "1.0.0",
        "endpoints": {
            "POST /convert": "Convert weather JSON to plain text"
        }
    }


@app.post("/convert")
def convert_weather_json(data: WeatherData):
    """
    Convert weather JSON data to plain text format.
    
    Args:
        data: WeatherData object containing city info and weather list
        
    Returns:
        JSON object with 'text' field containing formatted weather data as a string
    """
    try:
        output = f"Location: {data.city['name']}, {data.city['country']}\n"
        output += f"Timezone: {data.city['timezone']}\n\n"

        for item in data.list:
            output += f"Timestamp: {item['dt_txt']}\n"
            output += f"Temp: {item['main']['temp']}°C | Feels Like: {item['main']['feels_like']}°C\n"
            output += f"Humidity: {item['main']['humidity']}% | Clouds: {item['clouds']['all']}%\n"
            output += f"Condition: {item['weather'][0]['description']}\n"
            output += f"Wind: {item['wind']['speed']} m/s | Visibility: {item.get('visibility', 'N/A')} m\n"
            output += f"Rain (3h): {item.get('rain', {}).get('3h', 0)} mm\n"
            output += "--------------------------\n"

        # Convert to safe string (important for APIs / LLMs)
        result = {
            "text": output,
            "status": "success"
        }

        return result

    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required field in JSON: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing weather data: {str(e)}"
        )


@app.post("/convert-raw")
def convert_weather_json_raw(data: dict):
    """
    Convert weather JSON data to plain text format (accepts raw dict).
    
    Args:
        data: Raw dictionary containing city info and weather list
        
    Returns:
        JSON object with 'text' field containing formatted weather data
    """
    try:
        output = f"Location: {data['city']['name']}, {data['city']['country']}\n"
        output += f"Timezone: {data['city']['timezone']}\n\n"

        for item in data["list"]:
            output += f"Timestamp: {item['dt_txt']}\n"
            output += f"Temp: {item['main']['temp']}°C | Feels Like: {item['main']['feels_like']}°C\n"
            output += f"Humidity: {item['main']['humidity']}% | Clouds: {item['clouds']['all']}%\n"
            output += f"Condition: {item['weather'][0]['description']}\n"
            output += f"Wind: {item['wind']['speed']} m/s | Visibility: {item.get('visibility', 'N/A')} m\n"
            output += f"Rain (3h): {item.get('rain', {}).get('3h', 0)} mm\n"
            output += "--------------------------\n"

        result = {
            "text": output,
            "status": "success"
        }

        return result

    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required field in JSON: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing weather data: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
