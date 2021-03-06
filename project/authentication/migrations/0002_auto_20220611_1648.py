# Generated by Django 3.2.6 on 2022-06-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.CharField(default='English', max_length=16),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='Unset', max_length=128),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='Unset', max_length=16),
        ),
    ]
