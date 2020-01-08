from django.shortcuts import render
from django.views import View
from booker.factories import UserFactory, BaseContentFactory
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

class DemoSession(View):

    def get(self, request, *args, **kwargs):
        """Creates demo account."""
        "http://localhost:8000/booker/demo"
        logout(request)
        if request.user.is_anonymous:
            user = self.__create_demo_session()
            login(request, user)
        return redirect('/api/booker/entries/')

    def __create_demo_session(self):
        import time
        user = UserFactory.create(username=int(time.time()))
        BaseContentFactory.create(user)
        return user

