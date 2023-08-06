import requests

# OpenWeatherMap API key (replace with your own API key)
api_key = "8b0c0a6249e289895adc46ade201e7e7"

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get the city name from the user
city = input("Enter the city name: ")

# Create the complete URL for the API request
complete_url = f"{base_url}q={city}&appid={api_key}"

# Send the API request and get the response
response = requests.get(complete_url)

# Check if the request was successful (status code 200)

if response.status_code == 200:
        data = response.json()

        # Extract relevant weather data from the response
        weather_main = data["weather"][0]["main"]
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Convert temperature from Kelvin to Celsius
        temperature_celsius = temperature - 273.15

        # Display the weather information
        print(f"Weather in {city}: {weather_main} ({weather_description})")
        print(f"Temperature: {temperature_celsius:.2f} °C")
        print(f"Humidity: {humidity}%")
else:
    print(
        "Error: Unable to fetch weather data. Please check the city name or try again later."
    )

  
