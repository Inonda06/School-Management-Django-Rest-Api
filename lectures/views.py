from .models import  Lecture
from rest_framework import viewsets
from .serializers import CertificateSerializer

class LecturesViewset(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = CertificateSerializer
