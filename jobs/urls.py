from django.urls import path
from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<str:slug>', views.job_detail, name="job_detail"),

    # class based views <-->

    path('api/jobs', api.JobsListApi.as_view(), name='job_list_api'),
    path('api/jobs/<int:id>', api.JobsDetailApi.as_view(), name='job_detail_api'),

    path('users/', api.UserList.as_view()),
    path('users/<int:pk>/', api.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
