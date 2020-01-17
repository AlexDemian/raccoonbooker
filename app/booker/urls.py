from django.urls import include, path
from booker.views import BaseContentGenerator

urlpatterns = [
    path('base_content_generator', BaseContentGenerator.as_view(), name='base-content-generator'),
]