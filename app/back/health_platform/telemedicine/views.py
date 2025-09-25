import requests
import jwt
import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import VideoSession
from appointments.models import Appointment

VIDEOSDK_API_KEY = "your_api_key"
VIDEOSDK_SECRET = "your_api_secret"

class CreateVideoSessionView(APIView):
    def post(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id)

        # 1. Create meeting room via VideoSDK REST API
        url = "https://api.videosdk.live/v2/rooms"
        headers = {"Authorization": VIDEOSDK_API_KEY}
        response = requests.post(url, headers=headers).json()
        room_name = response["roomId"]

        # 2. Generate JWT tokens (provider & patient)
        expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        provider_token = jwt.encode(
            {"roomId": room_name, "user": "provider", "exp": expiration},
            VIDEOSDK_SECRET,
            algorithm="HS256"
        )
        patient_token = jwt.encode(
            {"roomId": room_name, "user": "patient", "exp": expiration},
            VIDEOSDK_SECRET,
            algorithm="HS256"
        )

        # 3. Save in DB
        video_session = VideoSession.objects.create(
            appointment=appointment,
            room_name=room_name,
            provider_token=provider_token,
            patient_token=patient_token,
        )

        return Response({
            "roomId": room_name,
            "provider_token": provider_token,
            "patient_token": patient_token,
        })
