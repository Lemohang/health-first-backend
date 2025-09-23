from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_patient', 'is_provider']

    def create(self, validated_data):
        # Use Django's create_user to hash password properly
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            is_patient=validated_data.get('is_patient', False),
            is_provider=validated_data.get('is_provider', False)
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # optional if you want to include user info

    class Meta:
        model = Profile
        fields = ['id', 'user', 'health_history', 'phone_number']
