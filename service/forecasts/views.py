from django.shortcuts import render
from .forms import CityForm
from django import forms
import requests


# Create your views here.
class CityForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)

def city(request):
    city_form = CityForm()
    context = {'city_form': city_form}
    return render(request, 'city.html', context)

def get_weather_data(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        raise ValueError(data.get("message", "City not found"))