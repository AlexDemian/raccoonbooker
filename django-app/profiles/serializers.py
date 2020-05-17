
from rest_framework import serializers
from django.contrib.auth import login as auth_login

from profiles.models import User
from profiles.constants import ERROR_WEAK_PASSWORD
from profiles.validators import WeakPasswordValidator, MaxLengthPasswordValidator
from booker.factories import BaseContentFactory

class UserAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'user_type', 'date_joined']
        read_only_fields = ['user_type', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def _do_on_register(self, request, user, user_password):
        # TODO: get language from cookies and save it
        user.set_password(user_password)
        user.save()
        auth_login(request, user)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        self._do_on_register(self.context['request'], user, validated_data["password"])
        BaseContentFactory.create(user)
        return user

    def create_from_demo_user(self, request, validated_data):
        user = request.user
        user.user_type = user.BASIC_USER
        user.email = validated_data["email"]
        self._do_on_register(request, user, validated_data["password"])
        return user

    def validate_password(self, value):
        WeakPasswordValidator().validate(value)
        MaxLengthPasswordValidator().validate(value)
        return value
