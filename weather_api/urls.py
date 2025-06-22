from django.urls import path
from .views import WeatherDataView, LiveWeatherAPIView


urlpatterns = [
    path('weather/', WeatherDataView.as_view(), name='weather-list-create'),
    path('live-weather/', LiveWeatherAPIView.as_view(), name='live-weather'),
]
