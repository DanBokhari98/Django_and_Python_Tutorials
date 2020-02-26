# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json, sys, os

# Enter your API key here
api_key = "mykey"

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def printWeather():
    weather = get_weather(api_key, 'New York')
    condition = weather['main']
    print(condition)
    #description = weather['description']
    print(weather)
    celc_to_fah = ( condition['temp']* (9/5))+32
    print(celc_to_fah)


printWeather()
