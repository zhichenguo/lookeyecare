from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class User(AbstractUser):

    def __str__(self):
        return self.username
        # return self.get_full_name()
