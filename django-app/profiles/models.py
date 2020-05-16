from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from model_utils import FieldTracker

from config.helpers import get_server_url


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

    tracker = FieldTracker()

    email = models.EmailField(_('email address'), unique=True)
    currency = models.CharField(_('currency'), max_length=3) # TODO: create choices
    user_type = models.CharField(_('account type'), max_length=50, choices=USER_TYPE_CHOICES, default=BASIC_USER)
    confirmed = models.BooleanField(_('is confirmed'), default=False)
    verification_token = models.CharField(_('verification token'), max_length=50)

    @property
    def is_demo_user(self):
        return self.user_type == self.DEMO_USER

    @property
    def is_prem_user(self):
        return self.user_type ==self.PREM_USER

    @property
    def verification_url(self):
        if not self.verification_token:
            return None
        return get_server_url() + reverse('confirm-user', kwargs={'token': self.verification_token})

    def save(self, *args, **kwargs):
        new_user = not self.pk
        if new_user:
            self.verification_token = get_random_string(length=50)
        return super().save(*args, **kwargs)
