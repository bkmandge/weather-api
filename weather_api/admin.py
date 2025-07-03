from django.contrib import admin
from .models import City, WeatherData, SavedCity

# Register your models here.
admin.site.register(City)
admin.site.register(WeatherData)
admin.site.register(SavedCity)
