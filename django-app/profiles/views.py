from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from rest_framework.authtoken.models import Token
from annoying.decorators import render_to

from profiles.forms import LoginForm
from profiles.constants import ERROR_INCORRECT_CREDENTIALS
from profiles.helpers import send_mail_on_confirmation_success

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

class UserConfirmations(View):
    
    def get(self, request, token, *args, **kwargs):
        user = getattr(Token.objects.filter(key=token).first(), 'user', None)
        if not user or user.confirmed:
            return redirect('warning-page')
        user.confirmed = True
        user.save()
        auth_login(request, user)
        # TODO: make as signal
        send_mail_on_confirmation_success(user)
        return redirect('index')