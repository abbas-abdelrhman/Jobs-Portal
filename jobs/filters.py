import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['job_title', 'job_type', 'category', 'description']
