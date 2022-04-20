from attr import fields
from rest_framework import serializers,viewsets
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields= ('id','email','password','is_student')
        extra_kwargs={'password':{'write_only':True, }}

    def create(self, validated_data):
        is_student=validated_data.pop('is_student')
        user=get_user_model().objects.create_user(**validated_data)
        user.is_student=is_student
        user.save()
        return user
