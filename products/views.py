from django.shortcuts import render
from .models import Category, Product

def category_list(request) :
    categories = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': categories})


def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'products/products.html', {'products': products})

 
