from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def image_upload(instance, filename):
    img_name, extension = filename.split('.')
    return "jobs/%s.%s" % (instance.id, extension)


class Job(models.Model):  # table
    job_title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    description = models.TextField(max_length=5000)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now=True)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    image = models.ImageField(upload_to=image_upload, blank=True, null=True)

    external_link = models.URLField()

    address = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)

    company_name = models.CharField(max_length=20, blank=True, null=True)
    application_link = models.URLField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        ## logic for save
        self.slug = slugify(self.job_title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ApplicantsData(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='apply/')
    cover_latter = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
