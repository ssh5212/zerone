from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    realname = models.TextField()
    hobby = models.CharField(max_length=50)
    forte = models.CharField(max_length=50)
    addr1 = models.CharField(max_length=200)
    intro = models.CharField(max_length=200)
    profileImage = models.TextField()
