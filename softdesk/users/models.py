from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(
        validators=[MinValueValidator(15)],
        verbose_name='Age',
        help_text='Age must be at least 15')

    email = models.EmailField(
        unique=True,
        verbose_name='Email')

    can_be_contacted = models.BooleanField(
        default=False,
        verbose_name='can be contacted')

    can_data_be_shared = models.BooleanField(
        default=False,
        verbose_name='can data be shared')
