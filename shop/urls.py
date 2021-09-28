"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pages.views import homepage_view
from store.views import store_front_view, product_details_view
from customers.views import register

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('store', store_front_view, name="store"),
    path('store/<int:id>/', product_details_view, name="details"),
    path('register/', register, name="register"),
    path('admin/', admin.site.urls),
]
