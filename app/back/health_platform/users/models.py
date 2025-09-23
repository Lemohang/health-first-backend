from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    health_history = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return self.user.username
