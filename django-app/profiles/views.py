from django.shortcuts import render, redirect
from annoying.decorators import render_to
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from profiles.forms import LoginForm
from profiles.constants import ERROR_INCORRECT_CREDENTIALS

@render_to('profiles/login.html')
def login(request):
    form = LoginForm(data=request.POST)
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user:
            auth_login(request,user)
            return redirect('index')
        print (user, request.POST['email'], request.POST['password'])
        form.lazy_errors = [ERROR_INCORRECT_CREDENTIALS]
    return {'login_form': form}


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('login')
