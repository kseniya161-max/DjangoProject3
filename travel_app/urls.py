from django.urls import path, include
from travel_app. apps import NewAppConfig
from travel_app. views import home

app_name = "travel_app"

urlpatterns = [
    path('', home, name='home')
]