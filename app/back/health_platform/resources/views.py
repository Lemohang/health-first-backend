from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer

class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    