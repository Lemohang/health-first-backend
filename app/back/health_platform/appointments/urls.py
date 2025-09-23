from django.urls import path
from .views import AppointmentListCreateView, AvailabilityListCreateView

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointments'),
    path('availability/', AvailabilityListCreateView.as_view(), name='availability'),
]
