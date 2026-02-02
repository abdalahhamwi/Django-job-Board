from django.shortcuts import render
from home.models import Post_Job



# Create your views here.


def jobs_views(request):
    
   job_detail = Post_Job.objects.all()
   
   return render(request, "jobs.html", {"job_detail": job_detail})


def job_detail_views(request , id):
   
   job_detail  = Post_Job.objects.get(id=id)

   return render(request, "job_detail.html" , {"job_detail ": job_detail })