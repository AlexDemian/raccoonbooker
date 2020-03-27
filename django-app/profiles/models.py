from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    currency = models.CharField(max_length=3)
    demo_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        new_user = not self.pk
        user = super(User, self).save(*args, **kwargs)
        if new_user:
            Token.objects.create(user=self)
        return user