from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class CreateUserView(CreateView):
    """Создаем представление для регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('users:login')
