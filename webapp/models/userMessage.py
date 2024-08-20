from django.db import models
from django.contrib.auth.models import User


class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    date = models.DateTimeField()
