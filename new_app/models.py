from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")
    photo = models.ImageField(upload_to='products/', verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за единицу товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создание")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Дата изменения")

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименование'
        ordering = ['name']


