from django.db import models

# Create your models here.


class Popolar_Categories(models.Model):
    name = models.CharField(max_length=100)
    available_position = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class Job_Listing(models.Model):
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)
    job_type =  models.CharField(max_length=50)
    photo_company = models.ImageField(upload_to="photo", null=True, blank=True)
    
                                    