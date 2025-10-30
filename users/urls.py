from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path, include


app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
