from django.contrib.auth.models import User
from rest_framework import serializers
from .models import City, WeatherData, SavedCity

# City serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

# Weather serializer
class WeatherDataSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField() # overriding original temperature
    timestamp = serializers.SerializerMethodField()   # overriding original timestamp
    city = serializers.SerializerMethodField()   # overriding original city
    
    class Meta:
        model = WeatherData
        fields = ['id', 'city', 'humidity', 'temperature', 'description', 'timestamp']
    
    def get_city(self, obj):
        return obj.city.name    # returns city name
    
    def get_temperature(self, obj):
        return f"{obj.temperature} °C"

    def get_timestamp(self, obj):
        return obj.timestamp.strftime("%d %b %Y, %I: %M %p")
    
# SavedCity serializer
class SavedCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCity
        fields = '__all__'

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']