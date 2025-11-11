from django.core.cache import cache

from config.settings import CACHE_ENABLED
from travel_app.models import Product


def get_list_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'list_product_cache'
    products = cache.get('list_product_cache')
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set('list_product_cache', products)
    return products