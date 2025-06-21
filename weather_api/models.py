from django.db import models

# Create your models here.
class WeatherData(models.Model):
    """stores weather related data such as city name, temperature info
    """
    city = models.CharField(max_length = 100)
    temperature = models.FloatField()
    description = models.TextField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.city} -> {self.temperature}°C"
    
