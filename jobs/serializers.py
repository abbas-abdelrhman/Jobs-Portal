from .models import Job
from rest_framework import serializers
from django.contrib.auth.models import User


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    job_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Job.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'job_owner']
