# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from .models import City, WeatherData, SavedCity
from .serializers import CitySerializer, WeatherDataSerializer, SavedCitySerializer, UserSerializer

# Adding City name 
class CityCreateAPIView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
    
# Listing city names    
class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# Searching city 
# request:- GET /api/city-search/?name=Pune
class CitySearchAPIView(generics.ListAPIView):
    serializer_class = CitySerializer
    
    def get_queryset(self):
        queryset = City.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


# Adding weather data
class WeatherDataCreateAPIView(generics.CreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
        
    
# Listing weather data
class WeatherDataListAPIView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
        

# Adding city and user data
class SavedCityCreateAPIView(generics.CreateAPIView):
    queryset = SavedCity.objects.all()
    serializer_class = SavedCitySerializer


# Listing city and user data
class SavedCityListAPIView(generics.ListAPIView):
    queryset = SavedCity.objects.all()
    serializer_class = SavedCitySerializer


# Listing user data
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    