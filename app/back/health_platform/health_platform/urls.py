from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # App routes
    path('api/users/', include('users.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('api/resources/', include('resources.urls')),
    path('api/telemedicine/', include('telemedicine.urls')),

    # JWT Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
