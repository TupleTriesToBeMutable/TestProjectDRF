from django.urls import path
from .controllers import guest

urlpatterns = [
    path('guest/register', guest.register),
    path('guest/login', guest.user_login),
    path('guest/getinfo', guest.getinfo),
]
