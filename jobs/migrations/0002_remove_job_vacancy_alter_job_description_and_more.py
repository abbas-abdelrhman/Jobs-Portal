# Generated by Django 4.2 on 2023-04-29 22:14

from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Vacancy',
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=jobs.models.image_upload),
        ),
    ]
