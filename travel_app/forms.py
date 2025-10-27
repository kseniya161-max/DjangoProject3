from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from travel_app.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    """ Форма Продукта"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo', 'category', 'price', 'is_favorite']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Добавьте фото'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите категорию товара, например: горящие путевки'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену товара'})
        self.fields['is_favorite'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['is_favorite'].label = 'Избранное'


def clean_name(self):
        """ Проверяет на валидацию имени"""
        name = self.cleaned_data.get('name')
        for i in FORBIDDEN_WORDS:
            if i.lower() in name.lower():
                raise forms.ValidationError(f"Название продукта не должно содержать '{i}'.")
        return name


    def clean_description(self):
        """ Проверяет на валидацию описания"""
        description = self.cleaned_data.get('description')
        for i in FORBIDDEN_WORDS:
            if i.lower() in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать '{i}'.")
        return description


    def clean_price(self):
        price =  self.cleaned_data.get('price')

        if price is None or price <= 0:
            raise ValidationError('Цена не может быть равна или меньше 0')
        return price

