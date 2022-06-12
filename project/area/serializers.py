from gettext import install
from typing import Any, Dict
from django.utils.translation import ugettext_lazy as _

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError
from rest_framework import serializers

from .models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        """
        Manage Service Area
        """
        model = ServiceArea
        fields = ['name', 'price', 'geojson_data', 'user_id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return ServiceArea.objects.create(**validated_data)

    # def get_absolute_url(self, obj):
    #     return reverse('servicearea_detail',kwargs={'pk': obj.id})

    def to_representation(self, instance: ServiceArea) -> Dict:
        data = dict()
        data['id'] = instance.id
        data['name'] = instance.name
        data['price'] = instance.price
        data['geojson_data'] = instance.geojson_data
        data['user_id'] = instance.user_id
        return data
