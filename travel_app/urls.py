from django.contrib.admin import views
from django.urls import path, include
from travel_app. apps import NewAppConfig
from travel_app.views import home, product_detail, contact, add_product

app_name = "travel_app"

urlpatterns = [
    path('', home, name='home'),
    path('travel_product/<int:product_id>/', product_detail, name='product_detail'),
    path('contact/', contact, name='contact'),
    path('add_product/', add_product, name='add_product'),

]