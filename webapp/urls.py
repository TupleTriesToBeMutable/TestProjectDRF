from django.urls import path
from .controllers import guest
from .controllers.user import UserController
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('guest/register', guest.register),
    path('guest/login', guest.user_login),
    path('guest/getinfo', guest.getinfo),
    path('admin/users/<int:pk>/', UserController.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
