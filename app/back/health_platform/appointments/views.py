from rest_framework import generics, permissions
from .models import Appointment, Availability
from .serializers import AppointmentSerializer, AvailabilitySerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_patient:
            return Appointment.objects.filter(patient=user)
        if user.is_provider:
            return Appointment.objects.filter(provider=user)
        return Appointment.objects.none()

class AvailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Availability.objects.filter(provider=self.request.user)
    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)
        