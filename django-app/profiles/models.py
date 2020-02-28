from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    currency = models.CharField(max_length=3)
    demo_user = models.BooleanField(default=False)