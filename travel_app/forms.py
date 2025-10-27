from django.forms import ModelForm
from travel_app.models import Product


class ProductForm(ModelForm):
    """ Форма Продукта"""
    class Meta:
        model = Product
        fields = '__all__'




