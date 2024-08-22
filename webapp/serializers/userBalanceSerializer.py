from rest_framework import serializers
from webapp.models.userBalance import UserBalance
from django.contrib.auth.models import User


class UserBalanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = UserBalance
        fields = ['user', 'balance']
