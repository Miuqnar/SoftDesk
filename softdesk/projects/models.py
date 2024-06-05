from uuid import uuid4
from django.db import models
from django.conf import settings

from constants import (PRIORITY_CHOICES,
                       STATUS_CHOICES,
                       TAG_CHOICES,
                       TYPE_CHOICE)


class Project(models.Model):
    objects = None
    name = models.CharField(
        max_length=250,
        verbose_name='Name')

    description = models.CharField(
        max_length=1000,
        verbose_name='Project description')

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICE)

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True)


class Contributor(models.Model):
    objects = None
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    project = models.ForeignKey(
        to=Project,
        related_name='contributors',
        on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')


class Issue(models.Model):
    objects = None
    title = models.CharField(
        max_length=100,
        verbose_name='Title')

    description = models.CharField(
        max_length=1000,
        verbose_name='Issue description')

    project = models.ForeignKey(
        to=Project,
        related_name='issues',
        on_delete=models.CASCADE)

    assigned_to = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES)

    tag = models.CharField(
        max_length=7,
        choices=TAG_CHOICES)

    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=[0])

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True)


class Comment(models.Model):
    objects = None
    uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True)

    issue = models.ForeignKey(
        to=Issue,
        related_name='comments',
        on_delete=models.CASCADE)

    description = models.CharField(
        max_length=1000,
        verbose_name='Comment description')

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    created_time = models.DateTimeField(
        auto_now_add=True)