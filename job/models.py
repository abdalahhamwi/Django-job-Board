from django.db import models


# Create your models here.
class JobApplication(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website_portfolio_link = models.URLField(max_length=200, null=True, blank=True)
    cv = models.FileField(upload_to="cv/")
    cover_letter = models.TextField()
