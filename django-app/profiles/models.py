from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # User type
    BASIC_USER = 'basic'
    DEMO_USER = 'demo'
    PREM_USER = 'prem'
    USER_TYPE_CHOICES = [
        (BASIC_USER, _('Basic')),
        (DEMO_USER, _('Demo')),
        (PREM_USER, _('Premium')),
    ]

    email = models.EmailField(_('email address'), unique=True)
    currency = models.CharField(_('currency'), max_length=3)
    user_type = models.CharField(_('user_type'), max_length=50, choices=USER_TYPE_CHOICES, default=BASIC_USER)
    confirmed = models.BooleanField(_('confirmed'), default=False)

    @property
    def is_demo_user(self):
        return self.user_type == self.DEMO_USER

    @property
    def is_prem_user(self):
        return self.user_type ==self.PREM_USER

    def save(self, *args, **kwargs):
        new_user = not self.pk
        user = super(User, self).save(*args, **kwargs)
        if new_user:
            Token.objects.create(user=self)
        return user