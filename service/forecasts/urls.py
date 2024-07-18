from django.urls import path, include
from .views import city
from django.conf.urls.static import static


urlpatterns = [
    path('weather', city, name='weather '),
]
