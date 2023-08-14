import requests #pip install requests in terminal if not installed before
import json
import os
from sys import platform

city = input("Enter your city: ")
api = "77fc6a8470c9129392cdd11b89488abd" #generate your own api
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
r = requests.get(url)
wdic = json.loads(r.text)
kelvin_temp = wdic["main"]["temp"]
x = f"Temperature in {city} is {(kelvin_temp - 273) : .2f}° celcius or {kelvin_temp} kelvin"
print(x)
if platform == "Windows":
    command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
    os.system(command)
elif platform == "Darwin":
    os.system(f"say '{x}'")