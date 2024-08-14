from django.urls import path
from .controllers import guest

urlpatterns = [
    path('guest/register', guest.register),
    path('home/', guest.guest),
]
