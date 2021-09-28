from customers.forms import CustomerCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
from customers.forms import CustomerCreationForm


def register(request):
    if request.method == "GET":
        return render(request, "customers/register.html", {"form": CustomerCreationForm})
    elif request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            return redirect(reverse("homepage"))
