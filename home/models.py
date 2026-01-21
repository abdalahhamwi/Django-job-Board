from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.name
class Job(models.Model):

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField()
    salary = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    experience = models.CharField(max_length=10)

    def __str__(self):
        return self.title
