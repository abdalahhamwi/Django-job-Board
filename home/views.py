from django.shortcuts import render, redirect
from job.models import Job_Detail


# Create your views here.


def home_view(request):
   job_detail = Job_Detail.objects.all()
   
   
   return render(request, "home.html", { 'job_detail': job_detail} )


def post_job(request):

    return render(request, "post_job.html")
    