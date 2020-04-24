from django.views import View
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from booker.factories import UserFactory, BaseContentFactory

class BaseContentGenerator(View):

    def post(self, request, *args, **kwargs):
        """Creates new account and demo content for account."""

        user = UserFactory.create(demo_user=True)
        BaseContentFactory.create(user)
        login(request, user)
        return redirect('index')
