from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductForm
from django.core.paginator import Paginator



def home(request):
    """Отображает главную страницу приложения"""
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


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









