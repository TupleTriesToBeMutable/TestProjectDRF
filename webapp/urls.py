from django.urls import path
from webapp.controllers import userAccount, guest, adminUser
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('guest/register', guest.register),
    path('guest/login', guest.user_login),
    path('guest/getinfo', guest.getinfo),
    path('user/<str:username>', userAccount.UserAccountController.as_view()),
    path('admin/users/<int:id>/', adminUser.AdminUserController.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
