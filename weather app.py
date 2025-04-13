import tkinter as tk
import requests
from datetime import datetime

# Replace with your actual API key from OpenWeatherMap
API_KEY = "a7b316c90c6d66d3be2d73e3df059396"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        pressure = data['main']['pressure']

        temp_label.config(text=f"{temperature}°C")
        feels_like_label.config(text=f"Feels like: {feels_like}°C")
        desc_label.config(text=description.title())
        wind_label.config(text=f"{wind} m/s")
        humidity_label.config(text=f"{humidity} %")
        pressure_label.config(text=f"{pressure} hPa")
        time_label.config(text=datetime.now().strftime("%I:%M %p"))

    except requests.RequestException as e:
        temp_label.config(text="Error")
        feels_like_label.config(text="Check API Key / Internet")
        desc_label.config(text="")
        wind_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="")
    except KeyError:
        temp_label.config(text="Invalid City")
        feels_like_label.config(text="Try Again")
        desc_label.config(text="")
        wind_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="")

def search():
    city = city_entry.get()
    get_weather(city)

# Main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x450")
root.config(bg="white")

# City entry
city_entry = tk.Entry(root, font=("Arial", 18), justify="center")
city_entry.pack(pady=10)

search_btn = tk.Button(root, text="Search", font=("Arial", 12), command=search)
search_btn.pack()

# Time
time_label = tk.Label(root, font=("Arial", 14), bg="white")
time_label.pack(pady=5)

# Temperature display
temp_label = tk.Label(root, font=("Arial", 40), bg="white", fg="#FF6F61")
temp_label.pack()

# Feels like
feels_like_label = tk.Label(root, font=("Arial", 14), bg="white")
feels_like_label.pack()

# Description
desc_label = tk.Label(root, font=("Arial", 14), bg="white")
desc_label.pack(pady=5)

# Weather details frame
frame = tk.Frame(root, bg="skyblue")
frame.pack(fill="both", expand="yes", pady=10)

# Labels
wind_text = tk.Label(frame, text="WIND", font=("Arial", 12), bg="skyblue")
wind_text.grid(row=0, column=0, padx=10, pady=5)

humidity_text = tk.Label(frame, text="HUMIDITY", font=("Arial", 12), bg="skyblue")
humidity_text.grid(row=0, column=1, padx=10, pady=5)

pressure_text = tk.Label(frame, text="PRESSURE", font=("Arial", 12), bg="skyblue")
pressure_text.grid(row=0, column=2, padx=10, pady=5)

wind_label = tk.Label(frame, text="--", font=("Arial", 12), bg="skyblue")
wind_label.grid(row=1, column=0, padx=10, pady=5)

humidity_label = tk.Label(frame, text="--", font=("Arial", 12), bg="skyblue")
humidity_label.grid(row=1, column=1, padx=10, pady=5)

pressure_label = tk.Label(frame, text="--", font=("Arial", 12), bg="skyblue")
pressure_label.grid(row=1, column=2, padx=10, pady=5)

root.mainloop()
