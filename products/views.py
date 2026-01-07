from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Category, Product
from .forms import CategoryForm, ProductForm
 

class CategoryListView(ListView):
    model = Category
    template_name = "products/categories.html"
    context_object_name = "categories"
    paginate_by = 5
    ordering = ["title"]


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"
    paginate_by = 6
    ordering = ["name"]


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/category_form.html"
    success_url = reverse_lazy("products:category_list")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("products:products_list")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "products/category_detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.product_set.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/category_form.html"
    success_url = reverse_lazy("products:category_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy("products:products_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "products/category_confirm_delete.html"
    success_url = reverse_lazy("products:category_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("products:products_list")
