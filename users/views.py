from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
import secrets
from users.forms import UserRegisterForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class CreateUserView(CreateView):
    """Создаем представление для регистрации"""
    model = User
    form_class = UserRegisterForm
    template_name = 'login.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active=False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}user/email-confirm/{token}/'
        send_mail(
            subject = 'Подтверждение почты',
            message = f'Перейдите по ссылке для подтверждения {url}',
            from_email = EMAIL_HOST_USER,
            recipient_list = [user.email]

        )
        return super().form_valid(form)
