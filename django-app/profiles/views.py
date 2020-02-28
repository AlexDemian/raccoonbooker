from django.shortcuts import render, redirect
from annoying.decorators import render_to
from django.contrib.auth import login as auth_login

@render_to('profiles/login.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    return {}

@render_to
def logout(request):
    return {}

