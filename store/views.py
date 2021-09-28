from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product


def store_front_view(request):
    # fetch data from database
    products_data = Product.objects.all()
    context = {
        "products": products_data
    }

    return render(request, 'store/index.html', context)


def product_details_view(request, id, *args, **kwargs):
    data = None
    # fetch product
    if id is not None:
        data = Product.objects.get(id=id)
    context = {
        "product": data
    }
    return render(request, "store/details.html", context)
