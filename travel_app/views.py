from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    """Отображает главную страницу приложения"""
    return render(request, 'home.html')


def product_detail(request, product_id):
    """Отображает страницу продукта"""
    travel_product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'travel_product': travel_product })
