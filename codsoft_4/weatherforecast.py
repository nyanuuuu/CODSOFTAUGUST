# Importing libraries:
from tkinter import *
import requests
from tkinter import messagebox

# Function:
def get_weather(city):
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data is not None:
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        temp_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        description_label.config(text=f"Description: {weather_data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "City not found")
# Creating GUI window:
window = Tk()
window.title('//Weather Forecast//')
window.geometry("300x300")
icon = PhotoImage(file='icon6.png')
window.iconphoto(True, icon)
window.config(background="#72A0C1")

# Labels:
label = Label(window, text="Weather Forecast", font=("Times New Roman", 20, "italic bold"), bg="#72A0C1", fg="#2b235a")
label.pack(pady=10)

city_label = Label(window, text="Enter City:",font=("Times New Roman", 14,  "italic bold"), bg="#72A0C1", fg="white")
city_label.pack(pady=3)
city_entry = Entry(window,width=20,font=("Times New Roman",12,"bold"),fg="#54416d")
city_entry.pack(pady=3)

# button:
weather_button = Button(window, text="Get Weather", command=display_weather,font=("Times New Roman", 10,  "bold"),bg="#54416d",fg="white")
weather_button.pack(pady=10)

humidity_label = Label(window, text="",width=25,font=("Times New Roman",12,"bold"),fg="#54416d")
humidity_label.pack()

temp_label = Label(window, text="",width=25,font=("Times New Roman",12,"bold"),fg="#54416d")
temp_label.pack()

description_label = Label(window, text="",width=25,font=("Times New Roman",12,"bold"),fg="#54416d")
description_label.pack()

window.mainloop()