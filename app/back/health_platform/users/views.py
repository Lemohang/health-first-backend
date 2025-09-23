from rest_framework import generics, permissions
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

# -------------------------------
# User Registration
# -------------------------------
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can register

# -------------------------------
# Profile view
# -------------------------------
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Returns the profile for the logged-in user
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
