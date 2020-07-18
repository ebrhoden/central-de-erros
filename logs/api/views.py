from django.db.models import Count
from rest_framework.pagination import PageNumberPagination

from .serializers import LogSerializer, LogSerializerWithFullAccess
from ..models import Log

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

# Don't forget that.
# 'DEFAULT_PERMISSION_CLASSES':[
#     'rest_framework.permissions.IsAuthenticated',
# ],


@api_view(['GET'])
def listLog(request):
    """Returns all logs associated to this specific user"""
    user = request.user
    try:
        logs = Log.objects.filter(user=user)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    except Log.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def detailLog(request, pk):
    """Returns information about a specific log"""
    try:
        log = Log.objects.filter(id=pk)
        serializer = LogSerializer(log, many=True)
        return Response(serializer.data)

    except Log.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateLog(request, pk):
    try:
        log = Log.objects.get(id=pk)
    except Log.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if user.is_staff:
        serializer = LogSerializerWithFullAccess(instance=log, data=request.data)
    else:
        serializer = LogSerializer(instance=log, data=request.data)

    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'update successful'
        return Response(data=data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteLog(request, pk):
    try:
        log = Log.objects.get(id=pk)

    except Log.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if log.user != user:
        return Response({'response': "You don't have permission to delete that."})

    operation = log.delete()
    data = {}
    if operation:
        data['success'] = 'delete successful'
    else:
        data['failure'] = 'delete failed'

    return Response(data=data)


@api_view(['POST'])
def createLog(request):
    """Creates a new log"""
    account = request.user
    log = Log(user=account)
    serializer = LogSerializer(log, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiLogListView(ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['level', 'description', 'origin', 'ambient']

    ordering_fields = ('level',)

