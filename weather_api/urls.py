from django.urls import path
from .views import WeatherDataView


urlpatterns = [
    path('weather/', WeatherDataView.as_view(), name='weather-list-create')
]
