from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("cart/", views.cart_detail, name="cart_detail"),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),

    path("increase/<int:item_id>/", views.increase_quantity, name="increase"),
    path("decrease/<int:item_id>/", views.decrease_quantity, name="decrease"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove"),

    path("checkout/", views.checkout, name="checkout"),
]
