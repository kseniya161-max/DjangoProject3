from django.urls import path, include
from Travel_app. apps import NewAppConfig
from Travel_app. views import home

app_name = "Travel_app"

urlpatterns = [
    path('', home, name='home')
]