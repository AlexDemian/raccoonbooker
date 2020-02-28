"""App root URL root-configuration."""

from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from django.views.generic.base import TemplateView
from django_js_reverse.views import urls_js

urlpatterns = [
    path('jsreverse/', urls_js, name='js_reverse'),
    path('', TemplateView.as_view(template_name="booker/index.html"), name='index'),
    path('profiles/', include('profiles.urls')),
    path('booker/', include('booker.urls')),
    path('api/booker/', include('booker.api_urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
