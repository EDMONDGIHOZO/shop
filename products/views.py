from django.shortcuts import render

# Create your views here.


def products_home_view(request):
    return render(request, "products/index.html", {})
