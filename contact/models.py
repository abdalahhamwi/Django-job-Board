from django.db import models

# Create your models here.

class Contact (models.Model):
    
    message = models.TextField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100 , null=True , blank=True )
    
    def __str__(self):
        return self.name
