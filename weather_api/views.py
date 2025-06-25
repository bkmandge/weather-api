from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import City, WeatherData, SavedCity
from .serializers import CitySerializer, WeatherDataSerializer, SavedCitySerializer

# API to save city
class CityCreateAPIView(generics.CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    

# API to Search City
class CitySearchAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'country']
    
    
# API / View to create weather
class WeatherDataCreateAPIView(generics.CreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    

# API / View to list weather
class WeatherDataListView(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    

class SavedCityCreateView(generics.CreateAPIView):
    queryset = SavedCity.objects.all()
    serializer_class = SavedCitySerializer
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        serializer.save()
        

class SavedCityListView(generics.ListAPIView):
    queryset = SavedCity.objects.all()
    serializer_class = SavedCitySerializer
    permission_classes = [permissions.AllowAny]
    

