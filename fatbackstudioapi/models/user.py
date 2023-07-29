from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    isStaff = models.BooleanField()
