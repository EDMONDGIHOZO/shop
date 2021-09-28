from django.contrib import admin
from store.models import Product, Category

store_models = [Product, Category]
admin.site.register(store_models)
