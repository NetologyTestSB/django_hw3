from django.shortcuts import render, redirect

from phones.models import Phone

def index_page(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort', '')
    if sort_param == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.order_by('price').reverse()
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
