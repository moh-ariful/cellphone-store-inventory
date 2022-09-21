from django.shortcuts import render
from .models import Stock
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateUserForm
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def stok(request):
    stocks = Stock.objects.all().order_by('-id')
    query = request.GET.get('q')

    if query:
        stocks = stocks.filter(Q(nama__icontains=query) |
                               Q(jumlah__icontains=query))

    context = {
        'stocks': stocks
    }
    return render(request, 'stok.html', context)


class CreateStock(generic.CreateView):
    model = Stock
    fields = ['nama', 'kategori', 'jumlah', 'harga', 'date']
    template_name = 'createstock.html'
    success_url = reverse_lazy('stok')


class DetailStock(generic.DetailView):
    model = Stock
    template_name = 'detailstock.html'


class UpdateStock(generic.UpdateView):
    model = Stock
    template_name = 'updatestock.html'
    fields = ['nama', 'kategori', 'jumlah', 'harga', 'date']


class DeleteStock(generic.DeleteView):
    model = Stock
    template_name = 'deletestock.html'
    success_url = reverse_lazy('stok')


class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
