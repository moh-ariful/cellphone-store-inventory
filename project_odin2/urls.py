from stock.views import home, stok
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', stok, name='stok'),
    path('', home, name='home'),
]
