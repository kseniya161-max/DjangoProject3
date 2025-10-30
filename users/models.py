from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', help_text='Введите email')
    phone = models.CharField(max_length=50, verbose_name= 'Телефон',blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name= 'Страна',blank=True, null=True, help_text='Введите страну')
    avatar = models.ImageField(upload_to='users/avatar', verbose_name= 'Аватар',blank=True, null=True, help_text='Загрузите фото')

    USERNAME_FIELD = "email"  # Указывает что email будет использоваться дл аутентификации пользователя
    REQUIRED_FIELDS = []   # Указывает какие поля могут быть обязательны для создания пользователя

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email