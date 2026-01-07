from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, OrderItem


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    order, _ = Order.objects.get_or_create(
        user=request.user,
        is_active=True
    )

    item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("orders:cart_detail")


@login_required
def cart_detail(request):
    order = Order.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    return render(request, "orders/cart.html", {
        "order": order
    })

@login_required
def increase_quantity(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    item.quantity += 1
    item.save()
    return redirect("orders:cart_detail")


@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("orders:cart_detail")

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    item.delete()
    return redirect("orders:cart_detail")

@login_required
def checkout(request):
    order = Order.objects.filter(
        user=request.user,
        is_active=True
    ).first()

    if order:
        order.is_active = False
        order.save()

    return render(request, "orders/check_successful.html")
