from django.core.paginator import Paginator
from django.shortcuts import render
from .form import AppylForm
from .models import Job
from .filters import JobFilter


# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    # filters
    the_filtration = JobFilter(request.GET, queryset=job_list)
    job_list = the_filtration.qs

    paginator = Paginator(job_list, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj, 'the_filtration': the_filtration}
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, slug):
    # jobdetail = Job.objects.get(slug=slug)
    jobdetail = Job.objects.last()

    if request.method == 'POST':
        form = AppylForm(request.POST, request.FILES)
        if form.is_valid():
            saving_form = form.save(commit=False)
            saving_form.job = jobdetail
            saving_form.save()

    else:
        form = AppylForm()

    context = {'job': jobdetail, 'form': form}
    return render(request, 'jobs/job_detail.html', context)
