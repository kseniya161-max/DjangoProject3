from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Product, ProductForm
from django.core.paginator import Paginator


class HomeListView(ListView):
    """Отображает главную страницу приложения"""
    model = Product
    template_name = 'home.html'
    context_object_name= 'page_object'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    """Отображает страницу продукта"""
    model = Product
    template_name = 'product_detail.html'
    context_object_name= 'travel_product'


class ContactView(TemplateView):
    """Отображает страницу с контактами"""
    template_name= 'contact.html'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('travel_app:home')








