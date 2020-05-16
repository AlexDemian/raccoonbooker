from django.dispatch import receiver
from django.db.models.signals import post_save

from profiles.models import User
from profiles.helpers import send_mail_on_registration_success, send_mail_on_confirmation_success 


@receiver(post_save, sender=User, dispatch_uid="send_email_on_registration")
def send_email_on_registration(sender, instance, created, **kwargs):

    if all([
        instance.tracker.previous('user_type') == User.DEMO_USER,
        instance.user_type == User.BASIC_USER
    ]) or all([
        created, 
        instance.user_type != User.DEMO_USER
    ]):
        send_mail_on_registration_success(instance, instance.password)

@receiver(post_save, sender=User, dispatch_uid="send_email_on_confirmation")
def send_email_on_confirmation(sender, instance, **kwargs):

    if instance.tracker.has_changed('confirmed') and instance.confirmed: 
        send_mail_on_confirmation_success(instance)
