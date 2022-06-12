from tkinter import N
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128, null=False)
    email = models.EmailField(_('email address'),unique=True)
    phone_number = models.CharField(max_length=16, default='Unset')
    language = models.CharField(max_length=16, default='English')
    currency = models.CharField(max_length=3, default='USD')
    is_staff = models.IntegerField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number','language','currency']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return '{}'.format(self.id)
