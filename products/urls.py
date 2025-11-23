from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='product_index'),
    path("items/", views.products_list, name="products_list"),
]
