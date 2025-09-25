from rest_framework import serializers
from .models import VideoSession

class VideoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSession
        fields = ["id", "appointment", "room_name", "provider_token", "patient_token", "started_at", "ended_at"]
        