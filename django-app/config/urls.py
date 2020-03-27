"""App root URL root-configuration."""

from django.urls import include, path
from django.views.generic.base import TemplateView
from django_js_reverse.views import urls_js

urlpatterns = [
    path(r'^i18n/', include('django.conf.urls.i18n')),
    path('jsreverse/', urls_js, name='js_reverse'),
    path('', TemplateView.as_view(template_name="booker/index.html"), name='index'),
    path('profiles/', include('profiles.urls')),
    path('booker/', include('booker.urls')),
    path('api/booker/', include('booker.api_urls')),
]
