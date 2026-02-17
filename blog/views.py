from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog_view(request):
    
    create_post_blog = Blog.objects.all()
    return render( request , "blog.html" , {"create_post_blog": create_post_blog} )
