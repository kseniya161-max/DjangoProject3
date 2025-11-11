from django.core.cache import cache

from config.settings import CACHE_ENABLED
from travel_app.models import Product


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