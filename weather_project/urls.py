"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Creates metadata of Weather API, stores in schema_view variable
schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='v1',
        description="API for storing and reviewing weather data by city name.",
        contact=openapi.Contact(email='root@example.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny] # anyone can view API doc w/o authentication
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather_api.urls')),
    
    # above scheme_view is connected swagger and redoc UI route / endpoint / url 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
