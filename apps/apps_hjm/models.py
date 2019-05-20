from django.db import models
from django.contrib import admin
from apps.utils import TimeStampModel


class Board(TimeStampModel):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)


class Resume(TimeStampModel):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    career = models.CharField(max_length=200)
    introduce = models.CharField(max_length=300)


admin.site.register(Board)
admin.site.register(Resume)
