from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post_Job(models.Model):

    type_job = [
        (" Part-time", "Part-time"),
        ("On-site", "On-site"),
        ("Remote", "Remote"),
        ("Hybrid", "Hybrid"),
    ]

    job_title = models.CharField(max_length=100)
    photo_company = models.ImageField(upload_to="photo", null=True, blank=True)
    Job_description = models.TextField(max_length=1000)
    Responsibility = models.TextField(max_length=1000 , null=True, blank=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=type_job)
    published_at = models.DateField(auto_now_add=True)
    Vacancy = models.IntegerField()
    salary = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.job_title)
        super(Post_Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.job_title
