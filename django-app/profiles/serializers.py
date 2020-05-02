
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
        read_only = ['user_type']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        BaseContentFactory.create(user)
        auth_login(self.context['request'], user)
        # TODO: get language from cookies and save it
        return user

    def create_from_demo_user(self, request, validated_data):
        user = request.user
        user.user_type = user.BASIC_USER
        user.email = validated_data["email"]
        user.set_password(validated_data["password"])
        user.save()
        auth_login(request, user)
        return user

    def validate_password(self, value):
        WeakPasswordValidator().validate(value)
        MaxLengthPasswordValidator().validate(value)
        return value
