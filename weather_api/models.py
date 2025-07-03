from django.utils.timezone import localtime
# importing and using built-in User model
from django.contrib.auth.models import User
from django.db import models

# City model
class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="IN")
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"

    class Meta:
        verbose_name_plural = "Cities"    

# WeatherData model    
class WeatherData(models.Model):
    # related_name -> for reverse querying.
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="weather_reports")
    temperature = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        local_timestamp = localtime(self.timestamp).strftime("%d %b %Y, %I:%M %p")
        return f"Weather in {self.city} at {local_timestamp}."

    class Meta:
        verbose_name_plural = "Weather Data"

# SavedCity model:- creating relation between city and user
# importing city and user with ForeignKey from City and User model 
class SavedCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Saved: {self.city.name} by {self.user.username}"
    
    class Meta:
        verbose_name_plural = "Saved Cities"
    