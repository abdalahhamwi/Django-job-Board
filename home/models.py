from django.db import models

# Create your models here.


class Job(models.Model):

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField()
    salary = models.IntegerField()
    category = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    