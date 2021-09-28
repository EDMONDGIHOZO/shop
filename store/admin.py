from django.contrib import admin
from store.models import Product, Category
from customers.models import Profile

store_models = [Product, Category, Profile]
admin.site.register(store_models)
