
from .models import  Certificate
from rest_framework import viewsets
from .serializers import CertificateSerializer

class CertificateViewset(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
