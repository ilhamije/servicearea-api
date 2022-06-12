from django.http import Http404

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


from .serializers import (MyTokenObtainPairSerializer,
                        CustomUserSerializer)
                        # UseruniqSerializer)
from .models import CustomUser


class CustomUserCreate(APIView):
    """
    Create User
    """
    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = {
                    'refresh': str(RefreshToken.for_user(user)),
                    'access': str(RefreshToken.for_user(user).access_token)
                }
                json.update(serializer.data)
                return Response(json, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserList(APIView):
    """
    Returns list of Users
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        custom_user = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_user, many=True)
        return Response(serializer.data)


class CustomUserDetail(APIView):
    """
    Get, put and delete by id
    """
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
