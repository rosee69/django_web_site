from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = """
    <html>
        <head>
            <title>Our Store — Orders</title>
        </head>
        <body style="font-family: Arial, sans-serif; margin: 40px;">
            <h1>Order section</h1>
            <h3>
                Here you can review your orders, check their status 
                and see the history of purchases.
            </h3>
        </body>
    </html>
    """
    return HttpResponse(html)