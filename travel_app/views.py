from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Product
from django.core.paginator import Paginator
from .forms import ProductForm, ProductModeratorForm


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


class AddProductView(LoginRequiredMixin, CreateView):
    """Создает продукт"""
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('travel_app:home')


    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super(). form_valid(form)




class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует продукт"""
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('travel_app:home')


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('travel_app.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    """Удаляет продукт"""
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('travel_app:home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('travel_app.can_delete_product'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)









