from django.shortcuts import render
from .models import Stock
# Create your views here.


def home(request):
    return render(request, 'home.html')


def stok(request):
    stocks = Stock.objects.all().order_by('-id')
    context = {
        'stocks': stocks
    }
    return render(request, 'stok.html', context)
