# Generated by Django 3.2.6 on 2022-06-12 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicearea',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='servicearea', to=settings.AUTH_USER_MODEL),
        ),
    ]
