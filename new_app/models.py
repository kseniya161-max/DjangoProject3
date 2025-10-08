from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")
    photo = models.ImageField(verbose_name="Изображение")
    category = models.CharField(max_length=200, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена за единицу товара")
    created_at = models.DateField(verbose_name="Дата создание")
    updated_at = models.DateField(verbose_name="Дата изменения")

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименование'
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=200, verbose_name="Описание")

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Наименование'
        verbose_name_plural = 'Наименования'
        ordering = ['name']
