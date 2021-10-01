from django.contrib import admin
from products.models import Category, Product

my_models = [Category, Product]

admin.site.register(my_models)
