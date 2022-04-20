from .models import  Certificate
from rest_framework import serializers

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields=('name','description','created_at','updated_at',)