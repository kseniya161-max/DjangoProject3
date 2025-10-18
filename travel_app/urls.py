from django.urls import path, include
from travel_app. apps import NewAppConfig
from travel_app.views import home, product_detail

app_name = "travel_app"

urlpatterns = [
    path('', home, name='home'),
    path('travel_product/<int: product_id>', product_detail, name='product_detail')

]