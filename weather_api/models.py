from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create city model
class City(models.Model):
    name = models.CharField(max_length=100, default="Pune")
    country = models.CharField(max_length=50, default="IN")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"
    

class WeatherData(models.Model):
    """stores weather related data such as city name, temperature info
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="weather_data")
    temperature = models.FloatField()
    description = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.city} -> {self.temperature}°C"
   
# to show relations between User and City
class SavedCity(models.Model):
    # related_name => Added for reverse lookups
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saved_cities", null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="saved_by_users")
    saved_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f"{self.user.username} saved {self.city.name}"