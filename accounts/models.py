from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    phone_number = models.IntegerField(max_length=12 , null=True , blank=True)


    def __str__(self):
        return self.email