from django.shortcuts import render, redirect
from annoying.decorators import render_to
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

@render_to('profiles/login.html')
def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        auth_login(request.user)
        return redirect('index')
    return {'form': form}

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('login')
