from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductForm


def home(request):
    """Отображает главную страницу приложения"""
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    """Отображает страницу продукта"""
    travel_product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'travel_product': travel_product })


def contact(request):
    return render(request, 'contact.html', {})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('travel_app:home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form':form})









