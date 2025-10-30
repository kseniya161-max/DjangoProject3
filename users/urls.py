from django.contrib.auth.views import LoginView

from users.apps import UsersConfig
from django.urls import path, include


app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),

]