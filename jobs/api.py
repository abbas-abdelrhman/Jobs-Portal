from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Job
from .serializers import JobSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


# @api_view(['GET'])
# def job_list_api(request):
#     all_jobs = Job.objects.all()
#     data = JobSerializer(all_jobs, many=True).data
#     return Response({'data': data})
#
#
# @api_view(['GET'])
# def job_detail_api(request, id):
#     job_detail = Job.objects.get(id=id)
#     data = JobSerializer(job_detail).data
#     return Response({'data': data})
#

class JobsListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JobsDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
