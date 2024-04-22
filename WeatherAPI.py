import requests

def weatherCheck(cityName):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "0cfa51bc6259fabaaac26fb124b89437"
    CITY = cityName

    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = round(kelvin - 273.15)
        fahrenhiet = round(celsius * (9/5) + 32)
        return celsius, fahrenhiet

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    flk = response['main']['feels_like']
    flc, flf = kelvin_to_celsius_fahrenheit(flk)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    
    print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
    print(f"Temperature in {CITY} feels like: {flc:.2f}C or {flf:.2f}F")
    print(f"humidity in {CITY}: {humidity:.2F}%")
    print(f"General weather in {CITY}: {description}")
