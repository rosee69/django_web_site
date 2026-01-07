from django import forms
from django.forms import TextInput, Textarea, Select, NumberInput, FileInput
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва категорії',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Короткий опис категорії',
                'rows': 3,
            }),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'country', 'category', 'image']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва товару',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опис товару',
                'rows': 4,
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна, ₴',
                'step': '0.01',
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Країна виробник',
            }),
            'category': Select(attrs={
                'class': 'form-control',
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
            }),
        }
