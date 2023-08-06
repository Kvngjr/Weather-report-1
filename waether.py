import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def show_weather():
    city = entry_city.get()
    api_key = "8b0c0a6249e289895adc46ade201e7e7" # Replace with your OpenWeatherMap API key
    try:
        weather_data = get_weather(city, api_key)
        if weather_data["cod"] == 200:
            main_info = weather_data["weather"][0]["main"]
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]

            weather_info = f"Weather: {main_info} ({description})\n"
            weather_info += f"Temperature: {temperature}°C\n"
            weather_info += f"Humidity: {humidity}%"

            label_result.config(text=weather_info)
        else:
            messagebox.showerror("Error", weather_data["message"])

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI
root = tk.Tk()
root.title("Weather App")

label_city = tk.Label(root, text="Enter City:")
label_city.pack()

entry_city = tk.Entry(root)
entry_city.pack()

button_get_weather = tk.Button(root, text="Get Weather", command=show_weather)
button_get_weather.pack()

label_result = tk.Label(root, text="", wraplength=300)
label_result.pack()

root.mainloop()
