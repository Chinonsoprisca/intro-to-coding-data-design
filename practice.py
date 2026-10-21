import requests

# url = "https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=48.13&longitude=11.58&elevation=524"
url = "https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=48.13&longitude=11.58&elevation=524&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"


response = requests.get(url)

data = response.json()
print(data)