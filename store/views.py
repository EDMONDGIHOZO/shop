from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def store_front_view(request):
    # fetch data from database
    products_data = Product.objects.all()
    context = {
        "products": products_data
    }

    return render(request, 'store/index.html', context)


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"hello{username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")
    return HttpResponse("Messages added", content_type="text/plain")

@user_passes_test(lambda user: user.is_staff)
def product_details_view(request, id, *args, **kwargs):
    data = None
    # fetch product
    if id is not None:
        data = Product.objects.get(id=id)
    context = {
        "product": data
    }
    return render(request, "store/details.html", context)
