from rest_framework import serializers
from .models import WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):
    """
    Creates serializer for WeatherData model.
    Converts WeatherData model data to and from Json.
    """
    class Meta:
        model = WeatherData
        fields = '__all__'
        