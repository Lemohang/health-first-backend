from django.db import models
from users.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, related_name='patient_appointments', on_delete=models.CASCADE)
    provider = models.ForeignKey(User, related_name='provider_appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending','Pending'),('confirmed','Confirmed'),('completed','Completed')])
    reason = models.TextField(blank=True, null=True)

class Availability(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0 = Monday
    start_time = models.TimeField()
    end_time = models.TimeField()
    
