from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    currency = models.CharField(max_length=3)
    date_format = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        first_save = self.pk is None
        super(User, self).save(*args, **kwargs)