from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

class ForceAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            login(request, get_user_model().objects.first())
        return self.get_response(request)