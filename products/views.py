from django.http import HttpResponse
from .models import Category, Product


def index(request):
    categories = Category.objects.all()

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Категорії зоомагазину</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                margin: 0;
                padding: 20px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .cat-card {
                background: #ffffff;
                border-radius: 10px;
                padding: 12px 16px;
                margin-bottom: 10px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            }
            .cat-title {
                font-weight: bold;
                color: #00796b;
                margin-bottom: 4px;
            }
            .cat-desc {
                color: #444;
            }
        </style>
    </head>
    <body>
        <h1>Список категорій:</h1>
    """

    for c in categories:
        html += f"""
        <div class="cat-card">
            <div class="cat-title">{c.title}</div>
            <div class="cat-desc">{c.description}</div>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return HttpResponse(html)



def products_list(request):
    products = Product.objects.select_related('category').all()

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Товари зоомагазину</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                margin: 0;
                padding: 20px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            .prod-card {
                background: #ffffff;
                border-radius: 10px;
                padding: 15px 20px;
                margin-bottom: 15px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .prod-title {
                font-size: 18px;
                font-weight: bold;
                color: #004d99;
                margin-bottom: 6px;
            }
            .prod-meta {
                font-size: 14px;
                color: #555;
                margin-bottom: 8px;
            }
            .prod-desc {
                font-size: 14px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Товари нашого зоомагазину</h1>
    """

    for p in products:
        html += f"""
        <div class="prod-card">
            <div class="prod-title">{p.name}</div>
            <div class="prod-meta">
                Категорія: {p.category.title} |
                Країна: {p.country} |
                Ціна: {p.price} грн
            </div>
            <div class="prod-desc">{p.description}</div>
        </div>
        """

    html += """
    </body>
    </html>
    """

    return HttpResponse(html)

