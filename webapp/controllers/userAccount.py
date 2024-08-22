from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from webapp.serializers.userSerializer import UserSerializer


class UserAccountController(mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            generics.GenericAPIView):
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
