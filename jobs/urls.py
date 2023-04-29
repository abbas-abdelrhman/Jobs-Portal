from django.urls import path
from . import views
from . import api


app_name = 'jobs'


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<str:slug>', views.job_detail, name="job_detail"),

    # # api ya basha
    # path('api/jobs', api.job_list_api, name='job_list_api'),
    # path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

    # class based views <-->

    path('api/jobs-list', api.JobsListApi.as_view(), name='job_list_api'),

    path('api/jobs-list/<int:id>', api.JobsDetailApi.as_view(), name='job_detail_api'),

]
