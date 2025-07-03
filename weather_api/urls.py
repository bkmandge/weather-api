from django.urls import path
from .views import CityCreateAPIView, CityListAPIView,CitySearchAPIView, WeatherDataCreateAPIView, WeatherDataListAPIView, SavedCityCreateAPIView, SavedCityListAPIView, UserListAPIView

urlpatterns = [
    # City endpoints
    path('city-add/', CityCreateAPIView.as_view(), name='add-city'),
    path('cities/', CityListAPIView.as_view(), name='list-cities'),
    path('search-city/', CitySearchAPIView.as_view(), name='search-city'),
    
    
    # Weather endpoints
    path('weather-add/', WeatherDataCreateAPIView.as_view(), name='add-weather'),
    path('weathers/', WeatherDataListAPIView.as_view(), name='list-weather'),
    
    # SavedCity endpoints
    path('saved-city-add/', SavedCityCreateAPIView.as_view(), name='add-saved-city'),
    path('saved-cities/', SavedCityListAPIView.as_view(), name='list-saved-cities'),
    
    # User endpoint
    path('users/', UserListAPIView.as_view(), name='list-users'),
]

