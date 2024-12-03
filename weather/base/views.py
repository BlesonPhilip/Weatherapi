from django.shortcuts import render
import requests
import json
# Create your views here.
def get_weather(city):
  base_url = https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={0fe25267ebf17078f25726ece783599d}
  {
  'q':city,
  'appid':api_key,
  'units':'metric'
  }

response= requests.get(base_url,params=parameters)
if response.status_code == 200:
  return response.json()
else:
  return None


def home(request):
  city = request.GET.get('city')
  if city:
    weather_data_result= get_weather(city)
    
  if weather_data_result is not None:
      weather_data = json.dumps(weather_data_result, indent=4)
      
      weather = weather_data_result['weather'][0]['main']
      weather_description=weather_data_result['weather'][0]['description']
      city=weather_data_result['name']
      country = weather_data_result['sys']['country']
      wind_speed = weather_data_result['wind']['speed']
      pressure = weather_data_result['main']['pressure']
      humidity = weather_data_result['main']['humidity']
      temperature = weather_data_result['main']['temperature']
      
  return render(request,'index.html')