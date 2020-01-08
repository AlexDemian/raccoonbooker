from django.urls import include, path
from booker.views import DemoSession

urlpatterns = [
    path('demo', DemoSession.as_view(), name='demo-session'),
]