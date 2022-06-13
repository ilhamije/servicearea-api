from django.db import models

from authentication.models import CustomUser


class ServiceArea(models.Model):
    name = models.CharField(max_length=128, null=False)
    price = models.CharField(max_length=9, null=False)
    geojson_data = models.JSONField()
    user = models.ForeignKey(
        CustomUser, related_name='servicearea', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '{}'.format(self.id)
