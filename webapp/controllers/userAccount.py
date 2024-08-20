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

    # def get_queryset(self):
    #     path_variables = self.request.parser_context.get('kwargs')
    #     username = path_variables.get(self.lookup_url_kwarg)
    #     return username

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(username=kwargs[self.lookup_url_kwarg])
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(serializer.data)
        # return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
