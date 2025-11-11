from django.contrib.admin import views
from django.urls import path, include
from travel_app. apps import NewAppConfig
from travel_app.views import HomeListView, ProductDetailView, ContactView,AddProductView, ProductUpdateView, ProductDeleteView, CategoryProductListView
from django.views.decorators.cache import cache_page

app_name = "travel_app"

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/', CategoryProductListView.as_view(), name='category'),

]