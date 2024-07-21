from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Autor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=1000)
    date_of_creation = models.DateTimeField(max_length=1000)
    deadline = models.DateTimeField(max_length=1000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    tags = models.ManyToManyField('TaskTags')

    def __str__(self):
        return self.text


class TaskTags(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

