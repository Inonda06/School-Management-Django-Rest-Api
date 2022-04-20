from .models import  Lecture
from rest_framework import serializers

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields=('title','description','duration','lecture_name','created_at','updated_at','is_required')