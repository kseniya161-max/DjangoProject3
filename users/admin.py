from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdministration(admin.ModelAdmin):
    """Административный интерфейс для управления экземплярами User."""
    list_display = ('id','email')

