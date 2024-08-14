import json

from django.contrib.auth.models import User
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import *

# валидацию json сделать, через jsonschema
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
            user.save()
            return HttpResponse(status=201)
