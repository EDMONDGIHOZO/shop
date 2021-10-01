from django.urls import path, include
from products.views import Latestprducts

urlpatterns = [
    # get the latest products
    path('products-latest', Latestprducts.as_view())
]
