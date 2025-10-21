from string import Template

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from .models import Product, ProductForm
from django.core.paginator import Paginator


class HomeListView(ListView):
    """Отображает главную страницу приложения"""
    model = Product
    template_name = 'home.html'
    context_object_name= 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all()


# def home(request):
#     """Отображает главную страницу приложения"""
#     products = Product.objects.all()
#     paginator = Paginator(products, 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'home.html', {'page_obj': page_obj})


class ProductDetailView(DetailView):
    """Отображает страницу продукта"""
    model = Product
    template_name = 'product_detail.html'
    context_object_name= 'travel_product'
    pk_url = 'product_id'

#
# def product_detail(request, product_id):
#     """Отображает страницу продукта"""
#     travel_product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_detail.html', {'travel_product': travel_product })


class ContactView(TemplateView):
    """Отображает страницу с контактами"""
    template_name= 'contact.html'

# def contact(request):
#     return render(request, 'contact.html', {})
#
class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('travel_app:home')
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('travel_app:home')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form':form})









