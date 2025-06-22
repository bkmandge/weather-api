# pylint: disable=no-member

from decouple import config

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WeatherData
from .serializers import WeatherDataSerializer
import requests

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

OPENWEATHER_API_KEY = config('OPENWEATHER_API_KEY')
# View to create and list weather
class WeatherDataView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


# View to fetch live weather
class LiveWeatherAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Get live weather by city name using OpenWeather API",
        manual_parameters=[
            openapi.Parameter(
                'city',
                openapi.IN_QUERY,
                description="City name (e.g., 'Pune')",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={200: 'Success', 400: 'City required', 503: 'OpenWeather API error'}
    )
    
    
    def get(self, request, format=None):
        city = request.query_params.get('city')
        if not city:
            return Response({"error":"City field is required"}, status=status.HTTP_400_BAD_REQUEST)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
        
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return Response({"error":"City not found or API error."}, status=response.status_code)
        data = response.json()
        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return Response(result, status=200)