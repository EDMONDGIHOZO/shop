from typing import Tuple
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.db.models.deletion import CASCADE


class Category (models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    # for name in admin dashboard
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=CASCADE)
    name = models.CharField(max_length=230)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
