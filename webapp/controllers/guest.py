import json

from django.contrib.auth.models import User
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from webapp.models.userBalance import UserBalance

@csrf_exempt
def register(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        if User.objects.filter(username=body['username']).exists():
            return HttpResponse(status=406)
        else:
            user = User.objects.create_user(username=body['username'],
                                            email=body['email'],
                                            password=body['password'])
            UserBalance.objects.create(user=user,
                                       balance=0)
            return HttpResponse(status=201)
    return HttpResponse(status=404)


@csrf_exempt
def user_login(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = authenticate(username=body['username'], password=body['password'])
        if user is not None:
            login(request, user)
            return HttpResponse(status=418)
        else:
            return HttpResponse(status=401)


def getinfo(request: HttpRequest):
    if request.method == 'GET' and request.user.is_authenticated:
        logout(request)
        return HttpResponse('Some info')
    else:
        return HttpResponse(status=401)

