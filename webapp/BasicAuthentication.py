from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class BasicAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_USERNAME')
        if not username:
            return None

        try:
            user = User.objects.get(username=username)
            authenticate(username=user.username, password=user.password)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None
