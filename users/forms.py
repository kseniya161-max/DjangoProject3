from dataclasses import fields

from django.contrib.auth.forms import UserCreationForm

from users.models import User
# StyleFormMixin

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
