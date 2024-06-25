from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'price_desc':
        phones = phones.order_by('-price')
    elif sort_by == 'price_asc':
        phones = phones.order_by('price')
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
