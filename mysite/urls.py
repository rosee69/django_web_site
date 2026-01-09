from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('secure-admin/', admin.site.urls),


    # Token auth
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # API
    path('api/', include('api.urls')),

    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
