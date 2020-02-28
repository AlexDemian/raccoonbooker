from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from booker.factories import UserFactory, BaseContentFactory


class BaseContentGenerator(View):

    def post(self, request, *args, **kwargs):
        """Creates base content for account."""

        user = self.__create_demo_session(self.request.user)
        login(request, user)
        return redirect('index')

    def __create_demo_session(self, user):
        user = UserFactory.create(demo_user=True)
        BaseContentFactory.create(user)
        return user
