from django.urls import path, include
from .models import Job
from rest_framework import routers, serializers, viewsets


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

