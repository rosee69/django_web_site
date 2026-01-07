from django.urls import path
from .views import (
    CategoryListView, ProductListView,
    CategoryCreateView, ProductCreateView,
    CategoryDetailView, ProductDetailView,
    CategoryUpdateView, ProductUpdateView,
    CategoryDeleteView, ProductDeleteView,
)

app_name = "products"

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("items/", ProductListView.as_view(), name="products_list"),

    path(
        "categories/create/",
        CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "items/create/",
        ProductCreateView.as_view(),
        name="product_create",
    ),

    path(
        "categories/<slug:slug>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "items/<slug:slug>/",
        ProductDetailView.as_view(),
        name="product_detail",
    ),

    path(
        "categories/<slug:slug>/edit/",
        CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "items/<slug:slug>/edit/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),

    path(
        "categories/<slug:slug>/delete/",
        CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        "items/<slug:slug>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
