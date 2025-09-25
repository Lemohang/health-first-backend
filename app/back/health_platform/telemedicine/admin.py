from django.contrib import admin
from .models import VideoSession

@admin.register(VideoSession)
class VideoSessionAdmin(admin.ModelAdmin):
    list_display = ("appointment", "room_name", "started_at", "ended_at")
