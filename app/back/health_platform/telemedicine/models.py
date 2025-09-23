from django.db import models
from users.models import User
from appointments.models import Appointment

class VideoSession(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    provider_token = models.TextField()
    patient_token = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
