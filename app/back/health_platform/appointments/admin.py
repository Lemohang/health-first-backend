
from django.contrib import admin
from .models import Appointment, Availability

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "provider", "date", "status", "reason")
    list_filter = ("status", "date", "provider")
    search_fields = ("patient__username", "provider__username", "reason")
    ordering = ("-date",)
    list_per_page = 20

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "provider", "day_of_week", "start_time", "end_time")
    list_filter = ("provider", "day_of_week")
    search_fields = ("provider__username",)
    ordering = ("provider", "day_of_week", "start_time")
