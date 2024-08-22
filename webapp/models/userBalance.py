from django.db import models
from django.contrib.auth.models import User


class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField()

