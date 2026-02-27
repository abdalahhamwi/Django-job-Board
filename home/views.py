from django.shortcuts import render, redirect
from .forms import PostJobForm
from . models import Post_Job
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_view(request):
   
   job_detail = Post_Job.objects.all()
   return render(request, "home.html", {"job_detail": job_detail} )

@login_required
def post_job(request):
   
   if request.method == "POST":
      add_post = PostJobForm(request.POST)
      if add_post.is_valid():
         add_post.save()
         return redirect ("home")
      else:
         add_post = PostJobForm()
         

   return render(request, "post_job.html" , {"add_post": PostJobForm} )
    