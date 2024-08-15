from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from webapp.serializers.userSerializer import UserSerializer


class UserController(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        #если авторизован
        return self.list(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

