from django.db import models

# Create your models here.


class Popolar_Categories(models.Model):
    name = models.CharField(max_length=100)
    available_position = models.IntegerField()
