from abc import ABC
from typing import Any
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ServiceAreaSerializer

from .models import ServiceArea


class CommonProcess(ABC):
    """
    Class for common processes
    """
    def get_userid(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        user, token = response
        user_id = token.payload.get('user_id')
        return user_id


class ServiceAreaByUser(APIView, CommonProcess):
    """
    Returns list of detail
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, user_id):
        try:
            return ServiceArea.objects.get(user_id=user_id)
        except ServiceArea.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user_id = self.get_userid(request)
        # area = self.get_object(user_id)
        area = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(area)
        return Response(serializer.data)


class ServiceAreaList(APIView, CommonProcess):
    """
    Returns list
    """
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        user_id = self.get_userid(request)
        if user_id:
            user = ServiceArea.objects.filter(user_id=user_id)
        else:
            user = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id = self.get_userid(request)
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaDetail(APIView, CommonProcess):
    """
    Returns list of detail
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user_id):
        try:
            return ServiceArea.objects.get(pk=pk, user_id=user_id)
        except ServiceArea.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_id = self.get_userid(request)
        area = self.get_object(user_id, pk)
        serializer = ServiceAreaSerializer(area)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        user_id = self.get_userid(request)
        area = self.get_object(user_id, pk)
        serializer = ServiceAreaSerializer(area, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_id = self.get_userid(request)
        area = self.get_object(user_id, pk)
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
