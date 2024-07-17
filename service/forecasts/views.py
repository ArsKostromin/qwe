from django.shortcuts import render
from forms import CityForm

# Create your views here.
def city(request):
    city_form = CityForm()
    context = {'city_form':city_form}