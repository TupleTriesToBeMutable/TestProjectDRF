from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from webapp.serializers.userSerializer import UserSerializer


class AdminUserController(mixins.ListModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
