from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from django.urls import path, include
from users. views import CreateUserView


app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
]

