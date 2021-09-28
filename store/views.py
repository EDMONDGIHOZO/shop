from django.shortcuts import render


def store_front_view (request):
    return render(request, 'store/index.html', {})
