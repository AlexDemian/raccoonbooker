from django.conf import settings

def get_server_url():
    pattern = "{proto}://{domain}"
    return pattern.format(**{
        'proto': settings.PROTO or 'http',
        'domain': settings.DOMAIN or 'undefined'
    })