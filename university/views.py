
from rest_framework import viewsets
from .models import University
from .Serializer import UniversitySerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
