from django.urls import path
from profiles import views

urlpatterns = [
    path('login', views.login, name='login')
]
