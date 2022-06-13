from typing import Any, Dict
from django.utils.translation import ugettext_lazy as _

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        """
        Manage Provider User
        """
        model = CustomUser
        fields = ['name', 'email', 'phone_number',
                'language', 'currency']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: Any):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance: Any, validated_data: Any):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)
        instance.email = email
        instance.set_password(password)
        instance.save()
        return instance

    def to_representation(self, instance: CustomUser) -> Dict:
        data = dict()
        data['id'] = instance.id
        data['name'] = instance.name
        data['email'] = instance.email
        data['phone_number'] = instance.phone_number
        data['language'] = instance.language
        data['currency'] = instance.currency
        return data

    # update function need email / password validation

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token
