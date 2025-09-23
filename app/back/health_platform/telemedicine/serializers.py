from rest_framework import serializers
from .models import VideoSession

class VideoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSession
        fields = '__all__'
    def validate(self, data):
        if data['ended_at'] and data['ended_at'] < data['started_at']:
            raise serializers.ValidationError("ended_at cannot be earlier than started_at")
        return data
    