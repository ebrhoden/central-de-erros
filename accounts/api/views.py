from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer


# Create your views here.


@api_view(['POST'])
@permission_classes((AllowAny,))
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered a new user.'
        data['email'] = account.email
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors

    return Response(data)
