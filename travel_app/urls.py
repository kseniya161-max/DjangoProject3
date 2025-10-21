from django.contrib.admin import views
from django.urls import path, include
from travel_app. apps import NewAppConfig
from travel_app.views import HomeListView, ProductDetailView, ContactView,AddProductView

app_name = "travel_app"

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add_product/', AddProductView.as_view(), name='add_product'),

]