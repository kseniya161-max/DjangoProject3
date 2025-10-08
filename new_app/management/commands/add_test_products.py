from django.core.management.base import BaseCommand
from new_app.models import Product, Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1 = Category.objects.create(name='Тест Горящие', description='Море')
        Product.objects.create(
            name='Тест Турция',
            description='Море',
            photo='products/Т.jpg',
            category=category1,
            price=100000
        )

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены'))