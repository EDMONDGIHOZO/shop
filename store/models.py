from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=140, null=True)

    def __str__(self):
        return self.name


class Product (models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    image_url = models.TextField(
        max_length=160, default="https://www.iconsdb.com/icons/preview/white/electronics-xxl.png")

    def __str__(self):
        return self.name
