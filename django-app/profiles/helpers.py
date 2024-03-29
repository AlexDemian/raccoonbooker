from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_html_templated_mail(receivers, template_path, context, **kwargs):
    """Sends html emails.
    
    Arguments:
        receivers: list, emails of mail receivers
        template_path: string, system path to template
        context: dict, template context
    """

    subject = kwargs.get('subject', '')
    message = render_to_string(template_path, context)
    
    send_mail(
        subject, message,
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=receivers, 
        fail_silently=False, 
        html_message=message,
    )

def send_mail_on_registration_success(user, password):
    subject = 'Welcome to Raccoon Booker!'
    template_path = 'emails/registration_success.html'
    
    context = {
        'user_email': user.email,
        'user_password': password[:2] + '*' * (len(password) - 4) + password[-2:],
        'verification_url': user.verification_url,
    }
    send_html_templated_mail([user.email], template_path, context, subject=subject)

def send_mail_on_confirmation_success(user):    
    subject = 'Thank you for account confirmation!'
    template_path = 'emails/confirmation_success.html'
    send_html_templated_mail([user.email], template_path, {}, subject=subject)