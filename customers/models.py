from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime
import os


def get_filename(instance, filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (current_time,old_name)
    return os.path.join('profiles/', filename)


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=CASCADE)
    phones = models.CharField(max_length=12)
    image = models.ImageField(upload_to=get_filename, null=True, blank=True)

    def __str__(self):
        return f'{self.customer.username} Profile!'
