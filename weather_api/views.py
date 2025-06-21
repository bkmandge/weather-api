# pylint: disable=no-member
from rest_framework import generics
from .models import WeatherData
from .serializers import WeatherDataSerializer
# Create your views here.

class WeatherDataView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
