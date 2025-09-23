from django.urls import path
from .views import UserCreateView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", UserCreateView.as_view(), name="user-register"),
    path("profile/", ProfileView.as_view(), name="user-profile"),
]