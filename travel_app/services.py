from django.core.cache import cache

from config.settings import CACHE_ENABLED
from travel_app.models import Product, Category


def get_list_from_cache():
    """Обращаемся к базе данных в случае если данных нет в Кеше"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'list_product_cache'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_category_product(category):
    """Получение списка продуктов отфильтрованного по категориям"""
    if not category:
        return None
    products = Product.objects.filter(category=category)
    return products