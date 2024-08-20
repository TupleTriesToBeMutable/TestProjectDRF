from rest_framework.viewsets import ModelViewSet
from webapp.serializers.userMessageSerializer import UserMessageSerializer
from webapp.models.userMessage import UserMessage
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class UserMessageController(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserMessageSerializer

    def get_queryset(self):
        user = self.request.user
        return UserMessage.objects.filter(user_id=user.id)
