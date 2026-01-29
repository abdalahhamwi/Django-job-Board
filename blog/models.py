from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    photo_post = models.ImageField(upload_to="blog/", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title
