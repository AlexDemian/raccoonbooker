"""App root URL root-configuration."""

from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django_js_reverse.views import urls_js

# Template views
index = login_required(TemplateView.as_view(template_name="booker/index.html"))
error_page = TemplateView.as_view(template_name="common/alert-pages/error.html")
warning_page = TemplateView.as_view(template_name="common/alert-pages/warning.html")

urlpatterns = [
    # Apps
    path('', index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('booker/', include('booker.urls')),
    
    # REST
    path('api/v1/', include('config.api_urls')),
    
    #Errors
    path('alerts/error_page', error_page, name='error-page'),
    path('alerts/warning_page', warning_page, name='warning-page'),

    # Third party apps
    path(r'^i18n/', include('django.conf.urls.i18n')),
    path('jsreverse/', urls_js, name='js_reverse'),
]
