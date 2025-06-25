from django.urls import path
from .views import CityCreateAPIView, CitySearchAPIView, WeatherDataCreateAPIView, WeatherDataListView, SavedCityCreateView, SavedCityListView


urlpatterns = [
    path('cities/add/', CityCreateAPIView.as_view(), name='city-add'),
    path('cities/search/', CitySearchAPIView.as_view(), name='city-search'),
    path('weather/add/', WeatherDataCreateAPIView.as_view(), name='weather-add'),
    path('weather/', WeatherDataListView.as_view(), name='weather-list'),    
    path('saved-cities/add/', SavedCityCreateView.as_view(), name='saved-city-add'),    
    path('saved-cities-all/', SavedCityListView.as_view(), name='saved-city-list-all'),    
]
