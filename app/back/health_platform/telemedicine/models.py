from django.db import models
from django.utils import timezone
from appointments.models import Appointment

class VideoSession(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    provider_token = models.TextField()
    patient_token = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"VideoSession for {self.appointment.id}"

    def end_session(self):
        """Mark the session as ended."""
        self.ended_at = timezone.now()   # ✅ set to current time
        self.save()
