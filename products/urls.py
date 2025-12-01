
from django.urls import path
from . import views

app_name = "products" 

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('items/', views.product_list, name='products_list'),
]
