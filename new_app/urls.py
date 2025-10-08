from django.urls import path, include
from new_app. apps import NewAppConfig
from new_app. views import home

app_name = NewAppConfig.name

urlpatterns = [
    path('', home, name='home')
]