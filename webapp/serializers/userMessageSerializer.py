from rest_framework import serializers
from webapp.models.userMessage import UserMessage
from django.contrib.auth.models import User


class UserMessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = UserMessage
        fields = ['message', 'date', 'user']
