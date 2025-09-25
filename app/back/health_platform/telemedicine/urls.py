from django.urls import path
from .views import CreateVideoSessionView

urlpatterns = [
    path("video-session/<int:appointment_id>/", CreateVideoSessionView.as_view(), name="create-video-session"),
]
