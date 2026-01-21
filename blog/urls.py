from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.blog_view, name="blog"),
    path("single_blog", views.single_blog_view, name="single_blog"),
]
