from rest_framework import serializers
from .models import City, WeatherData, SavedCity


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class WeatherDataSerializer(serializers.ModelSerializer):
    """
    Creates serializer for WeatherData model.
    Converts WeatherData model data to and from Json.
    """
    class Meta:
        model = WeatherData
        fields = '__all__'
        

class SavedCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCity
        fields = "__all__"
        read_only_fields = ['user']     # user is set from request, not from input
        
    